from cv2 import cv2
import numpy as np
from matplotlib import pyplot as plt

####MÁSCARAS
'''
img = cv2.imread('../imgs/shapes.png')
cv2.imshow("Original", img)
mascara = np.zeros(img.shape[:2], dtype="uint8")
(cX, cY) = (img.shape[1] // 2, img.shape[0] // 2)
cv2.circle(mascara, (cX, cY), 100, 0, -1)
img_com_mascara = cv2.bitwise_and(img, img, mask=mascara)

cv2.imshow("Mascara aplicada a imagem", img_com_mascara)

'''
'''
img = cv2.imread('../imgs/Lenna.png')
cv2.imshow("Original", img)
mascara = np.zeros(img.shape[:2], dtype="uint8")
(cX, cY) = (img.shape[1] // 2, img.shape[0] // 2)
cv2.circle(mascara, (cX, cY), 180, 255, 70) #Colcoa a mascara, raio, cor, espessura do circulo
cv2.circle(mascara, (cX, cY), 70, 255, -1)
cv2.imshow("Mascara", mascara)
img_com_mascara = cv2.bitwise_and(img, img, mask = mascara)

cv2.imshow("Mascara aplicada a imagem", img_com_mascara)
'''


####SISTEMA DE CORES
'''
img = cv2.imread('../imgs/Lenna.png')
cv2.imshow("Original", img)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray", gray)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV", hsv)
lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)

cv2.imshow("L*a*b*", lab)
'''


####CANAIS DE CORES

img = cv2.imread('../imgs/Lenna.png')
(canalAzul, canalVerde, canalVermelho) = cv2.split(img)

zeros = np.zeros(img.shape[:2], dtype = "uint8")

resultado = cv2.merge([zeros, zeros, zeros])

cv2.imshow("Vermelho", canalVermelho)
cv2.imshow('Verde', canalVerde)
cv2.imshow('Azul', canalAzul)
cv2.imshow('Resultado', zeros)



cv2.waitKey(0)
