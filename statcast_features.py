
# statcast_features.py
# Real feature engineering from pybaseball Statcast

from pybaseball import statcast_batter
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def get_batter_features(player_id, start=None, end=None):
    if not start:
        end = datetime.today()
        start = end - timedelta(days=30)
    if isinstance(start, datetime):
        start = start.strftime('%Y-%m-%d')
    if isinstance(end, datetime):
        end = end.strftime('%Y-%m-%d')

    try:
        data = statcast_batter(start, end, player_id)
    except:
        return {}

    if data.empty:
        return {}

    data = data.dropna(subset=['events', 'launch_speed', 'launch_angle'])

    total_pa = len(data)
    hr_rate = (data['events'] == 'home_run').sum() / total_pa if total_pa else 0
    iso = data['iso'].mean() if 'iso' in data else 0
    woba = data['woba'].mean() if 'woba' in data else 0
    ev = data['launch_speed'].mean()
    la = data['launch_angle'].mean()
    barrel = ((data['launch_speed'] > 95) & (data['launch_angle'].between(10, 25))).sum() / total_pa
    hard_hit = (data['launch_speed'] > 95).sum() / total_pa

    return {
        'HR_rate': hr_rate,
        'ISO': iso,
        'wOBA': woba,
        'ExitVelo': ev,
        'LaunchAngle': la,
        'barrel_rate': barrel,
        'hard_hit_pct': hard_hit * 100
    }
