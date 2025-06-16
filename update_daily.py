
# update_daily.py — runs daily predictions

from data.live_roster import get_all_teams, get_current_roster
from core import predict_hr
import pandas as pd
import datetime

# Mock daily report (expand with real matchups)
def run_daily():
    today = datetime.date.today().strftime('%Y-%m-%d')
    all_teams = get_all_teams()

    reports = []
    for team in all_teams:
        opponent = 'Rays' if team != 'Rays' else 'Yankees'
        roster = get_current_roster(team)
        pitcher = {
            'HR_per9': 1.2,
            'avg_pitch_speed': 94,
            'slider_pct': 25,
            'curve_pct': 12,
            'fastball_pct': 60
        }
        weather = {
            'temp': 80,
            'wind_speed': 10,
            'wind_dir': 1,
            'humidity': 50
        }
        result = predict_hr(roster, pitcher, weather)
        top = result.head(3).copy()
        top['team'] = team
        reports.append(top)

    final = pd.concat(reports)
    final.to_csv(f'daily_hr_report_{today}.csv', index=False)
    print(f"✅ Daily report saved: daily_hr_report_{today}.csv")

if __name__ == "__main__":
    run_daily()
