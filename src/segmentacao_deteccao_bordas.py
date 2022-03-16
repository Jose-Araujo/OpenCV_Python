
import numpy as np
from cv2 import cv2

img = cv2.resize(cv2.imread('../imgs/road3.jpeg'), (540, 380))
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#FILTRO SOBEL

# sobelX = cv2.Sobel(img, cv2.CV_64F, 1, 0)
# sobelY = cv2.Sobel(img, cv2.CV_64F, 0, 1)
# sobelX = np.uint8(np.absolute(sobelX))
# sobelY = np.uint8(np.absolute(sobelY))
# sobel = cv2.bitwise_or(sobelX, sobelY)
#
# resultadoSobel = np.vstack([
#     np.hstack([img, sobelX]),
#     np.hstack([sobelY, sobel])
# ])
#
# cv2.imshow("Sobel", resultadoSobel)

#FILTRO LAPLACIANO

# lap = cv2.Laplacian(img, cv2.CV_64F)
# lap = np.uint8(np.absolute(lap))
#
# resultadoLaplaciano = np.vstack([img, lap])
#
# cv2.imshow("Laplaciano", resultadoLaplaciano)

#DETECTOR DE BORDAS CANNY

suave = cv2.GaussianBlur(img, (7, 7), 0)

canny1 = cv2.Canny(suave, 20, 120)
canny2 = cv2.Canny(suave, 70, 300)

resultadoCanny = np.vstack([
    np.hstack([img, suave]),
    np.hstack([canny1, canny2])
])

cv2.imshow("Canny", resultadoCanny)

cv2.waitKey(0)