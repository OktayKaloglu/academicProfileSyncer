from fake_useragent import UserAgent
import httpx
from typing import Callable
import requests
import time
from fp.fp import FreeProxy
import logging
from data_types import ProxyMode


class DOSException(Exception):
    """DOS attack exception"""


class MaxTryException(Exception):
    """Max try exception"""


class ProxyGenerator(object):
    def __init__(self):
        self.logger = logging.getLogger("proxy_generator")
        self._proxy_gen = None
        self._proxy_used = False
        self.proxy_mode = None
        self._proxies = {}
        self._session = None
        self._proxy_works = False
        self._TIMEOUT = 5
        self._new_session()

    def get_session(self):
        return self._session

    def set_logger(self, enable: bool):
        handler = logging.StreamHandler()  # output to console
        formatter = logging.Formatter("%(levelname)s: %(message)s")
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
        self.logger.setLevel(logging.INFO if enable else logging.CRITICAL)

    def __del__(self):
        self._close_session()

    def _check_proxy(self, proxies) -> bool:
        with requests.Session() as session:
            session.proxies = proxies
            try:
                resp = session.get("http://httpbin.org/ip", timeout=self._TIMEOUT)
                if resp.status_code == 200:
                    self.logger.info(
                        "Proxy works! IP address: %s", resp.json()["origin"]
                    )
                    return True
                elif resp.status_code == 401:
                    self.logger.warning("Incorrect credentials for proxy!")
                    return False
            except TimeoutError:
                time.sleep(self._TIMEOUT)
            except Exception as e:
                self.logger.info("Exception while testing proxy: %s", e)
            return False

    def _new_session(self, **kwargs):
        # Accepts the redirect to another site.
        init_kwargs = {"follow_redirects": True}
        init_kwargs.update(kwargs)
        proxies = {}
        if self._session:
            proxies = self._proxies
            self._close_session()
        self.got_403 = False

        user_agent = UserAgent().random

        _HEADERS = {
            "accept-language": "en-US,en,tr,tr-TR",
            "accept": "text/html,application/xhtml+xml,application/xml",
            "User-Agent": user_agent,
        }
        # self._session.headers.update(_HEADERS)
        init_kwargs.update(headers=_HEADERS)

        if self._proxy_works:
            init_kwargs["proxies"] = proxies  # .get("http", None)
            self._proxies = proxies
        self._session = httpx.Client(**init_kwargs)

        return self._session

    def _close_session(self):
        if self._session:
            self._session.close()

    # wait-time is seconds
    def _fp_coroutine(self, timeout=1, wait_time=120):
        """Get a free proxy from free-proxy-list.net."""
        freeproxy = FreeProxy(rand=False, timeout=timeout)
        if not hasattr(self, "_dirty_freeproxies"):
            self._dirty_freeproxies = set()
        try:
            all_proxies = freeproxy.get_proxy_list(repeat=False)  # free-proxy >= 1.1.0
        # Library version checking
        except TypeError:
            all_proxies = freeproxy.get_proxy_list()  # free-proxy < 1.1.0
        all_proxies.reverse()

        t1 = time.time()
        # This function checks if proxies are working
        # if not it adds them to the dirty list
        # and gets a new proxy from the list
        # if it works yields the proxy for the usage
        while time.time() - t1 < wait_time:
            proxy = all_proxies.pop()
            if not all_proxies:
                all_proxies = freeproxy.get_proxy_list()
            if proxy in self._dirty_freeproxies:
                continue
            proxies = {"http://": proxy, "https://": proxy}
            proxy_works = self._check_proxy(proxies)
            if proxy_works:
                # Stop execution callback with yield
                dirty_proxy = yield proxy
                t1 = time.time()
            else:
                dirty_proxy = proxy

            self.logger.info("Added dirty proxy to the dict ->")
            self.logger.info(str(proxy))
            self._dirty_freeproxies.add(dirty_proxy)

    def FreeProxies(self, timeout=1, wait_time=120):
        self.proxy_mode = ProxyMode.FREE_PROXIES

        self._fp_gen = self._fp_coroutine(timeout=timeout, wait_time=wait_time)
        self._proxy_gen = self._fp_gen.send
        proxy = self._proxy_gen(None)  # prime the generator
        self.logger.info("Trying with proxy %s", proxy)
        proxy_works = self._use_proxy(proxy)
        n_retries = 200
        n_tries = 0

        while (not proxy_works) and (n_tries < n_retries):
            self.logger.info("Trying with proxy %s", proxy)
            proxy_works = self._use_proxy(proxy)
            n_tries += 1
            if not proxy_works:
                proxy = self._proxy_gen(proxy)

        if n_tries == n_retries:
            n_dirty = len(self._dirty_freeproxies)
            self._fp_gen.close()
            msg = (
                "None of the free proxies are working at the moment. "
                f"Marked {n_dirty} proxies dirty. Try again after a few minutes."
            )
            raise MaxTryException(msg)
        else:
            return True

    def has_proxy(self) -> bool:
        return self._proxy_gen

    def _set_proxy_generator(self, gen: Callable[..., str]) -> bool:
        self._proxy_gen = gen
        return True

    def get_next_proxy(self, num_tries=None, old_timeout=3, old_proxy=None):
        new_timeout = old_timeout
        if self._proxy_gen:
            if num_tries:
                self.logger.info("Try #%d failed. Switching proxy.", num_tries)
            # Try to get another proxy
            new_proxy = self._proxy_gen(old_proxy)
            while not self._use_proxy(new_proxy):
                new_proxy = self._proxy_gen(new_proxy)
            new_timeout = self._TIMEOUT  # Reset timeout to default
            self._new_session()
        else:
            self._new_session()

        return self._session, new_timeout

    def _use_proxy(self, http: str, https: str = None) -> bool:
        if http[:4] != "http":
            http = "http://" + http
        if https is None:
            https = http
        elif https[:5] != "https":
            https = "https://" + https

        proxies = {"http://": http, "https://": https}
        self._proxy_works = self._check_proxy(proxies)

        if self._proxy_works:
            self._proxies = proxies
            self._new_session(proxies=proxies)

        return self._proxy_works
