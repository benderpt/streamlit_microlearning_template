import streamlit as st
from streamlit_lottie import st_lottie
import json

# Load Lottie animation
def load_lottie(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

# Correct percentage of global internet traffic represented by video
correct_percentage = 53  # This is an example value, you can adjust it based on the latest data
error_margin = 5
close_margin = 10

# Initialize session state
if 'submitted' not in st.session_state:
    st.session_state.submitted = False

# Display Lottie animation
lottie_animation = load_lottie("content/Assets/section7.json")
st_lottie(lottie_animation, height=300)

# Slider for user input
user_guess = st.slider("Can you guess what percentage of global internet traffic is represented by video?", 0, 100, 50)

# Submit button and feedback
if not st.session_state.submitted:
    if st.button("Submit"):
        if abs(user_guess - correct_percentage) <= error_margin:
            st.session_state.submitted = True
            st.success(f"Correct! Video represents approximately {correct_percentage}% of global internet traffic.")
        elif abs(user_guess - correct_percentage) <= close_margin:
            st.warning(f"You were close!")
        else:
            st.error(f"Not quite!")

