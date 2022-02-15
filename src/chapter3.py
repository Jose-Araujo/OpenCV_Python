
from cv2 import cv2
import numpy as npp

#RESIZING AND CROPPING

img = cv2.imread("../imgs/gato1.jpg")
print(img.shape) #Ver as dimensões e a quantidade de canais de uma imagem

imgResize = cv2.resize(img, (512,341)) #Para alterar o tamanho de uma imagem, aumentando ou diminuindo suas dimensões utilizamos a função cv2.resize(imagem, (X, Y))
print(imgResize.shape)
imgSlicing = img[::3, ::3] #Reduz a imgaem em duas vezes o tamanho original
#print(imgSlicing.shape)
imgCropped = img[0:200, 200:500] #Faz um corte da imagem a artir das dimensões fornecidas

#ESPELHANDO IMAGEM
#flip_h = imgSlicing[::-1, :] # espelhar a imagem na horizontal
flip_h = cv2.flip(imgSlicing, 1) # comando equivalente

#flip_v = imgSlicing[:, ::-1] # espelhar a imagem na vertical
flip_v = cv2.flip(imgSlicing, 0) # comando equivalente

#flip_hv = imgSlicing[::-1,::-1] # espelhar a imagem na vertical e horizontal
flip_h = cv2.flip(imgSlicing, -1) # comando equivalente

#ROTACIONANDO IMAGEM
(alt, lar) = imgSlicing.shape[:2]
centro = (lar//2, alt//2)

M = cv2.getRotationMatrix2D(centro, 45, 1)
imgRotate = cv2.warpAffine(imgSlicing, M, (lar, alt))

#cv2.imshow("Image", img)
#cv2.imshow("Resize Image", imgResize)
#cv2.imshow("Image Cropped", imgCropped)
#cv2.imshow("Slicing", imgSlicing)
cv2.imshow("Rotate Image", imgRotate)

cv2.waitKey(0)