"""
Resume Builder Page

This Streamlit page helps users build an ATS-optimized resume by combining:
- a job description,
- an existing resume,
- and keyword analysis.

Features:
- Upload or paste job description
- Upload or paste current resume
- Keyword gap analysis (between job & resume)
- Matching score / fit %
- AI-suggested improvements per section
- Editable text blocks for each section
- Export as ATS-ready PDF or DOCX
"""

import streamlit as st
from utils.resume_tools import extract_keywords, match_keywords, suggest_resume_sections
from utils.file_loader import load_text_from_file
from utils.export import export_to_docx
import json

st.title("Resume Builder")
st.caption("Rebuild your resume based on a job description and your current resume.")

# ------------------------
# Inputs: Job & Resume
# ------------------------
col1, col2 = st.columns(2)

with col1:
    job_file = st.file_uploader("Upload Job Description", type=["pdf", "docx", "txt"], key="job")
    job_text = st.text_area("Or paste job description", height=300)
    if job_file:
        job_text = load_text_from_file(job_file)

with col2:
    resume_file = st.file_uploader("Upload Current Resume", type=["pdf", "docx", "txt"], key="resume")
    resume_text = st.text_area("Or paste current resume", height=300)
    if resume_file:
        resume_text = load_text_from_file(resume_file)

if job_text and resume_text:
    st.markdown("---")
    st.subheader("Job Match Analysis")

    job_keywords = extract_keywords(job_text)
    resume_keywords = extract_keywords(resume_text)
    match_result = match_keywords(job_keywords, resume_keywords)

    st.write(f"**Match Score:** {match_result['match_percent']}%")
    st.progress(int(match_result['match_percent']))

    if match_result['missing_keywords']:
        st.warning("Missing Keywords:")
        st.markdown(", ".join(match_result['missing_keywords']))

    st.markdown("---")
    st.subheader("Resume Suggestions")

    sections = suggest_resume_sections(job_text, resume_text)
    edited_sections = {}

    for section in sections:
        with st.expander(section['title'], expanded=True):
            edited_text = st.text_area("Edit this section", value=section['content'], height=200)
            edited_sections[section['title']] = edited_text

    if st.button("Export as DOCX"):
        docx_data = export_to_docx(edited_sections)
        st.download_button(
            label="Download ATS Resume",
            data=docx_data,
            file_name="ATS_Resume.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        )

else:
    st.info("Please provide both a job description and your current resume.")
