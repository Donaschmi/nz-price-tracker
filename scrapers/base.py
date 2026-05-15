import logging
import time
import random
from abc import ABC, abstractmethod
from curl_cffi import requests

log = logging.getLogger(__name__)

BROWSER_HEADERS = {
    "Accept":          "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection":      "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest":  "document",
    "Sec-Fetch-Mode":  "navigate",
    "Sec-Fetch-Site":  "none",
    "Sec-Fetch-User":  "?1",
    "Cache-Control":   "max-age=0",
}


class BaseScraper(ABC):
    name: str = ""

    def _get(self, url: str, *, params=None, extra_headers=None, timeout=12):
        headers = {**BROWSER_HEADERS, **(extra_headers or {})}
        time.sleep(random.uniform(1.5, 3.0))
        resp = requests.get(
            url,
            params=params,
            headers=headers,
            timeout=timeout,
            impersonate="chrome124",  # Spoofs Chrome 124 TLS fingerprint
        )
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
