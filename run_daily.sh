#!/bin/bash
# Daily price tracker runner.
# Activated by launchd — see com.nz-price-tracker.plist for scheduling.
set -euo pipefail

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$REPO"

echo "=== NZ Price Tracker — $(date) ==="

# Activate the virtual environment
source "$REPO/.venv/bin/activate"

# Run the scraper
python tracker.py

# Commit and push results if anything changed
git add latest_report.md prices.db
if ! git diff --staged --quiet; then
    git commit -m "chore: price snapshot $(date +%Y-%m-%d)"
    git push origin main
    echo "✅ Report pushed to GitHub."
else
    echo "ℹ️  Prices unchanged — nothing to commit."
fi
