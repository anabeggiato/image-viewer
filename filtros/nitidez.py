import numpy as np
import cv2

def aplicar_nitidez(img):
    # Kernel de nitidez
    kernel = np.array([[0, -1, 0],
                    [-1, 5,-1],
                    [0, -1, 0]])

    return cv2.filter2D(img, -1, kernel)