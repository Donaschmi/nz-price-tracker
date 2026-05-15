#!/usr/bin/env python3
"""Daily price tracker for NZ van life packing list.
Writes latest_report.md to the repo — no email needed.
Run manually or via GitHub Actions (see .github/workflows/daily.yml).
"""
import logging
import sys
from datetime import date, datetime

from database import Database
from items import ITEMS, RETAILER_NAMES
from scrapers import ALL_SCRAPERS

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(levelname)-7s  %(name)s — %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger("tracker")

GOOD_DEAL_PCT  = 15.0
GREAT_DEAL_PCT = 25.0
MAX_RESULTS    = 3

PRIORITY_LABEL = {"critical": "🔴", "high": "🟡", "normal": "⚪"}
DEAL_LABEL     = {
    "all_time_low": "🏆 All-time low",
    "great":        "🔥 Great deal (≥25% off avg)",
    "good":         "💚 Good deal (≥15% off avg)",
}


def classify_deal(price, stats, all_time_low):
    if all_time_low and price <= all_time_low:
        return "all_time_low"
    if stats and stats["count"] >= 3:
        disc = (stats["avg"] - price) / stats["avg"] * 100
        if disc >= GREAT_DEAL_PCT:
            return "great"
        if disc >= GOOD_DEAL_PCT:
            return "good"
    return None


def build_markdown(all_prices, deals, run_date, scrape_errors):
    lines = []
    lines.append(f"# 🇳🇿 NZ Van Life — Price Report")
    lines.append(f"*Last updated: {run_date} UTC · "
                 f"Retailers: Decathlon.be · Amazon.de · Wiggle.com · Zalando.be · Bol.com*")
    lines.append("")
    lines.append("🔴 Must-have · 🟡 Recommended · ⚪ Nice to have")
    lines.append("")

    # Scrape errors notice
    if scrape_errors:
        lines.append("> ⚠️ **Blocked retailers today:** " + ", ".join(scrape_errors) +
                     " — cloud IPs are sometimes rate-limited. Results below are from accessible retailers only.")
        lines.append("")

    # Deals section
    if deals:
        lines.append(f"## 🎯 Today's deals ({len(deals)} found)")
        lines.append("")
        lines.append("| Item | Retailer | Price | Deal | Link |")
        lines.append("|------|----------|------:|------|------|")
        for d in deals:
            shop = RETAILER_NAMES.get(d["retailer"], d["retailer"])
            label = DEAL_LABEL.get(d["deal_type"], "")
            name = d["item_meta"]["name"]
            lines.append(f"| {name} | {shop} | €{d['price']:.2f} | {label} | [→]({d['url']}) |")
        lines.append("")
    else:
        lines.append("## 🎯 Today's deals")
        lines.append("*No significant discounts today — prices are near their recent averages.*")
        lines.append("")

    # Full price table grouped by category
    lines.append("## 📋 All tracked items")
    lines.append("")
    lines.append("*Cheapest result per item across all retailers. "
                 "Discount shown vs 30-day rolling average once ≥3 data points exist.*")
    lines.append("")

    current_cat = None
    for item in ITEMS:
        rows = all_prices.get(item["id"], [])
        cat = item["category"]
        if cat != current_cat:
            if current_cat is not None:
                lines.append("")
            lines.append(f"### {cat}")
            lines.append("")
            lines.append("| | Item | Best price | Retailer | vs avg | Link |")
            lines.append("|--|------|----------:|----------|--------|------|")
            current_cat = cat

        pri = PRIORITY_LABEL.get(item["priority"], "⚪")

        if not rows:
            lines.append(f"| {pri} | {item['name']} | *no results* | — | — | — |")
            continue

        best = rows[0]
        shop = RETAILER_NAMES.get(best["retailer"], best["retailer"])
        stats = best.get("stats")
        disc_str = "—"
        if stats and stats["count"] >= 3:
            disc = (stats["avg"] - best["price"]) / stats["avg"] * 100
            sign = "▼" if disc > 0 else "▲"
            disc_str = f"{sign}{abs(disc):.0f}%"

        deal_icon = ""
        if best.get("deal_type") == "all_time_low":
            deal_icon = " 🏆"
        elif best.get("deal_type") == "great":
            deal_icon = " 🔥"
        elif best.get("deal_type") == "good":
            deal_icon = " 💚"

        url = best.get("url", "")
        link = f"[→]({url})" if url else "—"
        lines.append(
            f"| {pri} | {item['name']} | **€{best['price']:.2f}**{deal_icon} "
            f"| {shop} | {disc_str} | {link} |"
        )

    lines.append("")
    lines.append("---")
    lines.append(f"*Generated {run_date} UTC. Prices are indicative — verify before purchasing.*")
    return "\n".join(lines)


