import streamlit as st
from PIL import Image
import os

def slider_app():

    # CSS to hide the tick labels below the slider and the current value
    # and add padding to the sides of the slider
    st.markdown("""
        <style>
        /* Hide the tick labels below the slider */
        .stSlider div[data-testid="stTickBar"] > div {
            display: none;
        }
        /* Add padding to the sides of the slider */
        .stSlider {
            padding-left: 11%;
            padding-right: 11%;
        }
        </style>
    """, unsafe_allow_html=True)
    
    images = [
        {"title": "Disponibilização de robôs", "file": "content/Assets/section1/image1.png"},
        {"title": "Atividade fisica e companhia", "file": "content/Assets/section1/image2.png"},
        {"title": "Melhoria  Saúde física e mental", "file": "content/Assets/section1/image3.png"},
    ]

    # Create the select slider
    slider_labels = [img["title"] for img in images]
    slider_value = st.select_slider("Importância do acesso a dados", label_visibility="hidden", options=slider_labels)

    # Find the index of the selected label
    selected_index = slider_labels.index(slider_value)
    image_info = images[selected_index]

    # Display the image based on the slider value
    image = Image.open(image_info["file"])
    st.image(image, use_column_width=True)

# Ensure the script can be run standalone for testing
if __name__ == "__main__":
    slider_app()