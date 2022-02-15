
from cv2 import cv2

#print("Package Imported")

#READ: IMAGES - VIDEOS - WEBCAM
'''
img = cv2.imread("../imgs/gato8.jpeg") #Lê uma imagem do computador

cv2.imshow("Output", img) #Exibi a imagem 
cv2.waitKey(0) #Delay
'''

'''
cap = cv2.VideoCapture("../videos/VID_20220111_085052381.mp4") #Lê um vídeo do computador

while True:                         # Como um vídeo é uma sequência de imagens é necessário criar um loop para mostrar todas as imgaens
    success, img = cap.read()       #Nessa função eu faço a leitura do vídeo, armazeno a imagem em img, a var success indica se fooi armazenado (T/F)
    cv2.imshow("Video", img)        #Mostro a imagem
    if cv2.waitKey(15) & 0xFF == ord('q'):  #Condição para fechar a janela
        break
'''


cap = cv2.VideoCapture(0) #Acessa a câmera nativa do notebook
cap.set(3, 640) #Define a largura da imagem
cap.set(4, 480) #Define a altura da imagem
cap.set(10, 100) #Altera a luminosidade do vídeo

while True:
    success, img = cap.read()
    cv2.imshow("Camera", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break