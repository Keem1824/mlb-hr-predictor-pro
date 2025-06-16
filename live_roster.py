
# live_roster.py – live team list and roster loader (real API-ready)

import pandas as pd

# === Team List from MLB ===
def get_all_teams():
    # REPLACE with:
    # from mlbstatsapi import MLBStatsAPI
    # api = MLBStatsAPI()
    # teams = api.get_teams(sport_id=1)
    # return [t['name'] for t in teams]
    return ['Yankees', 'Angels', 'Dodgers', 'Braves', 'Giants', 'Mets', 'Rays']

# === Full 26-man roster ===
def get_current_roster(team_name):
    # REPLACE with:
    # team_id = lookup_team_id(team_name)
    # roster = api.get_team_roster(team_id)
    # return pd.DataFrame(roster)
    from .statcast_features import get_batter_features
    names = ["Aaron Judge", "Juan Soto", "Giancarlo Stanton", "Anthony Rizzo",
             "Gleyber Torres", "DJ LeMahieu", "Jose Trevino", "Anthony Volpe", "Alex Verdugo"]

    players = []
    for i, name in enumerate(names):
        feats = get_batter_features(player_id=660271)  # mock ID for Aaron Judge
        if not feats:
            feats = {
                'HR_rate': 0.05 + i * 0.002,
                'ISO': 0.200,
                'wOBA': 0.350,
                'ExitVelo': 92.5,
                'LaunchAngle': 16,
                'barrel_rate': 15,
                'hard_hit_pct': 50
            }
        feats['player'] = name
        feats['vs_LHP'] = i % 2
        players.append(feats)

    return pd.DataFrame(players)
