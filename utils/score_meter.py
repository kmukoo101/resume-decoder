def interpret_score(score: float) -> str:
    """
    Interprets buzzword density score into a human-readable (and sarcastic) message.

    Parameters:
        score (float): The buzzword density percentage.

    Returns:
        str: Interpretation of the score with emoji and attitude.
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
