import numpy as np

def aumentar_contraste(img, fator=1.7):
    return np.clip(img * fator, 0, 255).astype(np.uint8)
