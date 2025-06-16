
from pybaseball import statcast_batter
from xgboost import XGBClassifier
from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import joblib

def build_training_data(player_ids, days=60):
    end = datetime.today()
    start = end - timedelta(days=days)
    X, y = [], []

    for pid in player_ids:
        try:
            df = statcast_batter(start, end, pid)
            df = df.dropna(subset=['events', 'launch_speed', 'launch_angle'])
        except:
            continue

        for _, row in df.iterrows():
            features = {
                'ExitVelo': row['launch_speed'],
                'LaunchAngle': row['launch_angle'],
                'barrel_rate': 1 if (row['launch_speed'] > 95 and 10 <= row['launch_angle'] <= 25) else 0,
                'hard_hit_pct': 1 if row['launch_speed'] > 95 else 0,
                'HR': 1 if row['events'] == 'home_run' else 0
            }
            X.append({k: features[k] for k in features if k != 'HR'})
            y.append(features['HR'])

    return pd.DataFrame(X), y

if __name__ == "__main__":
    player_ids = [660271, 592450, 664056]
    X, y = build_training_data(player_ids)
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    model = XGBClassifier(n_estimators=100, max_depth=5, learning_rate=0.1, use_label_encoder=False, eval_metric='logloss')
    model.fit(X_scaled, y)

    joblib.dump(model, 'model/xgb_model.pkl')
    joblib.dump(scaler, 'model/xgb_scaler.pkl')
    print("✅ XGBoost model and scaler saved.")
