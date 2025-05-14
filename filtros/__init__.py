from .escala_cinza import escala_cinza
from .inversao_cores import inversao_cores
from .contraste import aumentar_contraste
from .blur import desfocar
from .nitidez import aplicar_nitidez
from .bordas import detectar_bordas

def aplicar_filtro(img, nome_filtro):
    if nome_filtro == "Escala de cinza":
        return escala_cinza(img)
    elif nome_filtro == "Inversão de cores":
        return inversao_cores(img)
    elif nome_filtro == "Aumento de contraste":
        return aumentar_contraste(img)
    elif nome_filtro == "Desfoque":
        return desfocar(img)
    elif nome_filtro == "Aumentar nitidez":
        return aplicar_nitidez(img)
    elif nome_filtro == "Detecção de bordas":
        return detectar_bordas(img)
    else:
        return img
