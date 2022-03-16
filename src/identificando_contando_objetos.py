
from cv2 import cv2
import numpy as np
import mahotas

def escrever(img, texto, cor=(255, 0, 0)):
    fonte = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img, texto, ((img.shape[1]//2) - 100, img.shape[0] - 15), fonte, 0.5, cor, 0, cv2.LINE_AA)

imgColorida = cv2.resize(cv2.imread("../imgs/shapes.png"), (550, 350)) #Carregamento da imagem
imgGray = cv2.cvtColor(imgColorida, cv2.COLOR_BGR2GRAY) #converte para cinza
imgBlur = cv2.blur(imgGray, (7, 7))  #aplicação de blur para remover ruído e facilitar a identificação de bordas (suavização da imagem)

#BINARIZAÇÃO DA IMAGEM

#BINARIZAÇÃO COM LIMIAR

#(T, bin) =cv2.threshold(imgBlur, 235, 255, cv2.THRESH_BINARY)
#(T, bin) =cv2.threshold(imgBlur, 235, 255, cv2.THRESH_BINARY_INV)

#OBSERVAÇÃO: não é o método mais adequado, tendo em vista que é necessário alterar o thresh (limiar) manualmente para verificar se
# a conversão de tons de cinza para preto e branco foi feito de forma adequado, entretatno, com ele foi possível a identificação
# dos contornos de forma satisfatória, já que ele consegue captar todos os tons de cinza, até os mais claros, o que não é possível
# com outros métodos, principalmente quando há objetos de cor amarelo claro.

#FILTRO DE OTSU

# T = mahotas.thresholding.otsu(imgBlur) #aplicando o filtro otsu para binarização da imagem
# bin = imgBlur.copy()
#
# bin[bin > T] = 255
# bin[bin < 255] = 0
# bin = cv2.bitwise_not(bin)

#FILTRO DE RIDDLER-CALVARD

# T = mahotas.thresholding.rc(imgBlur) #aplicando o filtro otsu para binarização da imagem
# bin = imgBlur.copy()
#
# bin[bin > T] = 255
# bin[bin < 255] = 0
# bin = cv2.bitwise_not(bin)

#OBSERVAÇÃO: ambos os filtros são muito bons para detecção de bordas, mas há um certo problema na detecção de cores mais claras,
# como no caso do amarelo, que eles passam a ignorar e consideram apenas as cores mais escuras

#THRESHOLD ADAPTATIVO

bin = cv2.adaptiveThreshold(imgBlur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 17, 5)

#OBSERVAÇÃO: esse método determina o valor de threshold (limiar) matematicamente a partir do valor da janela/caixa de cálculo
# para que o limiar seja calculado nos pixels pŕoximos das imagens. Um excelente método para detecção de bordas, mas depende do
# valor do tamanho do bloco

imgCanny = cv2.Canny(bin, 70, 200) #aplicação de filtro para identificação de bordas

(objetos, lixo) = cv2.findContours(imgCanny.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) #lixo recebe dados que não serão utilizados

escrever(imgGray, "Imagens em tons de cinza", 0) #Chamando a função escrever
escrever(imgBlur, "Suavizacao com Blur", 0)
escrever(bin, "Binarizacao", 255)
escrever(imgCanny, "Detector de bordas Canny", 255)

temp = np.vstack([
    np.hstack([imgGray, imgBlur]),
    np.hstack([bin, imgCanny])
])

cv2.imshow("Quantidade de objetos: " + str(len(objetos)), temp)
cv2.waitKey(0)

imgC2 = imgColorida.copy()
cv2.imshow("Imagem Original", imgColorida)

cv2.drawContours(imgC2, objetos, -1, 0, 2)
escrever(imgC2, str(len(objetos)) + " objetos encontrados!", 0)
cv2.imshow("Contornos na imagem", imgC2)

cv2.waitKey(0)