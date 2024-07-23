import streamlit as st
from streamlit_lottie import st_lottie
import json

# Load Lottie animation
def load_lottie(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

def render_end_section():
    # Display Lottie animation
    lottie_animation = load_lottie("content/Assets/endsection.json")
    st_lottie(lottie_animation, height=300)
    

    
    st.markdown(f"""
        <div style="text-align: center;">
            <h3> 🎓 Congratulations! You have completed the microlearning session on data. 🎓</h3>
            <h4>I hope it helped you look at data from a different perspective</h4>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")

    # Restart button
    if st.button("Restart", key="end_restart"):
        st.session_state.current_section = 0
        st.rerun()
