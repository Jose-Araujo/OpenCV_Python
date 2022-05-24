from cv2 import cv2
import numpy as np
from matplotlib import pyplot as plt

####MÁSCARAS

img = cv2.imread('../imgs/Lenna.png')
cv2.imshow("Original", img)
mascara = np.zeros(img.shape[:2], dtype="uint8")
(cX, cY) = (img.shape[1] // 2, img.shape[0] // 2)
cv2.circle(mascara, (cX, cY), 100, 255, -1)
#cv2.imshow("Mascara1", mascara)
img_com_mascara1 = cv2.bitwise_and(img, img, mask=mascara)

cv2.circle(mascara, (cX, cY), 180, 255, 70) #Colcoa a mascara, raio, cor, espessura do circulo
cv2.circle(mascara, (cX, cY), 70, 255, -1)
cv2.imshow("Mascara2", mascara)
img_com_mascara2 = cv2.bitwise_and(img, img, mask = mascara)

#cv2.imshow("Mascara aplicada a imagem1", img_com_mascara1)
cv2.imshow("Mascara aplicada a imagem2", img_com_mascara2)


temp = np.vstack([
    np.hstack([img, img_com_mascara2])
])

cv2.imshow("Mascara", temp)
####SISTEMA DE CORES

# img = cv2.imread('../imgs/Lenna.png')
# cv2.imshow("Original", img)
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow("Gray", gray)
# hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# cv2.imshow("HSV", hsv)
# lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
#
# cv2.imshow("L*a*b*", lab)

####CANAIS DE CORES

# img = cv2.imread('../imgs/Lenna.png')
# (canalAzul, canalVerde, canalVermelho) = cv2.split(img)
#
# zeros = np.zeros(img.shape[:2], dtype = "uint8")
#
# resultado = cv2.merge([canalAzul, zeros, zeros])
#
# cv2.imshow("Vermelho", canalVermelho)
# cv2.imshow('Verde', canalVerde)
# cv2.imshow('Azul', canalAzul)
# cv2.imshow('Resultado', resultado)

cv2.waitKey(0)