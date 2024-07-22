# scripts/components.py
import streamlit as st
import os
import json
from PIL import Image

def configure_sidebar():
    """Configura a sidebar do Streamlit."""
    logo_path = "content/Assets/logo.png"
    icon_path = "content/Assets/logo.png"
    
    # Verifica se os arquivos existem
    if os.path.exists(logo_path) and os.path.exists(icon_path):
        st.logo(logo_path, icon_image=icon_path)
    else:
        st.error("Logotipo ou ícone não encontrados.")

    st.sidebar.title("Micro-aprendizagem Análise da avaliabilidade de políticas 🎓")
    st.sidebar.divider()
    st.sidebar.subheader("Objetivos 🎯")
    st.sidebar.markdown("""Compreender o conceito de análise de avaliabilidade nas seguintes dimensões: \n
    - Qual a sua função
    - Quais as vantagens
    - Como se operacionaliza
    """)
    st.sidebar.divider()
    st.sidebar.markdown("[Ver guia de avaliabilidade](https://planapp.gov.pt/wp-content/uploads/2024/01/PlanAPP_Guia-Avaliabilidade-1.pdf) 📘")
    st.sidebar.markdown("[Acompanhe o PlanAPP](https://linktr.ee/planapp) 🫶")
    st.sidebar.divider()
    # Botão para reiniciar
    if st.sidebar.button("Voltar ao início"):
        st.session_state.current_section = 0
        st.rerun()


def render_question_content(section):
    """Render question and handle user response."""
    question_key = "question_multiple" if "question_multiple" in section else "question"
    if question_key in section:
        st.write(section[question_key])
        options = section.get("options", [])
        
        feedback_placeholder = st.empty()

        selected_options = st.multiselect("Selecione uma ou mais opções", options, placeholder="Selecione uma opção", key="multiselect") if question_key == "question_multiple" else st.radio("Selecione uma opção", options)

        if selected_options:
            if not st.session_state.get("response_submitted", False):
                if st.button(section.get("button_text", "Responder")):
                    st.session_state.response_submitted = True
                    st.session_state.selected_options = selected_options
                    st.experimental_rerun()  # Force a rerun to update the state
        
        if st.session_state.get("response_submitted", False):
            selected_options = st.session_state.get("selected_options", [])
            if set(selected_options) == set(section.get("answer", [])):
                feedback_placeholder.success("Correcto!")
            else:
                feedback_placeholder.error("Errado!")
            st.markdown(section["explanation"].replace("\n", "  \n"))
            st.subheader('', divider='rainbow')
            col1, col2 = st.columns(2)
            with col1:
                if st.button(section.get("button_answer", "Continuar")):
                    st.session_state.current_section += 1
                    st.session_state.response_submitted = False
                    st.rerun()
            if st.session_state.current_section > 0:
                with col2:
                    if st.button("Voltar"):
                        st.session_state.current_section -= 1
                        st.session_state.response_submitted = False
                        st.rerun()

def render_question_content(section):
    """Render question and handle user response."""
    question_key = "question_multiple" if "question_multiple" in section else "question"
    if question_key in section:
        st.write(section[question_key])
        options = section.get("options", [])
        
        feedback_placeholder = st.empty()

        if not st.session_state.get("response_submitted", False):
            selected_options = st.multiselect("Selecione uma ou mais opções", options, placeholder="Selecione uma opção", key="multiselect") if question_key == "question_multiple" else st.radio("Selecione uma opção", options)

            if selected_options:
                if st.button(section.get("button_text", "Responder")):
                    st.session_state.response_submitted = True
                    st.session_state.selected_options = selected_options
                    st.experimental_rerun()  # Force a rerun to update the state
        
        if st.session_state.get("response_submitted", False):
            selected_options = st.session_state.get("selected_options", [])
            correct_count = 0  # Contador de respostas corretas
            incorrect_count = 0  # Contador de respostas incorretas

            for option in selected_options:
                explanation = section["explanations"].get(option, "")
                if option in section["answer"]:
                    st.success(f"{option}: {explanation}")
                    correct_count += 1  # Incrementa contador de respostas corretas
                else:
                    st.error(f"{option}: {explanation}")
                    incorrect_count += 1  # Incrementa contador de respostas incorretas

            if correct_count == len(section["answer"]) and incorrect_count == 0:
                feedback_placeholder.success("Todas as respostas estão corretas!")
            elif correct_count > 0 and incorrect_count > 0:
                feedback_placeholder.warning("Existem respostas corretas, mas também existem respostas incorretas.")
            elif correct_count == 1 and incorrect_count == 0:
                feedback_placeholder.warning("Resposta correta, mas ainda incompleta.")
            elif correct_count > 1 and correct_count < len(section["answer"]) and incorrect_count == 0:
                feedback_placeholder.warning("Respostas corretas, mas incompletas.")
            else:
                feedback_placeholder.error("Existem respostas incorretas.")
            
            # Adicionar coluna extra para "Tentar novamente"
            col1, col2, col3 = st.columns(3)
            with col1:
                if st.button(section.get("button_answer", "Continuar")):
                    st.session_state.current_section += 1
                    st.session_state.response_submitted = False
                    st.experimental_rerun()
            with col2:
                if st.button("Tentar novamente"):
                    st.session_state.response_submitted = False
                    st.experimental_rerun()  # Refresh the page
            if st.session_state.current_section > 0:
                with col3:
                    if st.button("Voltar"):
                        st.session_state.current_section -= 1
                        st.session_state.response_submitted = False
                        st.experimental_rerun()

def render_static_content(section):
    """Render title, image, and text from the section."""
    if "title" in section:
        st.markdown(f"<h3 style='text-align: center;'>{section['title']}</h3>", unsafe_allow_html=True)
    if "image_path" in section and os.path.exists(section["image_path"]):
        st.image(section["image_path"])
        st.divider()
    if "text" in section:
        st.markdown(section["text"].replace("\n", "  \n"))


def render_script_content(section):
    """Execute script if present in the section."""
    if "script_path" in section:
        script_path = section["script_path"]
        script_dir, script_name = os.path.split(script_path)
        script_module_name = script_name.replace('.py', '')

        # Add script directory to the system path
        import sys
        sys.path.append(script_dir)

        # Import and run the script
        script_module = __import__(script_module_name)
        script_module.slider_app()

        st.write(section["explanation"])

def render_navigation_buttons(section):
    """Render navigation buttons."""
    if "button_text" in section:
        if st.session_state.current_section > 0:
            st.subheader('', divider='rainbow')
            col1, col2 = st.columns(2)
            with col1:
                if st.button(section["button_text"]):
                    st.session_state.current_section += 1
                    st.rerun()
            with col2:
                if st.button("Voltar"):
                    st.session_state.current_section -= 1
                    st.rerun()
        else:
            if st.button(section["button_text"]):
                st.session_state.current_section += 1
                st.rerun()

def load_quiz_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)
    
