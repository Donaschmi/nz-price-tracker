import os

DB_PATH = os.getenv("DB_PATH", "prices.db")

EMAIL_FROM     = os.environ["EMAIL_FROM"]
EMAIL_TO       = os.environ["EMAIL_TO"]
SMTP_HOST      = os.getenv("SMTP_HOST", "smtp.gmail.com")
SMTP_PORT      = int(os.getenv("SMTP_PORT", "587"))
SMTP_PASSWORD  = os.environ["SMTP_PASSWORD"]

# Alert when today's price is at least this % below the 30-day average
GOOD_DEAL_PCT  = float(os.getenv("GOOD_DEAL_PCT",  "15"))  # ≥15% off → Good deal
GREAT_DEAL_PCT = float(os.getenv("GREAT_DEAL_PCT", "25"))  # ≥25% off → Great deal

# Max results fetched per item per retailer
MAX_RESULTS_PER_RETAILER = int(os.getenv("MAX_RESULTS_PER_RETAILER", "3"))

# Seconds to wait between requests to the same retailer
RATE_LIMIT_SECONDS = float(os.getenv("RATE_LIMIT_SECONDS", "2.5"))
