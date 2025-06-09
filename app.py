import os
import cv2
import streamlit as st
from PIL import UnidentifiedImageError

from utils import carregar_imagem, salvar_imagem  

import numpy as np
from PIL import Image
import io
from filtros import aplicar_filtro

st.set_page_config(page_title="Visualizador de Imagens", layout="wide")
st.title("Visualizador de Imagens com Filtros")

# Upload da imagem
uploaded_file = st.file_uploader("Escolha uma imagem", type=["jpg", "jpeg", "png"])

# Lista de filtros disponíveis
filtros = [
    "Nenhum",
    "Escala de cinza",
    "Inversão de cores",
    "Aumento de contraste",
    "Desfoque",
    "Aumentar nitidez",
    "Detecção de bordas"
]
filtro_escolhido = st.selectbox("Selecione um filtro para aplicar", filtros)

# Quando a imagem for carregada
if uploaded_file:
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, 1)  # Lê a imagem como BGR

    # Aplica o filtro escolhido
    img_filtrada = aplicar_filtro(img.copy(), filtro_escolhido)

    # Layout com duas colunas para comparação
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Imagem original")
        st.image(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), use_container_width=True)

    with col2:
        st.subheader("Imagem com filtro aplicado")
        if len(img_filtrada.shape) == 2:
            st.image(img_filtrada, channels="GRAY", use_container_width=True)
        else:
            st.image(cv2.cvtColor(img_filtrada, cv2.COLOR_BGR2RGB), use_container_width=True)

    # Converte a imagem filtrada para PIL
    if len(img_filtrada.shape) == 2:
        result_pil = Image.fromarray(img_filtrada)
    else:
        result_pil = Image.fromarray(cv2.cvtColor(img_filtrada, cv2.COLOR_BGR2RGB))

    # Salva a imagem em bytes para download
    buf = io.BytesIO()
    result_pil.save(buf, format="PNG")
    byte_im = buf.getvalue()

    # Botão de download
    st.download_button("Baixar imagem filtrada", data=byte_im, file_name="imagem_filtrada.png", mime="image/png")
