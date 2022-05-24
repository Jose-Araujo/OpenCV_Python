
from matplotlib import pyplot as plt
from cv2 import cv2
import numpy as np

##################################
#   Nessa execução surgiu um erro:
#
#   UserWarning: Matplotlib is currently using agg, which is a non-GUI backend, so cannot show the figure.
#
#   Solução, usar o comando direto no terminal: sudo apt-get install python3-tk
#
#   Esse comando irá instalar algumas dependências do matplotlib e solucionará o erro
##################################

#Função calcHist para calcular o hisograma da imagem

# img = cv2.imread('../imgs/Lenna.png')
# img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow("Imagem P&B", img)

# h = cv2.calcHist([img], [0], None, [256], [0, 256])
# plt.figure()                      #plota uma figura
# plt.title("Histograma P&B")       #titulo do histograma
# plt.xlabel("Intensidade")         #legenda do eixo x
# plt.ylabel("Qtde de Pixels")      #legenda do eixo y
# plt.plot(h)                       #histograma em linhas
# plt.xlim([0, 256])                #escala do eixo x
# #plt.hist(img.ravel(), 256, [0, 256]) #Outra maneira de plotar o histograma (em barras)
# plt.show()
##################################

#Histograma da imagem colorida

# img2 = cv2.imread('../imgs/Lenna.png')
# cv2.imshow("Colorida", img2)
#
# #Separando os canais
#
# canais = cv2.split(img2)
# cores = ("b", "g", "r")
#
# plt.figure()
# plt.title("Histograma Colorido")
# plt.xlabel("Intensidade")
# plt.ylabel("Número de Pixels")

# for (canal, cor) in zip(canais, cores):
#     # zip cria uma lista de tuplas formada pelas união das listas passadas e não tem nada a ver
#     #com um processo de compactação como poderia se esperar
#     hist = cv2.calcHist([canal], [0], None, [256], [0, 256])
#     plt.plot(hist, cor)
#     plt.xlim([0, 256])
# plt.show()
##################################

#Equalização de Histograma

img = cv2.imread('../imgs/Lenna.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
h_eq = cv2.equalizeHist(img)

cv2.imshow("Original", img)
cv2.imshow("Equalizada", h_eq)

plt.figure()
plt.title("Histograma Equalizado")
plt.xlabel("Intensidade")
plt.ylabel("Qtde de Pixels")
plt.hist(h_eq.ravel(), 256, [0, 256])
plt.xlim([0, 256])
plt.show()

plt.figure()
plt.title("Histograma Original")
plt.xlabel("Intensidade")
plt.ylabel("Qtde de Pixels")
plt.hist(img.ravel(), 256, [0, 256])
plt.xlim([0, 256])
plt.show()

#Exemplo da OpenCV

# hist, bins = np.histogram(img.flatten(), 256, [0, 256])
#
# cdf = hist.cumsum()
# cdf_normalized = cdf * hist.max()/cdf.max()
#
# plt.plot(cdf_normalized, color = 'b')
# plt.hist(img.flatten(), 256, [0, 256], color = 'r')
# plt.xlim([0,256])
# plt.legend(('cdf','histogram'), loc = 'upper left')
# plt.show()
#
# cdf_m = np.ma.masked_equal(cdf, 0)
# cdf_m = (cdf_m - cdf_m.min())*255/(cdf_m.max() - cdf_m.min())
# cdf = np.ma.filled(cdf_m, 0).astype('uint8')
#
# img2 = cdf[img]
#
# plt.plot(cdf, color = 'b')
# plt.hist(img.flatten(), 256, [0, 256], color = 'r')
# plt.xlim([0,256])
# plt.legend(('cdf','histogram'), loc = 'upper left')
# plt.show()


cv2.waitKey(0)