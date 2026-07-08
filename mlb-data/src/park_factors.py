"""Static park factors (runs / HR), index 100 = league-neutral environment.

Orientační hodnoty odvozené z veřejných tříletých park factors
(Baseball Savant / FanGraphs, stav ~2024). Před tréninkem modelu je vhodné
je zaktualizovat z https://baseballsavant.mlb.com/leaderboard/statcast-park-factors
— stačí přepsat čísla tady a spustit `python -m src.backfill --only-reference`.

Keyed by venue *name* (venue_id is resolved from the MLB API during backfill;
names below match the API venue names). Unknown venues fall back to 100/100.
"""

PARK_FACTORS: dict[str, tuple[float, float]] = {
    # venue name: (park_factor_runs, park_factor_hr)
    "Coors Field": (112, 110),                 # Rockies
    "Fenway Park": (107, 96),                  # Red Sox
    "Great American Ball Park": (103, 116),    # Reds
    "Kauffman Stadium": (103, 90),             # Royals
    "Chase Field": (103, 99),                  # D-backs
    "Nationals Park": (102, 103),              # Nationals
    "Truist Park": (101, 103),                 # Braves
    "Globe Life Field": (101, 100),            # Rangers
    "Wrigley Field": (100, 99),                # Cubs
    "Citizens Bank Park": (100, 110),          # Phillies
    "Angel Stadium": (100, 104),               # Angels
    "PNC Park": (100, 91),                     # Pirates
    "Target Field": (99, 100),                 # Twins
    "Rogers Centre": (99, 103),                # Blue Jays
    "Yankee Stadium": (99, 110),               # Yankees
    "Minute Maid Park": (99, 103),             # Astros (od 2025 "Daikin Park")
    "Daikin Park": (99, 103),                  # Astros
    "Oriole Park at Camden Yards": (98, 104),  # Orioles
    "Dodger Stadium": (98, 107),               # Dodgers
    "Guaranteed Rate Field": (98, 106),        # White Sox (od 2025 "Rate Field")
    "Rate Field": (98, 106),                   # White Sox
    "Busch Stadium": (98, 92),                 # Cardinals
    "Comerica Park": (97, 95),                 # Tigers
    "Progressive Field": (97, 97),             # Guardians
    "American Family Field": (97, 106),        # Brewers
    "Miller Park": (97, 106),                  # Brewers (název do 2020)
    "Citi Field": (96, 101),                   # Mets
    "loanDepot park": (96, 92),                # Marlins
    "Marlins Park": (96, 92),                  # Marlins (název do 2020)
    "Oracle Park": (96, 88),                   # Giants
    "Petco Park": (96, 100),                   # Padres
    "Tropicana Field": (96, 96),               # Rays (do 2024)
    "George M. Steinbrenner Field": (102, 108),  # Rays 2025 (provizorní)
    "Oakland Coliseum": (95, 89),              # A's (do 2024)
    "Sutter Health Park": (101, 102),          # A's 2025 (provizorní)
    "T-Mobile Park": (94, 99),                 # Mariners
}

DEFAULT_PARK_FACTOR = (100.0, 100.0)


def lookup(venue_name: str | None) -> tuple[float, float]:
    if not venue_name:
        return DEFAULT_PARK_FACTOR
    return PARK_FACTORS.get(venue_name, DEFAULT_PARK_FACTOR)
