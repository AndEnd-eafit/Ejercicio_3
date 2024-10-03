import streamlit as st
import cv2
import numpy as np
import pytesseract
from PIL import Image

# Estilos personalizados con tipografías Lexend e Inter
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Lexend:wght@400;700&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap');
    
    .title {
        font-family: 'Lexend', sans-serif;
        font-weight: 700;
        text-align: center;
    }
    
    .text {
        font-family: 'Inter', sans-serif;
        text-align: justify;
    }

    .image-container {
        display: flex;
        justify-content: center;
    }
    </style>
    """, unsafe_allow_html=True)

# Título
st.markdown('<h1 class="title">Reconocimiento de caracteres</h1>', unsafe_allow_html=True)

# Espacio para la imagen (PNG)
st.markdown('<div class="image-container">', unsafe_allow_html=True)
img_file_buffer = st.file_uploader("Sube una imagen en formato PNG", type=["png"])
st.markdown('</div>', unsafe_allow_html=True)

# Filtro en el sidebar
with st.sidebar:
    filtro = st.radio("Aplicar Filtro", ('Con Filtro', 'Sin Filtro'))

# Procesamiento de imagen y OCR
if Reconocimiento de caracteres - Yoru is not None:
    # Leer el archivo de imagen
    img = Image.open(Reconocimiento de caracteres - Yoru)
    cv2_img = np.array(img)
    
    # Aplicar filtro si es necesario
    if filtro == 'Con Filtro':
        cv2_img = cv2.bitwise_not(cv2_img)
    
    # Convertir la imagen a RGB
    img_rgb = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2RGB)
    
    # Extraer texto de la imagen
    text = pytesseract.image_to_string(img_rgb)
    
    # Mostrar el texto extraído
    st.markdown('<p class="text">Texto extraído:</p>', unsafe_allow_html=True)
    st.write(text)
