
# insights.py — simple rules-based LLM-style text explainer

def explain_player(row):
    lines = []
    if row['HR_probability'] > 0.25:
        lines.append("🚀 High home run probability!")
    if row['barrel_rate'] > 12:
        lines.append("💣 Elite barrel rate.")
    if row['hard_hit_pct'] > 50:
        lines.append("🔥 Crushing the ball lately.")
    if row['LaunchAngle'] > 15:
        lines.append("📈 Ideal launch angle.")
    if not lines:
        return "Solid contributor but not a top HR threat today."
    return " ".join(lines)
