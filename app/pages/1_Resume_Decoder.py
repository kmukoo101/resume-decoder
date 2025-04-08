"""
Resume Decoder Page

This Streamlit page allows users to paste job descriptions or resume content,
select a translation style, and receive a decoded version of the content
with plain language or humorous interpretation.

Features:
- Buzzword detection and scoring
- Multiple tone options for translation
- Highlighting of corporate fluff
- Export and copy features for decoded output
- Custom buzzword injection
- Style descriptions for clarity
- Side-by-side view toggle
- Honest job title generator
"""

import streamlit as st
from app.components import text_utils
from utils.funny_titles import generate_title
from utils.style_metadata import STYLE_DESCRIPTIONS
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
    options=list(STYLE_DESCRIPTIONS.keys()),
    format_func=lambda x: f"{x} – {STYLE_DESCRIPTIONS[x]}"
)

# Optional: Add custom buzzword
st.markdown("Optional: Add a custom buzzword")
new_word = st.text_input("Buzzword")
new_def = st.text_input("Its real meaning")

if new_word and new_def:
    buzzword_map[new_word.lower()] = new_def

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

        layout = st.radio("Choose Layout", ["Stacked", "Side-by-Side"], horizontal=True)

        st.markdown(f"### 🧠 Buzzword Score: {score}%")

        if layout == "Side-by-Side":
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("### 🪞 Decoded")
                st.write(decoded_text)
            with col2:
                st.markdown("### ✏️ Original with Highlights")
                st.markdown(highlights, unsafe_allow_html=True)
        else:
            st.markdown("### 🪞 Decoded Version")
            st.write(decoded_text)
            st.markdown("### ✏️ Original with Highlights")
            st.markdown(highlights, unsafe_allow_html=True)

        # Honest title generator
        st.markdown(f"### 🧾 Honest Job Title: *{generate_title()}*")

        # ------------------------
        # Export & Copy Options
        # ------------------------
        st.markdown("### 📤 Export or Share")

        st.download_button(
            label="💾 Download Decoded Text",
            data=decoded_text,
            file_name="decoded_resume.txt",
            mime="text/plain"
        )

        st.text_area(
            label="📋 Copy-Friendly Box",
            value=decoded_text,
            height=150,
            help="Click in the box, press Ctrl+A then Ctrl+C to copy."
        )

# Optional tip
st.markdown("---")
st.caption("Tip: Use 'Gen Z' or 'Corporate Satire' mode for a laugh. Try pasting your own resume!")
