"""
Resume Decoder Page

This Streamlit page allows users to paste job descriptions or resume content,
select a translation style, and receive a decoded version of the content
with plain language or humorous interpretation.

Features:
- Buzzword detection and scoring
- Multiple tone options for translation
- Highlighting of corporate fluff
"""

import streamlit as st
from app.components import text_utils
import json
import os

# ------------------------
# Load buzzword mapping
# ------------------------
BUZZWORD_FILE = "utils/buzzwords.json"

if os.path.exists(BUZZWORD_FILE):
    with open(BUZZWORD_FILE, "r") as f:
        buzzword_map = json.load(f)
else:
    st.error("Missing buzzword mapping file. Please check utils/buzzwords.json.")
    st.stop()

# ------------------------
# Page Layout and Header
# ------------------------

st.title("🧾 Resume Decoder")
st.caption("Translate job descriptions and resumes into real talk. No more corporate fluff.")

st.markdown("Paste in your resume or job post below, and we'll decode it for clarity, honesty, or humor.")

# ------------------------
# Text Input and Style Selection
# ------------------------

st.subheader("🔍 Input Text")
user_input = st.text_area(
    label="Enter a resume, job description, or bullet point list",
    height=300,
    placeholder="Example: 'We're looking for a self-motivated, detail-oriented team player...'"
)

style = st.selectbox(
    "Choose your decoding style",
    ["Plain English", "Real Talk", "Gen Z", "Corporate Satire"]
)

# ------------------------
# Decode Button Logic
# ------------------------

if st.button("🔥 Decode It"):
    if not user_input.strip():
        st.warning("Please enter text to decode.")
    else:
        # Call the core decoding function
        decoded_text, score, highlights = text_utils.decode_text(
            input_text=user_input,
            buzzword_dict=buzzword_map,
            style=style
        )

        # Display results
        st.markdown(f"### 🧠 Buzzword Score: {score}%")
        st.markdown("### 🪞 Decoded Version")
        st.write(decoded_text)

        st.markdown("### ✏️ Original with Highlights")
        st.markdown(highlights, unsafe_allow_html=True)

# Optional tip
st.markdown("---")
st.caption("Tip: Use 'Gen Z' or 'Corporate Satire' mode for a laugh. Try pasting your own resume!")

