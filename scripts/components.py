# scripts/components.py
import streamlit as st
import os
import sys
import json
from streamlit_lottie import st_lottie


def render_single_choice_question(section):
    """
    Renders a single-choice question and handles user responses.
    
    This function displays a single-choice question, processes user input, and provides feedback.
    """
    st.write(section["question"])
    options = section.get("options", [])
    
    feedback_placeholder = st.empty()

    if not st.session_state.get("response_submitted", False):
        selected_option = st.radio("Select an option", options)

        if selected_option:
            if st.button(section.get("button_text", "Submit", type="primary")):
                st.session_state.response_submitted = True
                st.session_state.selected_option = selected_option
                st.experimental_rerun()  # Force a rerun to update the state

    if st.session_state.get("response_submitted", False):
        selected_option = st.session_state.get("selected_option", "")
        explanation = section["explanations"]
        correct = selected_option in section["answer"]
        if correct:
            feedback_placeholder.success(f"{selected_option}: Correct! {explanation}")
        else:
            feedback_placeholder.error(f"{selected_option}: Incorrect. {explanation}")

        # Add columns for buttons
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button(section.get("button_answer", "Continue", type="primary")):
                st.session_state.current_section += 1
                st.session_state.response_submitted = False
                st.experimental_rerun()
        if not correct:
            with col2:
                if st.button("Try again"):
                    st.session_state.response_submitted = False
                    st.experimental_rerun()  # Refresh the page
        if st.session_state.current_section > 0:
            with col3:
                if st.button("Go back"):
                    st.session_state.current_section -= 1
                    st.session_state.response_submitted = False
                    st.experimental_rerun()

def render_multiple_choice_question(section):
    """
    Renders a multiple-choice question and handles user responses.
    
    This function displays a multiple-choice question, processes user input, and provides feedback.
    """
    st.write(section["question_multiple"])
    options = section.get("options", [])
    
    feedback_placeholder = st.empty()

    if not st.session_state.get("response_submitted", False):
        selected_options = st.multiselect(
            "Select one or more options", options, placeholder="Select an option", key="multiselect"
        )

        if selected_options:
            if st.button(section.get("button_text", "Submit"), type="primary"):
                st.session_state.response_submitted = True
                st.session_state.selected_options = selected_options
                st.experimental_rerun()  # Force a rerun to update the state

    if st.session_state.get("response_submitted", False):
        selected_options = st.session_state.get("selected_options", [])
        correct_count = 0  # Correct answer counter
        incorrect_count = 0  # Incorrect answer counter

        for option in selected_options:
            explanation = section["explanations"].get(option, "")
            if option in section["answer"]:
                st.success(f"{option}: {explanation}")
                correct_count += 1  # Increment correct answer counter
            else:
                st.error(f"{option}: {explanation}")
                incorrect_count += 1  # Increment incorrect answer counter

        # Provide overall feedback
        all_correct = correct_count == len(section["answer"]) and incorrect_count == 0
        if all_correct:
            feedback_placeholder.success("All answers are correct!")
        elif correct_count > 0 and incorrect_count > 0:
            feedback_placeholder.warning("Some answers are correct, but there are also incorrect answers.")
        elif correct_count == 1 and incorrect_count == 0:
            feedback_placeholder.warning("Correct answer, but still incomplete.")
        elif correct_count > 1 and correct_count < len(section["answer"]) and incorrect_count == 0:
            feedback_placeholder.warning("Correct answers, but incomplete.")
        else:
            feedback_placeholder.error("There are incorrect answers.")
        
        # Add columns for buttons
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button(section.get("button_answer", "Continue"), type="primary"):
                st.session_state.current_section += 1
                st.session_state.response_submitted = False
                st.experimental_rerun()
        if not all_correct:
            with col2:
                if st.button("Try again"):
                    st.session_state.response_submitted = False
                    st.experimental_rerun()  # Refresh the page
        if st.session_state.current_section > 0:
            with col3:
                if st.button("Go back"):
                    st.session_state.current_section -= 1
                    st.session_state.response_submitted = False
                    st.experimental_rerun()

def render_question_content(section):
    """
    Renders a question section and handles user responses based on question type.

    This function delegates rendering and response handling to the appropriate
    single-choice or multiple-choice question function based on the section content.
    """
    if "question_multiple" in section:
        render_multiple_choice_question(section)
    elif "question" in section:
        render_single_choice_question(section)

def render_static_content(section):
    """
    Renders static content including title, image, and text.

    This function displays a title, an image if it exists, and formatted text from the provided section.
    """
    if "title" in section:
        st.markdown(f"<h3 style='text-align: center;'>{section['title']}</h3>", unsafe_allow_html=True)
    if "image_path" in section and os.path.exists(section["image_path"]):
        st.image(section["image_path"])
    if "lottie" in section and os.path.exists(section["lottie"]):
        with open(section["lottie"], 'r') as f:
            lottie_animation = json.load(f)
        st_lottie(lottie_animation)
    st.divider()
    if "text" in section:
        st.markdown(section["text"].replace("\n", "  \n"))

def render_script_content(section):
    """
    Executes a script if present in the section.

    This function dynamically imports and runs a Python script specified in the section.
    """
    if "script_path" in section:
        script_path = section["script_path"]
        script_dir, script_name = os.path.split(script_path)
        script_module_name = script_name.replace('.py', '')

        # Add script directory to the system path
        sys.path.append(script_dir)

        # Read and execute the script
        with open(script_path) as f:
            code = f.read()
            exec(code, globals())

        st.divider()
        st.write(section["explanations"])

def render_navigation_buttons(section):
    """
    Renders navigation buttons for moving between sections.

    This function displays buttons for continuing to the next section or going back to the previous section.
    """
    if "button_text" in section:
        if st.session_state.current_section > 0:
            st.subheader('', divider='rainbow')
            col1, col2 = st.columns(2)
            with col1:
                if st.button(section["button_text"], type="primary"):
                    st.session_state.current_section += 1
                    st.rerun()
            with col2:
                if st.button("Go back"):
                    st.session_state.current_section -= 1
                    st.rerun()
        else:
            if st.button(section["button_text"], type="primary"):
                st.session_state.current_section += 1
                st.rerun()

def load_quiz_data(file_path):
    """
    Loads quiz data from a JSON file.

    Args:
        file_path (str): Path to the JSON file containing quiz data.

    Returns:
        dict: Parsed JSON data as a dictionary.
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)
