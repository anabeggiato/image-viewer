import cv2

def escala_cinza(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)