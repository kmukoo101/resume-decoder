"""
Examples & Try It Page

This Streamlit page allows users to explore sample job descriptions and resumes
to see how the Resume Decoder works without needing to provide their own input.

Features:
- Preloaded examples of job descriptions and resumes
- Auto-fill and decode functionality
- Reuse of buzzword detection and translation logic
"""

import streamlit as st
from app.components import text_utils
import json
import os

# ---------------------
# Load buzzwords
# ---------------------
BUZZWORD_FILE = "utils/buzzwords.json"
if os.path.exists(BUZZWORD_FILE):
    with open(BUZZWORD_FILE, "r") as f:
        buzzword_map = json.load(f)
else:
    st.error("Missing buzzword mapping file. Please check utils/buzzwords.json.")
    st.stop()

# ---------------------
# Preloaded examples
# ---------------------
EXAMPLES = {
    "Software Engineer – Corporate": """We are seeking a results-driven, self-starter to join our fast-paced team. 
        The ideal candidate will wear many hats and deliver impactful solutions while collaborating cross-functionally.""",

    "Marketing Resume Sample": """Dynamic and detail-oriented marketing professional with a proven track record of delivering innovative campaigns that drive engagement and ROI.""",

    "Startup Operations Manager": """Looking for a rockstar generalist who thrives under pressure, embraces chaos, and brings a get-it-done attitude to every challenge.""",

    "Customer Support – Remote": """Seeking a customer-obsessed team player with strong communication skills, empathy, and an unwavering commitment to delivering white-glove support experiences."""
}

# ---------------------
# Page layout
# ---------------------
st.title("Examples & Try It")
st.caption("Curious what this app can do? Try decoding one of our built-in examples.")

# Example selection
selected_example = st.selectbox("Choose an Example to Decode", list(EXAMPLES.keys()))
selected_text = EXAMPLES[selected_example]

# Show the selected example text
st.subheader("Sample Text")
st.code(selected_text, language="markdown")

# Style options
style = st.selectbox("Choose Decoding Style", ["Plain English", "Real Talk", "Gen Z", "Corporate Satire"])

# Decode button
if st.button("Decode This Example"):
    decoded_text, score, highlights = text_utils.decode_text(
        input_text=selected_text,
        buzzword_dict=buzzword_map,
        style=style
    )

    # Output sections
    st.markdown(f"### Buzzword Score: {score}%")
    st.markdown("### Decoded Version")
    st.write(decoded_text)

    st.markdown("### Original with Highlights")
    st.markdown(highlights, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.caption("Want to decode your own resume? Head to the main page.")
