"""
Configuration module for SofaScore Value Bet Finder.
"""

DEFAULT_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/122.0.0.0 Safari/537.36"
    ),
    "Accept": "application/json",
    "Referer": "https://www.sofascore.com/",
}

REQUEST_TIMEOUT = 10  # Seconds

# Analyzer Thresholds
DEFAULT_MIN_EV = 0.03  # Minimum 3% Expected Value (+3%)
