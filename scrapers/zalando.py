import re
import json
import logging
from bs4 import BeautifulSoup
from .base import BaseScraper

log = logging.getLogger(__name__)

SEARCH_URL = "https://www.zalando.be/catalog/"


class ZalandoScraper(BaseScraper):
    name = "zalando"

    def search(self, query: str, max_results: int = 3) -> list[dict]:
        resp = self._get(
            SEARCH_URL,
            params={"q": query},
            extra_headers={"Accept-Language": "en-BE,en;q=0.9"},
        )
        soup = BeautifulSoup(resp.text, "html.parser")
        results = []

        # Zalando embeds catalogue state in a JSON script tag
        for tag in soup.find_all("script", type="application/json"):
            try:
                data = json.loads(tag.string or "")
                # Look for a list that contains objects with priceRange/displayName
                articles = None
                if isinstance(data, dict):
                    articles = (
                        data.get("graphqlCache", {}) or
                        data.get("articles") or
                        data.get("results")
                    )
                if not articles:
                    continue

                # Normalise: sometimes it's a dict of {sku: {...}}
                items = articles.values() if isinstance(articles, dict) else articles
                for item in list(items)[:max_results * 3]:
                    if not isinstance(item, dict):
                        continue
                    name  = item.get("name") or item.get("displayName")
                    price = (item.get("price") or {}).get("current") or \
                            (item.get("priceRange") or {}).get("min")
                    url   = item.get("url") or item.get("uri", "")
                    if not name or not price:
                        continue
                    results.append({
                        "name":     str(name)[:120],
                        "price":    float(price),
                        "currency": "EUR",
                        "url":      url if url.startswith("http") else "https://www.zalando.be" + url,
                        "in_stock": True,
                    })
                    if len(results) >= max_results:
                        break
                if results:
                    return results
            except (json.JSONDecodeError, TypeError, ValueError):
                continue

        # Fallback: parse article cards
        for card in soup.select("article[class]"):
            try:
                name_el  = card.select_one("h3, [class*='title'], [class*='name']")
                price_el = card.select_one("[class*='price']")
                link_el  = card.select_one("a[href]")
                if not name_el or not price_el:
                    continue
                price_text = re.sub(r"[^\d.,]", "", price_el.get_text())
                price = float(price_text.replace(",", "."))
                href = link_el["href"] if link_el else ""
                results.append({
                    "name":     name_el.get_text(strip=True)[:120],
                    "price":    price,
                    "currency": "EUR",
                    "url":      href if href.startswith("http") else "https://www.zalando.be" + href,
                    "in_stock": True,
                })
                if len(results) >= max_results:
                    break
            except (ValueError, AttributeError):
                continue

        return results
