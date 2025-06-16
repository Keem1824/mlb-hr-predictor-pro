
import streamlit as st
import pandas as pd
from core import predict_hr
from data.live_roster import get_all_teams, get_current_roster
import numpy as np

st.set_page_config(page_title="MLB HR Predictor Pro", layout="wide")
st.title("⚾ MLB Home Run Predictor — Live Roster Mode")

teams = get_all_teams()
team = st.selectbox("Select Team", teams)
opponent = st.selectbox("Select Opponent", [t for t in teams if t != team])

# Auto-populated real roster
lineup_data = get_current_roster(team)
st.subheader(f"{team} Lineup (Auto-Populated)")
st.dataframe(lineup_data)

# Pitcher inputs
with st.expander("Pitcher & Weather Context"):
    HR_per9 = st.slider("HR per 9 innings", 0.5, 2.0, 1.3)
    avg_velo = st.slider("Fastball Velocity", 88.0, 100.0, 94.0)
    slider_pct = st.slider("Slider %", 0, 50, 25)
    curve_pct = st.slider("Curve %", 0, 40, 12)
    fb_pct = st.slider("Fastball %", 20, 80, 60)

    weather = {
        'temp': st.slider("Temp °F", 50, 100, 78),
        'wind_speed': st.slider("Wind mph", 0, 20, 10),
        'wind_dir': st.selectbox("Wind Direction", [-1, 0, 1], format_func=lambda x: {1: 'Out', 0: 'Cross', -1: 'In'}[x]),
        'humidity': st.slider("Humidity %", 20, 100, 55)
    }

pitcher = {
    'HR_per9': HR_per9,
    'avg_pitch_speed': avg_velo,
    'slider_pct': slider_pct,
    'curve_pct': curve_pct,
    'fastball_pct': fb_pct
}

if st.button("Run Prediction"):
    result = predict_hr(lineup_data, pitcher, weather)
    st.subheader(f"Top HR Threats for {team} vs {opponent}")
    st.dataframe(result.head(5))