def run():
    db = Database("prices.db")
    db.init()

    # ── Scrape ──────────────────────────────────────────────────────────────
    failed_retailers = set()
    ok_retailers = set()
    total = 0
    for item in ITEMS:
        for retailer_key, query in item.get("retailers", {}).items():
            scraper = ALL_SCRAPERS.get(retailer_key)
            if not scraper:
                continue
            log.info("[%s] %s → %r", item["id"], retailer_key, query)
            results = scraper.safe_search(query, max_results=MAX_RESULTS)
            if results:
                ok_retailers.add(retailer_key)
            else:
                failed_retailers.add(retailer_key)
            for r in results:
                db.record_price(
                    item_id=item["id"],
                    retailer=retailer_key,
                    product_name=r["name"],
                    price=r["price"],
                    url=r.get("url", ""),
                    currency=r.get("currency", "EUR"),
                    in_stock=r.get("in_stock", True),
                )
                total += 1

    log.info("Scraped %d prices", total)

    # ── Analyse ─────────────────────────────────────────────────────────────
    all_prices = {}
    deals = []

    for item in ITEMS:
        latest = db.get_latest_prices(item["id"])
        if not latest:
            all_prices[item["id"]] = []
            continue

        enriched = []
        for row in latest:
            stats     = db.get_stats(item["id"], row["retailer"])
            atl       = db.get_all_time_low(item["id"], row["retailer"])
            deal_type = classify_deal(row["price"], stats, atl)
            disc_pct  = 0.0
            if stats and stats["count"] >= 3:
                disc_pct = (stats["avg"] - row["price"]) / stats["avg"] * 100
            enriched.append({**row, "item_meta": item, "stats": stats,
                              "deal_type": deal_type, "discount_pct": disc_pct})
            if deal_type in ("all_time_low", "great", "good"):
                deals.append(enriched[-1])

        best_per_retailer = {}
        for row in enriched:
            k = row["retailer"]
            if k not in best_per_retailer or row["price"] < best_per_retailer[k]["price"]:
                best_per_retailer[k] = row
        all_prices[item["id"]] = sorted(best_per_retailer.values(), key=lambda x: x["price"])

    deals.sort(key=lambda x: (
        -{"all_time_low": 3, "great": 2, "good": 1}.get(x["deal_type"], 0),
        -x["discount_pct"],
    ))

    # ── Write report ─────────────────────────────────────────────────────────
    run_date = datetime.utcnow().strftime("%Y-%m-%d %H:%M")
    # Only flag retailers that returned zero results across ALL their queries
    truly_blocked = failed_retailers - ok_retailers
    scrape_errors = [RETAILER_NAMES.get(k, k) for k in sorted(truly_blocked)]
    md = build_markdown(all_prices, deals, run_date, scrape_errors)
    with open("latest_report.md", "w") as f:
        f.write(md)
    log.info("Report written to latest_report.md (%d deals)", len(deals))
    return 0


if __name__ == "__main__":
    sys.exit(run())
