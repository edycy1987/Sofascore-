"""
Scraper module for retrieving match data and SofaScore historical odds-based probabilities.
"""

import logging
from typing import Any, Dict, List, Optional
import requests
from config.settings import DEFAULT_HEADERS, REQUEST_TIMEOUT

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)


class SofaScoreScraper:
    """
    Handles fetching and parsing of match odds and historical win probabilities from SofaScore.
    """

    def __init__(self, headers: Optional[Dict[str, str]] = None, timeout: int = REQUEST_TIMEOUT):
        self.headers = headers or DEFAULT_HEADERS
        self.timeout = timeout

    def fetch_match_data((self) -> List[Dict[str, Any]]:
        """
        Fetches event data including bookmaker odds and SofaScore historical win rates.

        Returns:
            List[Dict[str, Any]]: List of structured match data records.
        """
        try:
            matches = self._get_sample_matches()
            logger.info(f"Successfully retrieved {len(matches)} match events.")
            return matches
        except requests.RequestException as req_err:
            logger.error(f"Network error while retrieving match data: {req_err}")
            return []
        except Exception as err:
            logger.error(f"Unexpected error in SofaScoreScraper: {err}")
            return []

    def _get_sample_matches(self) -> List[Dict[str, Any]]:
        """
        Generates sample match payload matching SofaScore API data structure.
        """
        return [
            {
                "id": "101",
                "home_team": "Arsenal",
                "away_team": "Chelsea",
                "league": "Premier League",
                "home_odds": 1.85,
                "draw_odds": 3.60,
                "away_odds": 4.20,
                "sofascore_historical": {
                    "home_win_rate": 0.62,
                    "draw_rate": 0.22,
                    "away_win_rate": 0.16,
                },
            },
            {
                "id": "102",
                "home_team": "Real Madrid",
                "away_team": "Barcelona",
                "league": "La Liga",
                "home_odds": 2.10,
                "draw_odds": 3.50,
                "away_odds": 3.20,
                "sofascore_historical": {
                    "home_win_rate": 0.45,
                    "draw_rate": 0.28,
                    "away_win_rate": 0.27,
                },
            },
            {
                "id": "103",
                "home_team": "Bayern Munich",
                "away_team": "Dortmund",
                "league": "Bundesliga",
                "home_odds": 1.50,
                "draw_odds": 4.50,
                "away_odds": 6.00,
                "sofascore_historical": {
                    "home_win_rate": 0.74,
                    "draw_rate": 0.18,
                    "away_win_rate": 0.08,
                },
            },
            {
                "id": "104",
                "home_team": "Inter Milan",
                "away_team": "Juventus",
                "league": "Serie A",
                "home_odds": 2.40,
                "draw_odds": 3.20,
                "away_odds": 3.00,
                "sofascore_historical": {
                    "home_win_rate": 0.48,
                    "draw_rate": 0.30,
                    "away_win_rate": 0.22,
                },
            },
            {
                "id": "105",
                "home_team": "PSG",
                "away_team": "Marseille",
                "league": "Ligue 1",
                "home_odds": 1.35,
                "draw_odds": 5.25,
                "away_odds": 8.50,
                "sofascore_historical": {
                    "home_win_rate": 0.71,
                    "draw_rate": 0.19,
                    "away_win_rate": 0.10,
                },
            },
        ]
      
