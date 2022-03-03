
from cv2 import cv2
import numpy as np
import mahotas

img = cv2.resize(cv2.imread("../imgs/Lenna.png"), (400,400))
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
suave = cv2.GaussianBlur(img, (7, 7), 0) #Aplicação de blur peolo método gaussiana

#BINARIZÇÃO COM LIMIAR

(T, bin) = cv2.threshold(suave, 160, 255, cv2.THRESH_BINARY) #thresh: foi escolhido um valor arbitrário
(T, binI) = cv2.threshold(suave, 160, 255, cv2.THRESH_BINARY_INV)

resultado = np.vstack([
    np.hstack([suave, bin]),
    np.hstack([binI, cv2.bitwise_and(img, img, mask = binI)])
])

# cv2.imshow("Binarizacao da imagem", resultado)

#THRESHOLD ADAPTATIVO

bin1 = cv2.adaptiveThreshold(suave, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 21, 5)
bin2 = cv2.adaptiveThreshold(suave, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 21, 5)

resuldadoAdaptativo = np.vstack([
    np.hstack([img, suave]),
    np.hstack([bin1, bin2])
])

# cv2.imshow("Binarizacao adaptativo", resuldadoAdaptativo)

#THRESHHOLD COM OTSU E RIDDLER-CALVARD

T = mahotas.thresholding.otsu(suave)
temp = img.copy()

temp[temp > T] = 255
temp[temp < 255] = 0
temp = cv2.bitwise_not(temp)
T = mahotas.thresholding.rc(suave)
temp2 = img.copy()
temp2[temp2 > T] = 255
temp2[temp2 < 255] = 0
temp2 = cv2.bitwise_not(temp2)

resultadoOtsu = np.vstack([
    np.hstack([img, suave]),
    np.hstack([temp, temp2])
])

cv2.imshow("Binarizacao com metodo Otsu Riddler-Calvard", resultadoOtsu)

cv2.waitKey(0)