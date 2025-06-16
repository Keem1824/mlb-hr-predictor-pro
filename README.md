
# ⚾ MLB Home Run Predictor Pro

This app predicts the probability of a player hitting a home run based on:
- Real MLB player stats
- Pitcher matchup profiles
- Weather factors (temperature, wind, humidity)
- Machine learning predictions (Random Forest)

Built with **Python + Streamlit**, ready for deployment on Streamlit Cloud.

---

## 🚀 Features

- ✅ Real player names in lineups (e.g., Yankees, Angels)
- ✅ Adjustable opposing pitcher stats (HR/9, pitch mix)
- ✅ Weather-aware prediction engine
- ✅ Streamlit GUI for fast, interactive use
- ✅ `.env`-ready for secure API key storage

---

## 📦 Setup

1. Clone the repo or unzip this folder:
```bash
pip install -r requirements.txt
cp .env.example .env
streamlit run app.py
```

---

## 🔌 Connect Real Data (Optional)

- `core.py` is modular — replace stubs with:
    - `pybaseball` for stats
    - `mlbstatsapi` or ESPN for lineups
    - `open-meteo` or `weatherapi.com` for weather

---

## 📤 Deployment

- Push to GitHub
- Go to [streamlit.io/cloud](https://streamlit.io/cloud)
- Select `app.py` and deploy

---

## 🔒 .env Example

```
WEATHER_API_KEY=your-weather-api-key-here
```

---

## 🧠 Roadmap

- [ ] Live MLB schedule and lineup auto-load
- [ ] Daily Fantasy value play integration
- [ ] Side-by-side team HR comparisons
- [ ] Natural language AI querying

---

Made by [Keem1834](https://github.com/Keem1834)
