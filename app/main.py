"""
Resume Decoder: A Streamlit app that translates job descriptions and resumes
into plain, honest language, or a humorous rewrite, to help users
see through corporate jargon and fluff.

Features:
- Buzzword detection
- Plain English decoding
- Multiple voice styles (e.g., Real Talk, Gen Z)
- Buzzword scoring and highlights
"""

import streamlit as st
from components import text_utils
import json

# Load buzzword mapping
with open("utils/buzzwords.json", "r") as f:
    buzzword_map = json.load(f)

# ---------------------
# Streamlit UI Layout
# ---------------------

st.set_page_config(page_title="Resume Decoder", layout="centered")

st.title("Resume Decoder")
st.caption("Cut through the fluff. Get the truth. Decode resumes and job descriptions with one click.")

# Text input
st.subheader("Paste Your Resume or Job Description")
uploaded_file = st.file_uploader("Upload your resume or job description", type=["pdf", "docx", "txt"])
user_input = ""

if uploaded_file:
    if uploaded_file.type == "application/pdf":
        import fitz  # PyMuPDF
        with fitz.open(stream=uploaded_file.read(), filetype="pdf") as doc:
            user_input = "\n".join([page.get_text() for page in doc])
    elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        import docx
        doc = docx.Document(uploaded_file)
        user_input = "\n".join([para.text for para in doc.paragraphs])
    else:
        user_input = uploaded_file.read().decode("utf-8")

# Style selection
style = st.selectbox("Choose Translation Style", ["Plain English", "Real Talk", "Gen Z", "Corporate Satire"])

# Decode button
if st.button("Decode It"):
    if not user_input.strip():
        st.warning("Please enter some text to decode.")
    else:
        # Decode the input
        decoded_text, score, highlights, tone_highlighted = text_utils.decode_text(user_input, buzzword_map, style=style)

        # Display score and interpretation
        st.markdown(f"**Buzzword Score:** {score}%")
        st.markdown("### Decoded Version:")
        st.write(decoded_text)

        # Show original with highlights
        st.markdown("### ✏Original with Highlights:")
        st.markdown(highlights, unsafe_allow_html=True)
