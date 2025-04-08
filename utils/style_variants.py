def apply_style(base_text: str, style: str, original: str) -> str:
    """
    Transforms a buzzword's decoded meaning into a stylized rewrite based on selected tone.

    Parameters:
        base_text (str): The plain translation of the buzzword.
        style (str): The selected tone or rewrite style.
        original (str): The original buzzword or phrase.

    Returns:
        str: A rewritten version styled with tone, humor, or honesty.
    """
    if style == "Plain English":
        # Clean and informative, no frills
        return base_text

    elif style == "Real Talk":
        # Casual and brutally honest
        return f"⚠️ '{original}' really means: {base_text}"

    elif style == "Gen Z":
        # Slangified, ironic, and emoji-laden
        return f"{original} 🤡 ({base_text.lower()} but like... ✨corporate✨)"

    elif style == "Corporate Satire":
        # Dry sarcasm, mocking tone
        return f"{original}™️ — now featuring: {base_text}"

    elif style == "Spiritual":
        # Woo-woo energy decoding
        return f"🌕 {original} (rooted in illusion — true meaning: {base_text}) ✨"

    elif style == "Haiku":
        # Haiku format (fun easter egg mode)
        syllables = base_text.split()  # Just split for now, not true haiku logic
        return f"{original}:\n{' '.join(syllables[:5])}\n{' '.join(syllables[5:12])}\n{' '.join(syllables[12:])}"

    elif style == "Passive-Aggressive":
        # Terse and pointed — almost HR-like
        return f"{original} (We *trust* you understand this means: {base_text})"

    else:
        # Fallback to plain
        return base_text
