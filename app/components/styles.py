"""
Styling Helpers for Resume Decoder

This module injects custom CSS and reusable layout elements to improve
the app’s visual polish and user experience.

Features:
- Custom highlight colors
- Typography tweaks
- Consistent spacing and alignment
- Section dividers and headers
- Color-coded BS Meter ranges
- ATS result styling
- Tone category inline highlights
"""

import streamlit as st

def inject_custom_css():
    """
    Injects custom CSS to style the app, including:
    - Highlight colors
    - Font sizes
    - Section spacing
    - Custom mark element for buzzword tooltips
    - Score badge styling
    - BS Meter and ATS feedback colors
    - Tone keyword coloring
    """
    st.markdown("""
    <style>
    /* General tweaks */
    body, html {
        font-family: 'Segoe UI', sans-serif;
        color: #222;
    }

    /* Highlighted buzzwords */
    mark {
        background-color: #fffb91;
        padding: 2px 4px;
        border-radius: 4px;
        cursor: help;
        transition: background 0.3s ease;
    }

    mark:hover {
        background-color: #ffe36f;
    }

    /* Section headers */
    .section-header {
        font-size: 1.4rem;
        font-weight: 600;
        margin-top: 2rem;
        margin-bottom: 1rem;
        border-bottom: 2px solid #eee;
        padding-bottom: 0.25rem;
    }

    /* Score badge */
    .score-badge {
        background-color: #efefef;
        padding: 0.4rem 0.8rem;
        font-size: 1rem;
        font-weight: bold;
        border-radius: 10px;
        display: inline-block;
        margin-bottom: 1rem;
    }

    /* BS Meter Colors */
    .bs-low {
        color: #2e8b57; /* green */
        font-weight: bold;
    }

    .bs-medium {
        color: #e69a00; /* amber */
        font-weight: bold;
    }

    .bs-high {
        color: #cc0000; /* red */
        font-weight: bold;
    }

    /* ATS status */
    .ats-good {
        color: #228B22;
        font-weight: 600;
    }

    .ats-bad {
        color: #B22222;
        font-weight: 600;
    }

    /* Tone keyword coloring */
    .tone-corporate {
        background-color: #e0f0ff;
        color: #0077b6;
        padding: 1px 4px;
        border-radius: 3px;
    }

    .tone-action {
        background-color: #e9ffe9;
        color: #1b5e20;
        padding: 1px 4px;
        border-radius: 3px;
    }

    .tone-creative {
        background-color: #fbeeff;
        color: #9c27b0;
        padding: 1px 4px;
        border-radius: 3px;
    }

    .tone-emotional {
        background-color: #fff6e6;
        color: #ff6f00;
        padding: 1px 4px;
        border-radius: 3px;
    }

    .tone-fluff {
        background-color: #fff0f0;
        color: #b00020;
        padding: 1px 4px;
        border-radius: 3px;
    }

    /* Footer */
    footer {
        font-size: 0.8rem;
        color: #888;
        margin-top: 3rem;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

def score_badge(score: int):
    """
    Render a styled score badge.

    Parameters:
        score (int): Buzzword density percentage

    Returns:
        str: Renderable HTML
    """
    return f"<div class='score-badge'>Buzzword Score: {score}%</div>"

def section_header(title: str):
    """
    Render a visually distinct section header.

    Parameters:
        title (str): Section heading text
    """
    st.markdown(f"<div class='section-header'>{title}</div>", unsafe_allow_html=True)
