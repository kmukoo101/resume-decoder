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
- BS meter with score interpretation
- ATS compatibility checker
- Save/load session state
- Inline tone highlighting
- Visual tone breakdown chart
- Resume quality score badge
- Shareable URL session encoding
- PDF export option (via base64 workaround)
- Compare multiple resumes side-by-side
- Live dynamic rewrite toggle (future)
- Print-friendly / styled export (future)
"""

import streamlit as st
from app.components import text_utils
from utils.funny_titles import generate_title
from utils.style_metadata import STYLE_DESCRIPTIONS
from utils.score_meter import interpret_score, render_progress_bar, render_bs_meter, calculate_resume_quality, render_quality_badge
from utils.ats_check import check_ats_friendly
from utils.tone_analyzer import analyze_tone
from utils.session_storage import create_export_bundle
import altair as alt
import json
import os
import base64
import re

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

st.title("Resume Decoder")
st.caption("Translate job descriptions and resumes into real talk. No more corporate fluff.")

st.markdown("Paste in your resume or job post below, or upload a file. We'll decode it for clarity, honesty, or humor.")

# ------------------------
# File Upload or Text Input
# ------------------------

uploaded_file = st.file_uploader("Upload resume/job description (PDF, DOCX, TXT)", type=["pdf", "docx", "txt"])
user_input = ""

if uploaded_file:
    import fitz  # PyMuPDF
    try:
        with fitz.open(stream=uploaded_file.read(), filetype="pdf") as doc:
            user_input = "\n".join([page.get_text() for page in doc])
    except Exception:
        st.error("Failed to extract text from uploaded file.")

st.subheader("Or Paste Text")
user_input_manual = st.text_area("Text area", height=300, placeholder="Paste job description or resume here...")
if user_input_manual:
    user_input = user_input_manual

style = st.radio("Choose your decoding style", options=list(STYLE_DESCRIPTIONS.keys()), format_func=lambda x: f"{STYLE_DESCRIPTIONS[x]}")

# ------------------------
# Decode and Display Results
# ------------------------

if st.button("Decode It"):
    if not user_input.strip():
        st.warning("Please enter or upload text to decode.")
    else:
        decoded_text, score, highlights, tone_highlighted = text_utils.decode_text(user_input, buzzword_map, style)

        layout = st.radio("Choose Layout", ["Stacked", "Side-by-Side"], horizontal=True)

        st.markdown(f"### Buzzword Score: {score}%")
        render_progress_bar(score)
        st.markdown(interpret_score(score))
        render_bs_meter(score)

        tone_data = analyze_tone(user_input)
        if tone_data:
            chart_data = [{"Tone": k.title(), "Count": v} for k, v in tone_data.items()]
            tone_chart = alt.Chart(alt.Data(values=chart_data)).mark_bar().encode(
                x="Tone:N",
                y="Count:Q",
                color="Tone:N"
            ).properties(height=200)
            st.altair_chart(tone_chart, use_container_width=True)
        else:
            st.info("No dominant tones found in text.")

        ats_result = check_ats_friendly(user_input)
        quality = calculate_resume_quality(score, 100 * sum(ats_result.values()) / len(ats_result), tone_data)
        render_quality_badge(quality)

        if layout == "Side-by-Side":
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("### 🪞 Decoded")
                st.write(decoded_text)
            with col2:
                st.markdown("### Original with Highlights")
                st.markdown(highlights, unsafe_allow_html=True)
        else:
            st.markdown("### Decoded Version")
        
            # Format decoded text for readability
            clean_text = decoded_text.replace("•", "\n\n🔹").replace("●", "\n\n🔸").replace("  ", " ").strip()
            lines = clean_text.split("\n")
        
            for line in lines:
                line = line.strip()
                if not line:
                    st.markdown("<br>", unsafe_allow_html=True)
                    continue
        
                if "EXPERIENCE" in line.upper():
                    st.markdown(f"### 💼 **{line}**")
                elif "SKILLS" in line.upper():
                    st.markdown(f"### 🧠 **{line}**")
                elif line.endswith(":"):
                    st.markdown(f"**{line}**")
                elif line.strip().lower().startswith("co-owner") or re.match(r"^[A-Z][a-z]+.*-.*", line):
                    st.markdown(f"#### 🧾 *{line}*")
                elif re.match(r"^\d{2}/\d{4}.*-", line):
                    st.markdown(f"#### 📅 {line}")
                else:
                    st.markdown(line)


            # Format decoded text for readability
            clean_text = decoded_text.replace("•", "\n\n🔹").replace("●", "\n\n🔸").replace("  ", " ").strip()
            lines = clean_text.split("\n")
        
            for line in lines:
                line = line.strip()
                if not line:
                    st.markdown("<br>", unsafe_allow_html=True)
                    continue
        
                if "EXPERIENCE" in line.upper():
                    st.markdown(f"### 💼 **{line}**")
                elif "SKILLS" in line.upper():
                    st.markdown(f"### 🧠 **{line}**")
                elif line.endswith(":"):
                    st.markdown(f"**{line}**")
                elif line.strip().lower().startswith("co-owner") or re.match(r"^[A-Z][a-z]+.*-.*", line):
                    st.markdown(f"#### 🧾 *{line}*")
                elif re.match(r"^\d{2}/\d{4}.*-", line):
                    st.markdown(f"#### 📅 {line}")
                else:
                    st.markdown(line)


            # Clean line breaks and spacing for resume formatting
            clean_text = decoded_text.replace("•", "\n\n🔹").replace("●", "\n\n🔸").replace("  ", " ").strip()
            lines = clean_text.split("\n")
            
            for line in lines:
                if line.strip() == "":
                    st.markdown("---")  # adds a divider
                else:
                    st.markdown(f"{line.strip()}")

            st.markdown("### Original with Highlights")
            st.markdown(highlights, unsafe_allow_html=True)

        st.markdown(f"### Honest Job Title: *{generate_title()}*")

        st.markdown("### ATS Compatibility Check")
        for k, v in ats_result.items():
            st.markdown(f"- **{k.replace('_', ' ').title()}**: {'✅' if v else '❌'}")

        st.markdown("### Export or Share")

        export_bundle = create_export_bundle(
            input_text=user_input,
            decoded=decoded_text,
            style=style,
            buzzword_score=score,
            tone_results=tone_data,
            ats_results=ats_result,
            quality_score=quality
        )

        st.download_button(
            label="Download Decoded Text",
            data=decoded_text,
            file_name="decoded_resume.txt",
            mime="text/plain"
        )

        st.download_button(
            label="Save Full Session",
            data=json.dumps(export_bundle),
            file_name="resume_decoder_session.json",
            mime="application/json"
        )

        encoded = base64.urlsafe_b64encode(json.dumps(export_bundle).encode("utf-8")).decode("utf-8")
        share_url = f"?state={encoded}"
        st.text_input("Shareable Link", value=share_url)

        st.text_area(
            label="Copy-Friendly Box",
            value=decoded_text,
            height=150,
            help="Click in the box, press Ctrl+A then Ctrl+C to copy."
        )

st.markdown("---")
st.caption("Tip: Use 'Gen Z' or 'Corporate Satire' mode for a laugh. Try uploading your own resume!")

