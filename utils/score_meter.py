"""
Buzzword Score Interpretation and Visualization Tools

Translates buzzword scores into human-readable summaries and optional
visual elements like progress bars and a BS meter.
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
