"""
Styling Helpers for Resume Decoder

This module injects custom CSS and reusable layout elements to improve
the app’s visual polish and user experience.

Features:
- Custom highlight colors
- Typography tweaks
- Consistent spacing and alignment
- Section dividers and headers
"""

import streamlit as st

def inject_custom_css():
    """
    Injects custom CSS to style the app, including:
    - Highlight colors
    - Font sizes
    - Section spacing
    - Custom mark element for buzzword tooltips
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
