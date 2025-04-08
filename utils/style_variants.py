def apply_style(base_text: str, style: str, original: str) -> str:
    if style == "Plain English":
        return base_text
    elif style == "Real Talk":
        return f"[Translation: {base_text}]"
    elif style == "Gen Z":
        return f"{original} (aka: {base_text}, fr)"
    elif style == "Corporate Satire":
        return f"{original}™️ — {base_text}"
    else:
        return base_text
