

### 8. `main.py`

```python
"""
Main execution script for SofaScore Value Bet Finder.
"""

import sys
from tabulate import tabulate

from config.settings import DEFAULT_MIN_EV
from src.analyzer import ValueBetAnalyzer
from src.scraper import SofaScoreScraper


def main():
    print("=" * 80)
    print("      SOFASCORE VALUE BET FINDER - HIGH PRECISION TIPS")
    print("=" * 80)

    try:
        scraper = SofaScoreScraper()
        print("\n[+] Fetching live match odds and SofaScore historical win rates...")
        matches = scraper.fetch_match_data()

        if not matches:
            print("[-] No match data returned. Exiting.")
            sys.exit(0)

        analyzer = ValueBetAnalyzer(min_ev=DEFAULT_MIN_EV)
        print(f"[+] Analyzing {len(matches)} matches (Minimum EV filter: +{DEFAULT_MIN_EV * 100:.1f}%)...")
        value_tips_df = analyzer.analyze_matches(matches)

        print("\n" + "=" * 80)
        print("                        NAGY PONTOSSÁGÚ TIPPEK (VALUE BETS)")
        print("=" * 80)

        if value_tips_df.empty:
            print("[-] Nem található pozitív várható értékű (Value Bet) tipp az adott feltételekkel.")
        else:
            table_output = tabulate(
                value_tips_df,
                headers="keys",
                tablefmt="grid",
                showindex=False
            )
            print(table_output)
            print(f"\n[✓] Összesen {len(value_tips_df)} pozitív EV-s tipp azonosítva.")

    except Exception as e:
        print(f"[!] Hiba történt a főprogram futtatása során: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
