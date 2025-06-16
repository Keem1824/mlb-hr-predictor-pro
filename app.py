
import streamlit as st
import pandas as pd
import numpy as np
from core import predict_hr
from data.live_roster import get_all_teams, get_current_roster
from data.insights import explain_player
from data.logger import log_event
from data.ask_gpt import ask_gpt
from data.dfs_optimizer import optimize_dfs
import datetime

st.set_page_config(page_title="MLB HR Predictor Pro", layout="wide")
st.title("💣 MLB Home Run Predictor Pro")

with st.sidebar:
    st.markdown("""### 📋 How to Use
1. Select a team
2. We pull the latest roster (or lineup)
3. Adjust pitcher and weather
4. Click **Run Prediction**
5. Generate GPT insight, DFS values, or reports!
    """)

teams = get_all_teams()
team = st.selectbox("Select Team", teams)
opponent = st.selectbox("Select Opponent", [t for t in teams if t != team])
lineup_data = get_current_roster(team)
st.subheader(f"{team} Lineup (Auto-Populated)")
st.dataframe(lineup_data)

with st.expander("⚙️ Pitcher & Weather Context"):
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
    result['Insights'] = result.apply(explain_player, axis=1)
    st.subheader(f"Top HR Threats for {team} vs {opponent}")
    st.dataframe(result.head(5))

    st.markdown("### 💬 Ask the Predictor (GPT-Ready)")
    question = st.text_input("Ask about HR threats or players today")
    if st.button("Get AI Insight"):
        gpt_context = result[['player', 'HR_probability', 'Insights']].to_string(index=False)
        st.info(ask_gpt(question, gpt_context))

    st.markdown("### 💸 DFS Value Rankings")
    sample_salaries = {row['player']: np.random.randint(3000, 6000) for _, row in result.iterrows()}
    dfs_df = optimize_dfs(result, sample_salaries)
    st.dataframe(dfs_df)

    st.markdown("### 📋 Generate Summary Report")
    summary = result.head(5).apply(lambda row: f"{row['player']}: {row['Insights']}", axis=1)
    report_text = f"🧠 Top HR Threats for {team} on {datetime.date.today()}\n" + "\n".join(summary)
    st.text_area("Copy your report below", report_text, height=180)

    log_event(team, opponent, len(result))
