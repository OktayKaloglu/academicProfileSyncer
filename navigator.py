import logging
import random
import sys
import re
import time
from urllib.parse import urlparse

from bs4 import BeautifulSoup
from httpx import TimeoutException
from requests.exceptions import Timeout
from data_types import OrganizationParserStruct

from proxy_generator import MaxTryException, ProxyGenerator, DOSException


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Navigator(object, metaclass=Singleton):
    def __init__(self):
        # super(Navigator, self).__init__()
        super().__init__()
        self.logger = logging.getLogger("navigator")
        self._timeout_obj = 5
        self._max_retries = 5
        # Both of them freeproxy
        self.proxy_manager_1 = ProxyGenerator()
        self.proxy_manager_2 = ProxyGenerator()
        self._session1 = self.proxy_manager_1.get_session()
        self._session2 = self.proxy_manager_2.get_session()
        self.got_403 = False
        self.proxy_manager_1.set_logger(True)
        self.proxy_manager_2.set_logger(True)
        self.debug_print_printed = False

    def set_logger(self, enable: bool):
        handler = logging.StreamHandler()  # output to console
        formatter = logging.Formatter("NAVIGATOR: %(levelname)s: %(message)s")
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
        self.logger.setLevel(logging.INFO if enable else logging.CRITICAL)

    def set_timeout(self, timeout: int):
        if timeout >= 0:
            self._timeout_obj = timeout

    def use_proxy(self):
        proxy_works = self.proxy_manager_1.FreeProxies()
        proxy_works2 = self.proxy_manager_2.FreeProxies()
        if not proxy_works and proxy_works2:
            self.proxy_manager_1 = self.proxy_manager_2
        if not proxy_works2 and proxy_works:
            sys.exit(1)
        if proxy_works and not proxy_works2:
            self.proxy_manager_2 = self.proxy_manager_1

        self._session1 = self.proxy_manager_1.get_session()
        self._session2 = self.proxy_manager_2.get_session()
        self.logger.info("Sessions started")

    def _new_session(self, **kwargs):
        self.got_403 = False
        self._session2 = self.proxy_manager_2._new_session(**kwargs)

    def _get_page(self, page_request: str) -> str:
        self.logger.info("Getting %s", page_request)
        resp = None
        tries = 0
        proxy_manager = self.proxy_manager_2
        session = self._session2
        timeout = self._timeout_obj
        while tries < self._max_retries:
            self.logger.info("Current tries: %d", tries)
            if self._max_retries - 1 == tries:
                raise MaxTryException(f"Cannot fetch this url: {page_request}")
            try:
                random_wait = random.uniform(1, 2)
                time.sleep(random_wait)
                resp = session.get(page_request, timeout=timeout)

                # Probably we should use debug instead of info
                if proxy_manager._proxies == {}:
                    self.logger.info("Session running on no proxy mode")
                    self.debug_print_printed = True
                else:
                    if self.debug_print_printed is not True:
                        self.logger.info(
                            "Session proxy config is %s", proxy_manager._proxies
                        )
                        self.debug_print_printed = True

                # Do we need captcha handling?
                # has_captcha bla bla

                if resp.status_code == 200:
                    return resp.text
                elif resp.status_code == 404:
                    self.logger.info("Got a 404 error. Attempting with same proxy")
                    tries += 1
                    self.logger.info("Increased tries! now tries is: %d", tries)
                    continue
                elif resp.status_code == 403:
                    self.logger.info("Got an access denied error (403).")
                    if not proxy_manager.has_proxy():
                        self.logger.info("No connections possible")
                        if not self.got_403:
                            self.logger.info(
                                "Retrying immediately with another session"
                            )
                        else:
                            random_wait = random.uniform(60, 2 * 120)
                            self.logger.info(
                                "Will retry after %.2f seconds (with another session).",
                                random_wait,
                            )
                            time.sleep(random_wait)
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
                if not proxy_manager.has_proxy():
                    self.logger.info("No other connections possible.")
                    random_wait = random.uniform(60, 2 * 60)
                    self.logger.info(
                        "Will retry after %.2f seconds (with the same session).",
                        random_wait,
                    )
                    time.sleep(random_wait)
                    continue

            except (Timeout, TimeoutException) as error:
                err = "Timeout Exception %s while fetching page: %s" % (
                    type(error).__name__,
                    error.args,
                )
                self.logger.info(err)
                if timeout < 3 * self._timeout_obj:
                    self.logger.info(
                        "Increasing timeout and retrying within same session."
                    )
                    timeout = timeout + self._timeout_obj
                    continue
                self.logger.info("Giving up this session.")
            except Exception as error:
                err = "Exception %s while fetching page: %s" % (
                    type(error).__name__,
                    error.args,
                )
                self.logger.info(err)
                self.logger.info("Retrying with a new session.")

            self.logger.info("Tries increased")
            tries += 1

            self.logger.info("Tries increased current tries cound -> %d", tries)

            try:
                session, timeout = proxy_manager.get_next_proxy(
                    num_tries=tries,
                    old_timeout=timeout,
                    old_proxy=proxy_manager._proxies.get("http", None),
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
        try:
            html = self._get_page(url)
        except MaxTryException:
            raise MaxTryException(f"Cannot fetch this URL:{url}")
        # Special html char, replace it
        html = html.replace("\xa0", " ")
        res = BeautifulSoup(html, "html.parser")
        return res

    def _filter_link(
        self,
        href: str,
        organization: OrganizationParserStruct,
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

        base_schema = urlparse(organization.source)
        href_schema = urlparse(href)

        # Path validation
        if href_schema.path == b"":
            return None

        # Check blacklisted word
        if organization.blacklist is not None:
            for word in organization.blacklist:
                if word.lower() in href_schema.path.lower():
                    return None

        # check is href includes http or not
        if href_schema.scheme != "":
            if href in organization.exact_url_blacklist:
                return None
            return href
        if organization.base_url_ending != "":
            builded_url = (
                base_schema.scheme
                + "://"
                + base_schema.netloc
                + organization.base_url_ending
                + href_schema.path
            )
            if builded_url in organization.exact_url_blacklist:
                return None
            return builded_url

        builded_url_bs = (
            base_schema.scheme + "://" + base_schema.netloc + href_schema.path
        )
        if builded_url_bs in organization.exact_url_blacklist:
            return None
        return builded_url_bs

    def search_organization(
        self,
        organization: OrganizationParserStruct,
    ) -> list:
        soup = self._get_soup(organization.source)
        rows = soup.find_all("a")

        if rows:
            self.logger.info("Found links on page")

        res = []
        seen_urls = set()

        self.logger.info("Starting filtering process for links")
        for link in rows:
            filtered = self._filter_link(
                href=link.get("href"),
                organization=organization,
            )
            if filtered is not None and filtered not in seen_urls:
                res.append(filtered)
                seen_urls.add(filtered)
        self.logger.info("Links gathered")
        for i in res:
            try:
                self._extract_course_page(i, organization)
            except MaxTryException:
                self.logger.info("This url cannot be fetched %s", i)
                continue
        return res

    def _extract_course_page(self, url: str, organization: OrganizationParserStruct):
        try:
            soup = self._get_soup(url)
        except MaxTryException:
            raise MaxTryException(f"Cannot fetch this URL: {url}")

        if organization.uses_single_line_information_on_instructor:
            input_for_instructor = (
                soup.select(organization.instructor_selector)[0].get_text().strip()
            )
            match2 = re.match(
                organization.single_line_instructor_regex, input_for_instructor
            )
            if match2:
                instructor_name = match2.group(1).strip()
            else:
                instructor_name = None
        else:
            instructor_name = (
                soup.select(organization.instructor_selector)[0].get_text().strip()
            )
            if instructor_name == "":
                instructor_name = None

        if organization.uses_single_line_information_on_course:
            # course code
            inpt = soup.select(organization.course_code_selector)[0].get_text().strip()
            match = re.match(organization.single_line_course_regex, inpt)
            if match:
                # course code
                course_code = match.group(1).strip()
                course_name = match.group(2).strip()
            else:
                course_name = None
                # course code
                course_code = None

        else:
            # This is course code for seperate selectors!
            course_code = (
                soup.select(organization.course_code_selector)[0].get_text().strip()
            )
            course_name = (
                soup.select(organization.course_name_selector)[0].get_text().strip()
            )

        if instructor_name is None:
            self.logger.info("Not founded instructor at url: %s", url)

        if course_code is None:
            self.logger.info("Not founded course code at url: %s", url)

        if course_name is None:
            self.logger.info("Not founded course name at url: %s", url)

        print(instructor_name)
        print(course_code)
        print(course_name)
