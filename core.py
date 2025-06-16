
import os
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from dotenv import load_dotenv

load_dotenv()

features = [
    'HR_rate', 'ISO', 'wOBA', 'ExitVelo', 'LaunchAngle', 'vs_LHP',
    'ParkFactor_HR', 'Pitcher_HR9', 'recent_form', 'barrel_rate',
    'hard_hit_pct', 'avg_pitch_speed', 'bullpen_HR9',
    'temp', 'wind_speed', 'wind_dir', 'humidity',
    'pitcher_slider_pct', 'pitcher_curve_pct', 'pitcher_fastball_pct'
]

# Initialize model
scaler = StandardScaler()
mock_data = pd.DataFrame([np.random.rand(len(features)) for _ in range(50)], columns=features)
scaler.fit(mock_data)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(scaler.transform(mock_data), np.random.randint(0, 2, 50))

def predict_hr(lineup_df, pitcher_dict, weather_dict):
    df = lineup_df.copy()
    df['ParkFactor_HR'] = 100
    df['Pitcher_HR9'] = pitcher_dict['HR_per9']
    df['recent_form'] = df['HR_rate'] * 1.1
    df['avg_pitch_speed'] = pitcher_dict['avg_pitch_speed']
    df['bullpen_HR9'] = pitcher_dict['HR_per9'] + 0.2
    df['temp'] = weather_dict['temp']
    df['wind_speed'] = weather_dict['wind_speed']
    df['wind_dir'] = weather_dict['wind_dir']
    df['humidity'] = weather_dict['humidity']
    df['pitcher_slider_pct'] = pitcher_dict['slider_pct']
    df['pitcher_curve_pct'] = pitcher_dict['curve_pct']
    df['pitcher_fastball_pct'] = pitcher_dict['fastball_pct']
    X = scaler.transform(df[features])
    df['HR_probability'] = model.predict_proba(X)[:, 1]
    return df[['player', 'HR_probability']].sort_values(by='HR_probability', ascending=False)
