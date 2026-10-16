"""
Mathematical analysis module for EV calculation and Value Bet detection.
"""

import logging
from typing import Any, Dict, List
import pandas as pd

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)


class ValueBetAnalyzer:
    """
    Calculates implied probabilities, Expected Value (EV), and identifies positive edge opportunities.
    """

    def __init__(self, min_ev: float = 0.03):
        """
        Args:
            min_ev (float): Minimum Expected Value threshold (e.g. 0.03 = +3% EV).
        """
        self.min_ev = min_ev

    @staticmethod
    def calculate_implied_probability(odds: float) -> float:
        """Calculates implied probability from decimal odds (1 / Odds)."""
        if odds <= 1.0:
            return 0.0
        return 1.0 / odds

    @staticmethod
    def calculate_expected_value(win_probability: float, odds: float) -> float:
        """Calculates Expected Value (EV = (Win Probability * Odds) - 1)."""
        if odds <= 1.0 or win_probability < 0.0:
            return -1.0
        return (win_probability * odds) - 1.0

    def analyze_matches(self, matches: List[Dict[str, Any]]) -> pd.DataFrame:
        """
        Processes match records and returns positive EV betting opportunities.

        Args:
            matches (List[Dict[str, Any]]): Match data extracted by scraper.

        Returns:
            pd.DataFrame: Formatted DataFrame sorted by EV descending.
        """
        results = []

        for match in matches:
            try:
                match_id = match.get("id", "N/A")
                home_team = match.get("home_team", "Unknown")
                away_team = match.get("away_team", "Unknown")
                league = match.get("league", "Unknown")

                selections = [
                    ("Home Win", match.get("home_odds", 0.0), match.get("sofascore_historical", {}).get("home_win_rate", 0.0)),
                    ("Draw", match.get("draw_odds", 0.0), match.get("sofascore_historical", {}).get("draw_rate", 0.0)),
                    ("Away Win", match.get("away_odds", 0.0), match.get("sofascore_historical", {}).get("away_win_rate", 0.0)),
                ]

                for sel_name, odds, hist_prob in selections:
                    if odds <= 1.0 or hist_prob <= 0.0:
                        continue

                    implied_prob = self.calculate_implied_probability(odds)
                    ev = self.calculate_expected_value(hist_prob, odds)
                    edge = (hist_prob - implied_prob) * 100

                    if ev >= self.min_ev:
                        results.append({
                            "Match ID": match_id,
                            "League": league,
                            "Match": f"{home_team} vs {away_team}",
                            "Selection": sel_name,
                            "Odds": odds,
                            "Implied Prob (%)": round(implied_prob * 100, 2),
                            "SofaScore Hist Prob (%)": round(hist_prob * 100, 2),
                            "Edge (%)": round(edge, 2),
                            "EV (%)": round(ev * 100, 2),
                        })

            except Exception as err:
                logger.error(f"Error evaluating match {match.get('id', 'N/A')}: {err}")

        df = pd.DataFrame(results)
        if not df.empty:
            df = df.sort_values(by="EV (%)", ascending=False).reset_index(drop=True)

        return df
