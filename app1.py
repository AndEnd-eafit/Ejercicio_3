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
st.markdown('<h1 class="title">Reconocimiento óptico de Caracteres</h1>', unsafe_allow_html=True)

# Espacio para la imagen (PNG)
image = Image.open('Reconocimiento de caracteres - Yoru.png')
st.image(image, width=300, use_column_width='auto', caption="Imagen del Traductor")

# Captura de imagen desde la cámara
img_file_buffer = st.camera_input("Toma una Foto")

# Filtro en el sidebar
with st.sidebar:
    filtro = st.radio("Aplicar Filtro", ('Con Filtro', 'Sin Filtro'))

# Procesamiento de imagen y OCR
if img_file_buffer is not None:
    # Leer el archivo de imagen
    bytes_data = img_file_buffer.getvalue()
    cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)

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
