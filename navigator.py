import logging
import random
import sys
import time
from urllib.parse import urlparse

from bs4 import BeautifulSoup
from httpx import TimeoutException
from requests.exceptions import Timeout

from proxy_generator import ProxyGenerator, DOSException


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Navigator(object, metaclass=Singleton):
    def __init__(self):
        super(Navigator, self).__init__()
        self.logger = logging.getLogger("navigator")
        self._TIMEOUT = 5
        self._max_retries = 5
        # Both of them freeproxy
        self.pm1 = ProxyGenerator()
        self.pm2 = ProxyGenerator()
        self._session1 = self.pm1.get_session()
        self._session2 = self.pm2.get_session()
        self.got_403 = False
        self.pm1.set_logger(True)
        self.pm2.set_logger(True)

    def set_logger(self, enable: bool):
        handler = logging.StreamHandler()  # output to console
        formatter = logging.Formatter("NAVIGATOR: %(levelname)s: %(message)s")
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
        self.logger.setLevel(logging.INFO if enable else logging.CRITICAL)

    def set_timeout(self, timeout: int):
        if timeout >= 0:
            self._TIMEOUT = timeout

    def use_proxy(self):
        proxy_works = self.pm2.FreeProxies()
        proxy_works2 = self.pm2.FreeProxies()
        if not proxy_works and proxy_works2:
            self.pm1 = self.pm2
        if not proxy_works2 and proxy_works:
            sys.exit(1)
        if proxy_works and not proxy_works2:
            self.pm2 = self.pm1

        self._session1 = self.pm1.get_session()
        self._session2 = self.pm2.get_session()
        self.logger.info("Sessions started")

    def _new_session(self, **kwargs):
        self.got_403 = False
        self._session2 = self.pm2._new_session(**kwargs)

    def _get_page(self, page_request: str) -> str:
        self.logger.info("Getting %s", page_request)
        resp = None
        tries = 0
        pm = self.pm2
        session = self._session2
        timeout = self._TIMEOUT
        while tries < self._max_retries:
            try:
                w = random.uniform(1, 2)
                time.sleep(w)
                resp = session.get(page_request, timeout=timeout)

                # Probably we should use debug instead of info
                self.logger.info("Session proxy config is {}".format(pm._proxies))

                # Do we need captcha handling?
                # has_captcha bla bla

                if resp.status_code == 200:
                    return resp.text
                elif resp.status_code == 404:
                    self.logger.info("Got a 404 error. Attempting with same proxy")
                    tries += 1
                    continue
                elif resp.status_code == 403:
                    self.logger.info("Got an access denied error (403).")
                    if not pm.has_proxy():
                        self.logger.info("No connections possible")
                        if not self.got_403:
                            self.logger.info(
                                "Retrying immediately with another session"
                            )
                        else:
                            w = random.uniform(60, 2 * 120)
                            self.logger.info(
                                "Will retry after %.2f seconds (with another session).",
                                w,
                            )
                            time.sleep(w)
                        self._new_session()
                        self.got_403 = True
                        continue  # Retry request same session
                    else:
                        self.logger.info(
                            "Currently trying another connection with different session"
                        )
                elif resp.status_code == 302 and resp.has_redirect_location:
                    self.logger.debug("Got a redirect, checking...")
                    page_request = resp.headers["location"]
                else:
                    self.logger.info(
                        """Response code %d, Retrying...""", resp.status_code
                    )
            except DOSException:
                if not pm.has_proxy():
                    self.logger.info("No other connections possible.")
                    w = random.uniform(60, 2 * 60)
                    self.logger.info(
                        "Will retry after %.2f seconds (with the same session).", w
                    )
                    time.sleep(w)
                    continue

            except (Timeout, TimeoutException) as e:
                err = "Timeout Exception %s while fetching page: %s" % (
                    type(e).__name__,
                    e.args,
                )
                self.logger.info(err)
                if timeout < 3 * self._TIMEOUT:
                    self.logger.info(
                        "Increasing timeout and retrying within same session."
                    )
                    timeout = timeout + self._TIMEOUT
                    continue
                self.logger.info("Giving up this session.")
            except Exception as e:
                err = "Exception %s while fetching page: %s" % (
                    type(e).__name__,
                    e.args,
                )
                self.logger.info(err)
                self.logger.info("Retrying with a new session.")

            self.logger.info("Tries increased")
            tries += 1

            self.logger.info("Tries increased current tries cound -> %d", tries)

            try:
                session, timeout = pm.get_next_proxy(
                    num_tries=tries,
                    old_timeout=timeout,
                    old_proxy=pm._proxies.get("http", None),
                )
            except Exception:
                self.logger.info(
                    "No other secondary connections possible. "
                    "Using the primary proxy for all requests."
                )
                break

        return self._get_page(page_request)

    def _set_retries(self, num_retries: int) -> None:
        if num_retries < 0:
            raise ValueError("num_retries must not be negative")
        self._max_retries = num_retries

    def _get_soup(self, url: str) -> BeautifulSoup:
        html = self._get_page(url)
        # Special html char, replace it
        html = html.replace("\xa0", " ")
        res = BeautifulSoup(html, "html.parser")
        return res

    def _filter_link(
        self, href: str, base_url: str, blacklist: list[str] = None
    ) -> str | None:
        builtin_include_filter = ["#", "javascript:", "mailto:"]
        builtin_equal_filter = ["/"]

        # Validate href
        if href is None:
            return None

        for char in builtin_equal_filter:
            if href == char:
                return None

        for bfilter in builtin_include_filter:
            if bfilter in href:
                return None

        base_schema = urlparse(base_url)
        href_schema = urlparse(href)

        # Path validation
        if href_schema.path == b"" or "":
            return None

        # Check blacklisted word
        if blacklist is not None:
            for word in blacklist:
                if word.lower() in href_schema.path.lower():
                    return None

        # check is href includes http or not
        if href_schema.scheme != "" or b"":
            return href
        else:
            return base_schema.scheme + "://" + base_schema.netloc + href_schema.path

    def search_organization(self, url: str, filter_source: str = None) -> list:
        soup = self._get_soup(url)
        rows = soup.find_all("a")
        blacklist = ["DersOgretimPlaniPdf", "sayfa"]

        if rows:
            self.logger.info("Found links on page")

        res = []
        seen_urls = set()

        self.logger.info("Starting filtering process for links")
        for link in rows:
            filtered = self._filter_link(
                href=link.get("href"), base_url=url, blacklist=blacklist
            )
            if filtered is not None and filtered not in seen_urls:
                res.append({"course": filtered})
                seen_urls.add(filtered)
        self.logger.info("Links gathered")
        return res
