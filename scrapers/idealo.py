import re
import json
import logging
from bs4 import BeautifulSoup
from .base import BaseScraper

log = logging.getLogger(__name__)

SEARCH_URL = "https://www.idealo.be/nl/preisvergleich/MainSearchProductCategory.html"


class IdealoScraper(BaseScraper):
    name = "idealo"

    def search(self, query: str, max_results: int = 3) -> list[dict]:
        resp = self._get(
            SEARCH_URL,
            params={"q": query},
            extra_headers={
                "Accept-Language": "nl-BE,nl;q=0.9,fr-BE;q=0.8,en;q=0.7",
                "Referer": "https://www.idealo.be/",
                "Cache-Control": "no-cache",
            },
        )
        soup = BeautifulSoup(resp.text, "html.parser")

        # ── Strategy 1: JSON-LD structured data ──────────────────────────────
        results = self._parse_jsonld(soup, max_results)
        if results:
            return results

        # ── Strategy 2: embedded __NEXT_DATA__ / window.__INITIAL_STATE__ ────
        results = self._parse_next_data(soup, max_results)
        if results:
            return results

        # ── Strategy 3: HTML product cards ────────────────────────────────────
        return self._parse_html_cards(soup, max_results)

    def _parse_jsonld(self, soup, max_results):
        results = []
        for tag in soup.find_all("script", type="application/ld+json"):
            try:
                data = json.loads(tag.string or "")
                items = data if isinstance(data, list) else [data]
                for item in items:
                    if item.get("@type") == "ItemList":
                        for entry in item.get("itemListElement", []):
                            product = entry.get("item", entry)
                            name  = product.get("name")
                            offer = product.get("offers") or product.get("offer")
                            if isinstance(offer, list):
                                offer = offer[0]
                            if not name or not offer:
                                continue
                            price = offer.get("price") or offer.get("lowPrice")
                            url   = product.get("url") or offer.get("url", "")
                            if not price:
                                continue
                            results.append({
                                "name":     str(name)[:120],
                                "price":    float(price),
                                "currency": offer.get("priceCurrency", "EUR"),
                                "url":      url,
                                "in_stock": True,
                            })
                            if len(results) >= max_results:
                                return results
            except (json.JSONDecodeError, TypeError, ValueError):
                continue
        return results

    def _parse_next_data(self, soup, max_results):
        tag = soup.find("script", id="__NEXT_DATA__")
        if not tag:
            return []
        try:
            data  = json.loads(tag.string or "")
            # Walk common key paths Idealo uses
            props = data.get("props", {}).get("pageProps", {})
            products = (
                props.get("products") or
                props.get("searchResult", {}).get("products") or
                props.get("initialData", {}).get("products") or
                []
            )
            results = []
            for p in products[:max_results]:
                price = (
                    p.get("price", {}).get("current") or
                    p.get("cheapestOffer", {}).get("price") or
                    p.get("priceMin")
                )
                if not price:
                    continue
                url = p.get("url") or p.get("detailPageUrl") or ""
                if url and not url.startswith("http"):
                    url = "https://www.idealo.be" + url
                results.append({
                    "name":     str(p.get("name") or p.get("title") or "")[:120],
                    "price":    float(price),
                    "currency": "EUR",
                    "url":      url,
                    "in_stock": True,
                })
            return results
        except (json.JSONDecodeError, TypeError, ValueError):
            return []

    def _parse_html_cards(self, soup, max_results):
        results = []
        # Idealo uses a variety of class patterns across redesigns
        selectors = [
            "[class*='offerList-item']",
            "[class*='resultList'] li",
            "[class*='result-list'] li",
            "[class*='sr-resultList'] li",
            "[data-testid*='product-card']",
            "article",
        ]
        cards = []
        for sel in selectors:
            cards = soup.select(sel)
            if cards:
                break

        for card in cards:
            try:
                name_el = (
                    card.select_one("[class*='title']") or
                    card.select_one("[class*='name']") or
                    card.select_one("h2, h3, h4")
                )
                price_el = (
                    card.select_one("[class*='price']:not([class*='old']):not([class*='strike'])") or
                    card.select_one("[data-testid*='price']")
                )
                link_el = card.select_one("a[href]")

                if not name_el or not price_el:
                    continue

                raw = re.sub(r"[^\d,.]", "", price_el.get_text(strip=True))
                if not raw:
                    continue
                # Idealo uses comma as decimal separator (€ 12,99)
                price = float(raw.replace(".", "").replace(",", "."))
                href = link_el["href"] if link_el else ""
                if href and not href.startswith("http"):
                    href = "https://www.idealo.be" + href

                results.append({
                    "name":     name_el.get_text(strip=True)[:120],
                    "price":    price,
                    "currency": "EUR",
                    "url":      href,
                    "in_stock": True,
                })
                if len(results) >= max_results:
                    break
            except (ValueError, AttributeError):
                continue

        return results
