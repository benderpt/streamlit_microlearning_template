# scripts/components.py
import streamlit as st
import os
import json
from streamlit_lottie import st_lottie

def configure_sidebar():
    """
    Configures the sidebar of the Streamlit application.

    This function sets up the sidebar with a logo, title, objectives, links, and a reset button.
    It checks if the logo and icon files exist before displaying them.
    """
    logo_path = "content/Assets/logos/logo.png"
    icon_path = "content/Assets/logos/logo.png"
    
    # Check if the logo and icon files exist
    if os.path.exists(logo_path) and os.path.exists(icon_path):
        st.logo(logo_path, icon_image=icon_path)
    else:
        st.error("Logo or icon not found.")

    st.sidebar.title("What is data? 📊")
    st.sidebar.divider()
    st.sidebar.subheader("Objectives 🎯")
    st.sidebar.markdown("""
    Understand concepts of data in the following dimensions:
- Its definition and essential requisites
- The transistor and the digital revolution
- The exponential growth of digital data
- The different types of digital data
    """)
    st.sidebar.divider()
    
    # Display the "Restart" button only if not in the first section
    if st.session_state.get('current_section', 0) > 0:
        if st.sidebar.button("Restart"):
            st.session_state.current_section = 0
            st.rerun()