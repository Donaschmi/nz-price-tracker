import smtplib
import logging
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import date

log = logging.getLogger(__name__)

PRIORITY_EMOJI = {"critical": "🔴", "high": "🟡", "normal": "⚪"}
DEAL_BADGE = {
    "all_time_low": ("🏆 All-time low", "#1a7f37"),
    "great":        ("🔥 Great deal",   "#d1242f"),
    "good":         ("💚 Good deal",    "#2da44e"),
    "watch":        ("👀 Worth watching", "#9a6700"),
}


def _badge(deal_type: str) -> str:
    label, color = DEAL_BADGE[deal_type]
    return (
        f'<span style="background:{color};color:#fff;border-radius:4px;'
        f'padding:2px 8px;font-size:11px;font-weight:600">{label}</span>'
    )


def _trend_bar(current: float, avg: float, mn: float, mx: float) -> str:
    if mx == mn:
        return ""
    pct = max(0, min(100, int((current - mn) / (mx - mn) * 100)))
    color = "#2da44e" if pct < 30 else "#9a6700" if pct < 60 else "#d1242f"
    return (
        f'<div style="background:#e8e8e8;border-radius:4px;height:6px;width:120px;display:inline-block;vertical-align:middle">'
        f'<div style="background:{color};width:{pct}%;height:100%;border-radius:4px"></div></div>'
        f'<span style="font-size:10px;color:#666;margin-left:4px">{pct}% of range</span>'
    )


def build_html_report(
    deals: list[dict],
    all_prices: dict,   # item_id → list of price rows with deal metadata
    run_date: str,
) -> str:
    def price_row(row: dict) -> str:
        deal_html = ""
        if row.get("deal_type"):
            deal_html = _badge(row["deal_type"]) + "&nbsp;"

        stats = row.get("stats")
        trend_html = ""
        if stats:
            disc = row.get("discount_pct", 0)
            disc_html = (
                f'<span style="color:#2da44e;font-weight:600">▼ {disc:.0f}% off avg</span>'
                if disc > 0 else ""
            )
            trend_html = (
                f'<div style="font-size:11px;color:#888;margin-top:2px">'
                f'avg&nbsp;€{stats["avg"]:.2f}&nbsp;·&nbsp;'
                f'30-day&nbsp;low&nbsp;€{stats["min"]:.2f}&nbsp;·&nbsp;'
                f'{disc_html}</div>'
            )

        return (
            f'<tr>'
            f'<td style="padding:8px 12px;border-bottom:1px solid #f0f0f0">'
            f'<a href="{row["url"]}" style="color:#0969da;text-decoration:none">{row["product_name"][:80]}</a>'
            f'</td>'
            f'<td style="padding:8px 12px;border-bottom:1px solid #f0f0f0;white-space:nowrap">'
            f'{deal_html}<strong>€{row["price"]:.2f}</strong>'
            f'{trend_html}'
            f'</td>'
            f'</tr>'
        )

    # ── Deals section ──────────────────────────────────────────────────────
    deals_html = ""
    if deals:
        deals_rows = "".join(price_row(d) for d in deals)
        deals_html = f"""
        <h2 style="color:#2D4A35;font-size:18px;margin:28px 0 8px">
            🎯 Today's best deals ({len(deals)} found)
        </h2>
        <p style="color:#666;font-size:13px;margin-bottom:12px">
            Prices at least 15% below the 30-day average, or a new all-time low.
        </p>
        <table style="width:100%;border-collapse:collapse;background:#fff;border-radius:8px;overflow:hidden;box-shadow:0 1px 4px rgba(0,0,0,.08)">
            <thead>
                <tr style="background:#2D4A35;color:#fff">
                    <th style="padding:10px 12px;text-align:left;font-weight:500">Product</th>
                    <th style="padding:10px 12px;text-align:left;font-weight:500">Price</th>
                </tr>
            </thead>
            <tbody>{deals_rows}</tbody>
        </table>
        """
    else:
        deals_html = """
        <div style="background:#f6f8fa;border-radius:8px;padding:20px;margin:20px 0;color:#666;font-size:14px">
            No significant deals today. Keep watching — prices fluctuate daily.
        </div>
        """

    # ── Full price table, grouped by category ──────────────────────────────
    categories_html = ""
    current_cat = None
    for item_id, rows in all_prices.items():
        if not rows:
            continue
        item_meta = rows[0].get("item_meta", {})
        cat = item_meta.get("category", "Other")
        if cat != current_cat:
            if current_cat is not None:
                categories_html += "</tbody></table></div>"
            categories_html += f"""
            <div style="margin-top:28px">
            <h3 style="color:#2D4A35;font-size:15px;margin-bottom:8px">{cat}</h3>
            <table style="width:100%;border-collapse:collapse;background:#fff;border-radius:8px;overflow:hidden;box-shadow:0 1px 4px rgba(0,0,0,.08)">
            <thead><tr style="background:#5C7A4E;color:#fff">
                <th style="padding:8px 12px;text-align:left;font-weight:500;font-size:12px">Item</th>
                <th style="padding:8px 12px;text-align:left;font-weight:500;font-size:12px">Shop</th>
                <th style="padding:8px 12px;text-align:left;font-weight:500;font-size:12px">Price</th>
                <th style="padding:8px 12px;text-align:left;font-weight:500;font-size:12px">vs 30-day avg</th>
            </tr></thead><tbody>
            """
            current_cat = cat

        priority_dot = PRIORITY_EMOJI.get(item_meta.get("priority", "normal"), "⚪")
        for i, row in enumerate(rows):
            item_name = f'{priority_dot} {item_meta["name"]}' if i == 0 else ""
            stats = row.get("stats")
            vs_avg = ""
            if stats and stats["count"] >= 3:
                disc = row.get("discount_pct", 0)
                color = "#2da44e" if disc >= 15 else "#d1242f" if disc < -5 else "#666"
                sign = "▼" if disc > 0 else "▲" if disc < 0 else ""
                vs_avg = f'<span style="color:{color};font-size:12px">{sign}{abs(disc):.0f}%</span>'
            elif stats:
                vs_avg = '<span style="color:#aaa;font-size:11px">tracking…</span>'
            else:
                vs_avg = '<span style="color:#aaa;font-size:11px">new</span>'

            from items import RETAILER_NAMES
            shop = RETAILER_NAMES.get(row["retailer"], row["retailer"])
            deal_badge = f' {_badge(row["deal_type"])}' if row.get("deal_type") else ""

            categories_html += (
                f'<tr>'
                f'<td style="padding:7px 12px;border-bottom:1px solid #f4f4f4;font-size:13px">{item_name}</td>'
                f'<td style="padding:7px 12px;border-bottom:1px solid #f4f4f4;font-size:12px;color:#555">{shop}</td>'
                f'<td style="padding:7px 12px;border-bottom:1px solid #f4f4f4;font-size:13px">'
                f'<a href="{row["url"]}" style="color:#0969da;text-decoration:none">€{row["price"]:.2f}</a>'
                f'{deal_badge}</td>'
                f'<td style="padding:7px 12px;border-bottom:1px solid #f4f4f4">{vs_avg}</td>'
                f'</tr>'
            )

    if current_cat:
        categories_html += "</tbody></table></div>"

    return f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>NZ Packing — Price Report {run_date}</title>
