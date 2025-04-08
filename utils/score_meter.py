"""
Buzzword Score Interpretation and Visualization Tools

Translates buzzword scores into human-readable summaries and optional
visual elements like progress bars and a BS meter.
Also supports combined resume quality scoring (BS + ATS + Tone).
"""

import streamlit as st

def interpret_score(score: float) -> str:
    """
    Interprets buzzword density score into a human-readable message.

    Parameters:
        score (float): Buzzword percentage

    Returns:
        str: A witty interpretation of the score
    """
    if score == 0:
        return "🧼 Spotless. Did a human actually write this?"
    elif score < 10:
        return "🟢 Minimal fluff. You might be employable *and* honest."
    elif score < 25:
        return "🟡 A few corporate clichés, but nothing HR can’t ignore."
    elif score < 40:
        return "🟠 You’re speaking fluent LinkedIn. Proceed with caution."
    elif score < 60:
        return "🔴 Corporate bingo is strong with this one."
    elif score < 75:
        return "🚨 You’ve unlocked the Synergy Achievement Badge™️."
    elif score < 90:
        return "💀 This reads like it was written by ChatGPT trapped in 2013."
    else:
        return "🧨 Buzzword singularity detected. Please step away from the resume."

def render_progress_bar(score: float):
    """
    Renders a colored progress bar reflecting the buzzword score.

    Parameters:
        score (float): Buzzword score (0-100)
    """
    st.progress(min(int(score), 100))

def render_bs_meter(score: float):
    """
    Displays a custom BS meter using emoji segments based on score.
    The more BS, the more explosive it gets.

    Parameters:
        score (float): Buzzword percentage
    """
    meter = ""
    if score < 10:
        meter = "🟩🟩⬜⬜⬜⬜"
    elif score < 25:
        meter = "🟨🟨🟩⬜⬜⬜"
    elif score < 40:
        meter = "🟧🟨🟨🟩⬜⬜"
    elif score < 60:
        meter = "🟥🟧🟨🟨🟩⬜"
    elif score < 75:
        meter = "🔥🟥🟧🟨🟨⬜"
    elif score < 90:
        meter = "💣🔥🟥🟧🟨⬜"
    else:
        meter = "☢️💣🔥🟥🟧🟨"

    st.markdown(f"**BS Meter:** `{meter}`")

def calculate_resume_quality(bs_score: float, ats_score: float, tone_data: dict) -> int:
    """
    Generates a rough resume quality score based on BS %, ATS result, and tone diversity.

    Parameters:
        bs_score (float): Buzzword density percentage
        ats_score (float): % of ATS-friendly criteria passed (0-100)
        tone_data (dict): Output of tone analyzer

    Returns:
        int: Quality score between 0 and 100
    """
    tone_diversity = len(tone_data)
    tone_score = min(tone_diversity * 10, 30)  # max 30 pts for tone variety

    # 100 - bs_score means less BS is better
    adjusted_bs = max(0, 100 - bs_score)

    # Equal weights: 35% BS, 35% ATS, 30% tone
    quality = 0.35 * adjusted_bs + 0.35 * ats_score + 0.3 * tone_score
    return round(quality)

def render_quality_badge(score: int):
    """
    Renders a badge that represents overall resume quality.

    Parameters:
        score (int): Quality score (0-100)
    """
    if score >= 85:
        color = "#4caf50"
        label = "Outstanding 🎉"
    elif score >= 70:
        color = "#8bc34a"
        label = "Great ✅"
    elif score >= 50:
        color = "#ffc107"
        label = "Needs Work ⚠️"
    else:
        color = "#f44336"
        label = "Uh-oh ❌"

    st.markdown(f"""
        <div style='background:{color};padding:0.75rem 1.25rem;border-radius:8px;font-weight:bold;color:#fff;display:inline-block;'>
            Resume Quality Score: {score}/100 – {label}
        </div>
    """, unsafe_allow_html=True)
