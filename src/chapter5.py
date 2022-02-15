
from cv2 import cv2
import numpy as np

#WARP PERSPECTIVE

img = cv2.imread("../imgs/gato6.jpg")

width, height = 250, 245
#cv2.rectangle(img,(210, 5), (480,235), (0, 150,0), 1) #Retângulo criado para referenciar os pontos na imagem


pts1 = np.float32([[220, 5],[480, 5],[220, 250],[480, 250]])
pts2 = np.float32([[0, 0], [width, 0], [0, width], [width, height]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)
imgOutput = cv2.warpPerspective(img, matrix, (width, height))

recorte = img[5:250, 220:480]


cv2.imshow("Imagem", img)
cv2.imshow("Output", imgOutput)
cv2.imshow("Recorte", recorte)


cv2.waitKey(0)