</head>
<body style="font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;background:#f6f8fa;margin:0;padding:20px">
<div style="max-width:720px;margin:0 auto">

  <!-- Header -->
  <div style="background:#2D4A35;color:#F5F0E8;border-radius:12px;padding:28px 32px;margin-bottom:20px">
    <div style="font-size:11px;letter-spacing:.15em;text-transform:uppercase;color:#C8A96E;margin-bottom:6px">
      🇳🇿 New Zealand · September 2026 · Van Life
    </div>
    <h1 style="margin:0;font-size:24px;font-weight:700">Daily Price Report</h1>
    <p style="margin:8px 0 0;color:rgba(245,240,232,.65);font-size:13px">{run_date} · Belgium shipping</p>
  </div>

  <!-- Priority legend -->
  <div style="background:#fff;border-radius:8px;padding:14px 20px;margin-bottom:20px;font-size:12px;color:#555;display:flex;gap:16px">
    <span>🔴 Must-have</span><span>🟡 Recommended</span><span>⚪ Nice to have</span>
    <span style="margin-left:auto;color:#888">Retailers: Decathlon.be · Amazon.de · Wiggle.com · Zalando.be · Bol.com</span>
  </div>

  {deals_html}

  <!-- Full table -->
  <h2 style="color:#2D4A35;font-size:18px;margin:32px 0 4px">📋 All tracked items</h2>
  <p style="color:#666;font-size:13px;margin-bottom:4px">
    Showing cheapest result per item across all retailers.
    Discount shown vs 30-day rolling average once ≥3 data points are available.
  </p>
  {categories_html}

  <!-- Footer -->
  <div style="margin-top:32px;padding-top:16px;border-top:1px solid #e0e0e0;font-size:11px;color:#aaa;text-align:center">
    Prices scraped daily from Decathlon.be, Amazon.de, Wiggle.com, Zalando.be, Bol.com.<br>
    Prices are indicative — verify before purchasing. Shipping to Belgium may add costs.
  </div>

</div>
</body></html>"""


def send_email(
    *,
    html_body: str,
    subject: str,
    email_from: str,
    email_to: str,
    smtp_host: str,
    smtp_port: int,
    smtp_password: str,
):
    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"]    = email_from
    msg["To"]      = email_to
    msg.attach(MIMEText(html_body, "html"))

    with smtplib.SMTP(smtp_host, smtp_port) as server:
        server.ehlo()
        server.starttls()
        server.login(email_from, smtp_password)
        server.sendmail(email_from, email_to, msg.as_string())

    log.info("Email sent to %s", email_to)
