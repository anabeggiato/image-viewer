# Funções de tratamento de erros

import os
import cv2
import streamlit as st
from PIL import UnidentifiedImageError

def carregar_imagem(caminho):
    try:
        if not os.path.isfile(caminho):
            st.error("Arquivo não encontrado.")
            return None

        imagem = cv2.imread(caminho)
        if imagem is None:
            st.error("Erro ao carregar imagem. Verifique o formato.")
            return None

        return imagem
    except UnidentifiedImageError:
        st.error("Arquivo selecionado não é uma imagem válida.")
        return None
    except Exception as e:
        st.error(f"Ocorreu um erro ao carregar a imagem: {str(e)}")
        return None

def salvar_imagem(imagem, caminho="imagem_editada.png"):
    if imagem is None:
        st.warning("Nenhuma imagem para salvar. Aplique um filtro primeiro.")
        return
    try:
        cv2.imwrite(caminho, imagem)
        st.success(f"Imagem salva com sucesso: {caminho}")
    except Exception as e:
        st.error(f"Erro ao salvar a imagem: {str(e)}")
