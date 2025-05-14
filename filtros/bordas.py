import cv2

def detectar_bordas(img):
    img_cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_blur = cv2.GaussianBlur(img_cinza, (5, 5), 1.4)
    
    return cv2.Canny(img_blur, 100, 200)