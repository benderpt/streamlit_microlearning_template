import streamlit as st
from streamlit_lottie import st_lottie
import json

# Load Lottie animation
@st.cache_data
def load_lottie(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

# Correct percentage of global internet traffic represented by video
correct_percentage = 50  # This is an example value, you can adjust it based on the latest data

# Initialize session state
if 'submitted' not in st.session_state:
    st.session_state.submitted = False
if 'user_guess' not in st.session_state:
    st.session_state.user_guess = 50  # Default value for slider

# Display Lottie animation
lottie_animation = load_lottie("content/Assets/section7.json")
st_lottie(lottie_animation, height=300)

# Form for user input
with st.form("guess_form"):
    st.session_state.user_guess = st.slider(
        "From the imense data that transits the internet, what approximately percentage of global internet traffic is do you think is represented by video?", 
        0, 100, 50, step=10, format="%d%%"
    )
    submitted = st.form_submit_button("Submit")

# Check for submission and provide feedback
if submitted:
    user_guess = st.session_state.user_guess
    if user_guess == correct_percentage:
        st.success(f"Correct! Video represents approximately 53% of global internet traffic.")
    elif user_guess > correct_percentage:
        st.info(f"Your guess of {user_guess}% is higher than the actual percentage.")
    else:
        st.info(f"Your guess of {user_guess}% is lower than the actual percentage.")

# Source information
st.write("""
Source: [Exploding Topics - Data Generated Per Day](https://explodingtopics.com/blog/data-generated-per-day#region)
""")
