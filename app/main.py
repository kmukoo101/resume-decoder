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
- Honest job title generator
- BS meter with score interpretation
- ATS compatibility checker
- Save/load session state
- Inline tone highlighting
- Visual tone breakdown chart
- Resume quality score badge
- Shareable URL session encoding
- PDF export option (via base64 workaround)
- Compare multiple resumes side-by-side (future)
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
st.caption("Translate job descriptions and resumes into real talk.")

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

        st.markdown(f"### Buzzword Score: `{score}%`")
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

        st.markdown("### Decoded Summary")
        jobs = text_utils.extract_experience_sections(decoded_text)
        if jobs:
            for i, job in enumerate(jobs):
                with st.expander(f"{job['title']} at {job['company']} — {job['dates']}", expanded=(i==0)):
                    st.markdown(f"**Summary:** {job['summary']}")
                    for point in job['bullets']:
                        st.markdown(f"- {point}")
        else:
            st.code(decoded_text, language="markdown")

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
st.caption("This is for a laugh. Don't take life so serious.")
