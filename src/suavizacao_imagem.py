
from cv2 import cv2
import numpy as np

img = cv2.imread("../imgs/Lenna.png")
img = img[::2, ::2]

#SUAVIZAÇÃO POR CÁLCULO MÉDIO UTILIZANDO A FUNÇÃO cv2.blur()
#
# suavizacaoBlur = np.vstack([
#     np.hstack([img, cv2.blur(img, (3, 3))]),
#     np.hstack([cv2.blur(img, (5, 5)), cv2.blur(img, (7, 7))]),
#     np.hstack([cv2.blur(img, (9, 9)), cv2.blur(img, (11, 11))])
# ])
# cv2.imshow("Imagens suavizadas (Blur)", suavizacaoBlur)

#SUAVIZAÇÃO PELA GAUSSIANA UTILIZANDO A FUNÇÃO cv2.GaussianBlur()

suavizacaoGaussiana = np.vstack([
    np.hstack([img, cv2.GaussianBlur(img, (3, 3), 0), cv2.GaussianBlur(img, (5, 5), 0)]),
    np.hstack([cv2.GaussianBlur(img, (7, 7), 0), cv2.GaussianBlur(img, (9, 9), 0), cv2.GaussianBlur(img, (11, 11), 0)])
])
cv2.imshow("Imagens suavizadas (Gaussiana)", suavizacaoGaussiana)

#SUAVIZAÇÃO PELA MEDIANA UTILIZANDO A FUNÇÃO cv2.medianBlur()

# suavizacaoMediaBlur = np.vstack([
#     np.hstack([img, cv2.medianBlur(img, 3)]),
#     np.hstack([cv2.medianBlur(img, 5), cv2.medianBlur(img, 7)]),
#     np.hstack([cv2.medianBlur(img, 9), cv2.medianBlur(img, 11)])
# ])
# cv2.imshow("Imagens suavizadas (Mediana)", suavizacaoMediaBlur)

#SUAVIZAÇÃO COM FILTRO BILATERAL UTILIZANDO A FUNÇÃO cv2.bilateralFilter()

# suavizacaoBilateral = np.vstack([
#     np.hstack([img, cv2.bilateralFilter(img, 3, 21, 21)]),
#     np.hstack([cv2.bilateralFilter(img, 5, 35, 35), cv2.bilateralFilter(img, 7, 49, 49)]),
#     np.hstack([cv2.bilateralFilter(img, 9, 63, 63), cv2.bilateralFilter(img, 11, 77, 77)])
# ])
# cv2.imshow("Imagens suavizadas (Bilateral)", suavizacaoBilateral)

cv2.waitKey(0)