import cv2

def desfocar(img):
    return cv2.blur(img, (10, 10))