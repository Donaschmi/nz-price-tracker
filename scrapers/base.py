import logging
import time
import random
import requests
from abc import ABC, abstractmethod

log = logging.getLogger(__name__)

BROWSER_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "en-US,en;q=0.9",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
}


class BaseScraper(ABC):
    name: str = ""
    _session: requests.Session | None = None

    def _get_session(self) -> requests.Session:
        if self._session is None:
            self._session = requests.Session()
            self._session.headers.update(BROWSER_HEADERS)
        return self._session

    def _get(self, url: str, *, params=None, extra_headers=None, timeout=20) -> requests.Response:
        session = self._get_session()
        headers = {**BROWSER_HEADERS, **(extra_headers or {})}
        time.sleep(random.uniform(1.5, 3.5))
        resp = session.get(url, params=params, headers=headers, timeout=timeout)
        resp.raise_for_status()
        return resp

    @abstractmethod
    def search(self, query: str, max_results: int = 3) -> list[dict]:
        """Return list of dicts: {name, price, url, currency, in_stock}."""
        ...

    def safe_search(self, query: str, max_results: int = 3) -> list[dict]:
        try:
            return self.search(query, max_results)
        except Exception as e:
            log.warning("%s: search(%r) failed — %s", self.name, query, e)
            return []
