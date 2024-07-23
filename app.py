import streamlit as st
from scripts.components import render_static_content, render_question_content, render_script_content, render_navigation_buttons, load_quiz_data
from scripts.sidebar import configure_sidebar
from scripts.endsection import render_end_section

def run():
    st.set_page_config(
        page_title="What is data?",
        page_icon="content/Assets/logos/logo.png",
        initial_sidebar_state="collapsed",
    )

    # CSS personalizado para os botões
    st.markdown("""
    <style>
    div.stButton > button {
        display: block;
        margin: 0 auto;
    }
    </style>
    """, unsafe_allow_html=True)

    # Inicializar o estado da aplicação
    if 'current_section' not in st.session_state:
        st.session_state.current_section = 0

    # Carrega os dados do quiz
    section_structure = load_quiz_data('sections_structure.json')

    def render_section(section):
        render_static_content(section)
        render_question_content(section)
        render_script_content(section)
        render_navigation_buttons(section)

    # Renderizar a secção atual
    current_section = st.session_state.current_section

    configure_sidebar()

    if current_section < len(section_structure):
        render_section(section_structure[current_section])
    else:
        render_end_section()

if __name__ == "__main__":
    run()
