from cv2 import cv2
import sys
import numpy as np

#LENDO, EXIBINDO E SALVANDO IMAGEM

# img = cv2.imread(cv2.samples.findFile("../imgs/road2.jpg"), cv2.IMREAD_UNCHANGED)
#
# if img is None:
#     sys.exit("Não há imagem")
#
# cv2.imshow("Display", img)
# k = cv2.waitKey(0)
#
# if k == ord("s"):
#     cv2.imwrite("../imgs/road2.png", img)

#LENDO, EXIBINDO E GRANDO VÍDEO

#LIGANDO A CÂMERA

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Não é possível abrir a câmera")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        print("Não pe possível receber os frames. Saindo...")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow("Camera", gray)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyALLWindow()

#LENDO VÍDEO

# cap = cv2.VideoCapture('../videos/VID_20220111_085052381.mp4')
#
# while cap.isOpened():
#     ret, frame = cap.read()
#
#     if not ret:
#         print("Não pe possível receber os frames. Saindo...")
#         break
#
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#
#     cv2.imshow("Camera", gray)
#
#     if cv2.waitKey(100) == ord('q'):
#         break
#
# cap.release()
# cv2.destroyALLWindow()

#SALVANDO VÍDEO

# cap = cv2.VideoCapture(0)
#
# fourcc = cv2.VideoWriter_fourcc(*'XVID') #Especifica o tipo de codificação para o vídeo (fourcc.org, para ver os formatos aceitos)
# out = cv2.VideoWriter('../videos/output.avi', fourcc, 20, (640, 480))
#
# while cap.isOpened():
#     ret, frame = cap.read()
#
#     if not ret:
#         print("Não pe possível receber os frames. Saindo...")
#         break
#     frame = cv2.flip(frame, 0) #Orienta os pícels na vertical
#
#     out.write(frame) #Salva os frames
#
#     cv2.imshow("Frame", frame)
#
#     if cv2.waitKey(1) == ord('q'):
#         break
#
# cap.release()
# out.release()
# cv2.destroyALLWindow()

#DESENHANDO NAS IMAGENS

# img = cv2.imread("../imgs/road2.jpg")
# blackImg = np.zeros((512, 512, 3), np.uint8) # Cria uma imagem preta
#
# cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (255, 0, 0), 5) #Linha
# cv2.rectangle(img, (50, 50), (img.shape[1] - 100, img.shape[0] - 50), (0, 255, 0), 3)
# cv2.circle(img, (img.shape[1]//2, img.shape[0]//2), 195, (255, 255, 255), 3)
# cv2.ellipse(img, (img.shape[1]//2, img.shape[0]//2), (200, 120), 0, 0, 90, 0, -1)
# cv2.ellipse(img, (img.shape[1]//2, img.shape[0]//2), (200, 120), 0, 180, 270, 0, -1)
#
# #Desenhando poligonos
#
# pts = np.array([[50, 20], [200, 20], [100, 50], [50, 28]], np.int32)
# pts = pts.reshape((-1, 1, 2))
#
# cv2.polylines(img, [pts], True, (255, 255, 255), 2)
#
# #Escrevenod na imagem
#
# cv2.putText(img, "OpenCV", (img.shape[1]//2, img.shape[0]//2), cv2.FONT_HERSHEY_SIMPLEX, 4, (255, 67,42), 3, cv2.LINE_AA)
#
# cv2.imshow("Linha", img)
# cv2.waitKey(0)

#UTILIZANDO O MOUSE COMO UM PINCEL

# events = [i for i in dir(cv2) if 'EVENT' in i] #Cria uma lista com as funções que o mouse executa
# print(events)
#
# def desenha_circulo(event, x, y, flags, param):
#     if event == cv2.EVENT_LBUTTONDBLCLK:
#         cv2.circle(img, (x, y), 100, (255, 0, 0), -1)
#
# img = np.zeros((512, 512, 3), np.uint8)
# cv2.namedWindow("Imagem")
# cv2.setMouseCallback("Imagem", desenha_circulo)
#
# while 1:
#     cv2.imshow("Imagem", img)
#     if cv2.waitKey(20) & 0xFF == ord('q'):
#         break
#
# cv2.destroyAllWindow()

#UTILIZANDO O MOUSE COMO UM PINCEL - AVANÇADO

# desenhar = False #Verdade se o mouse estiver pressionado
# mode = True #Se for verdade desenha um retangulo. Pressionadno m, faz uma curva
# ix, iy = -1, -1
#
# def desenha_circulo(event, x, y, flags, param):
#     global ix, iy, desenhar, mode
#
#     if event == cv2.EVENT_LBUTTONDOWN:
#         desenhar = True
#         ix, iy = x, y
#     elif event == cv2.EVENT_MOUSEMOVE:
#         if desenhar == True:
#             if mode == True:
#                 cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)
#             else:
#                 cv2.circle(img, (x, y), 5, (0, 0, 255), -1)
#     elif event == cv2.EVENT_LBUTTONUP:
#         desenhar = False
#         if mode == True:
#             cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)
#         else:
#             cv2.circle(img, (x, y), 5, (0, 0, 255), -1)
#
# img = np.zeros((512, 512, 3), np.uint8)
# cv2.namedWindow("Imagem")
# cv2.setMouseCallback("Imagem", desenha_circulo)
#
# while 1:
#     cv2.imshow("Imagem", img)
#     k = cv2.waitKey(1) & 0xFF
#
#     if k == ord('m'):
#         mode = not mode
#     elif k == ord('q'):
#         break
#
# cv2.destroyAllWindows()

#TRACKBAR COMO UMA PALETA DE CORES

# def nothing(x):
#     pass
#
# def desenha_circulo(event, x, y, flags, param):
#     if event == cv2.EVENT_LBUTTONDBLCLK:
#         cv2.circle(img, (x, y), raio, (b, g, r), -1)
#
# img = np.zeros((300, 512, 3), np.uint8)
# cv2.namedWindow('Imagem')
# cv2.setMouseCallback('Imagem', desenha_circulo)
#
# cv2.createTrackbar('R', 'Imagem', 0, 255, nothing)
# cv2.createTrackbar('G', 'Imagem', 0, 255, nothing)
# cv2.createTrackbar('B', 'Imagem', 0, 255, nothing)
# cv2.createTrackbar('Raio', 'Imagem', 0, 150, nothing)
#
# switch = '0 : OFF \n1 : ON'
# cv2.createTrackbar(switch, 'Imagem', 0, 1, nothing)
#
# while 1:
#     cv2.imshow('Imagem', img)
#     k = cv2.waitKey(1) & 0xFF
#     if k == ord('q'):
#         break
#
#     r = cv2.getTrackbarPos('R', 'Imagem')
#     g = cv2.getTrackbarPos('G', 'Imagem')
#     b = cv2.getTrackbarPos('B', 'Imagem')
#     s = cv2.getTrackbarPos(switch, 'Imagem')
#     raio = cv2.getTrackbarPos('Raio', 'Imagem')
#
#     if s == 0:
#         img[:] = 255
#
# cv2.destroyAllWindows()

# draw = False
#
# def nothing(x):
#     pass
#
# def desenhar(event, x, y, flags, param):
#     # global draw
#     # if event == cv2.EVENT_LBUTTONDOWN:
#     #     draw = True
#     # elif event == cv2.EVENT_MOUSEMOVE:
#     #     if draw == True:
#     #         cv2.circle(img, (x, y), raio, (b, g, r), -1)
#     # elif event == cv2.EVENT_LBUTTONUP:
#     #     draw = False
#     # else:
#     #     pass
#     if event == cv2.EVENT_LBUTTONDBLCLK:
#         draw = True
#         cv2.circle(img, (x, y), raio, (b, g, r), -1)
#
# def lendo_trackbar():
#     global r, g, b, s, raio
#
#     r = cv2.getTrackbarPos('R', 'Imagem')
#     g = cv2.getTrackbarPos('G', 'Imagem')
#     b = cv2.getTrackbarPos('B', 'Imagem')
#     s = cv2.getTrackbarPos(switch, 'Imagem')
#     raio = cv2.getTrackbarPos('Raio', 'Imagem')
#
#     return (r, g, b, s, raio)
#
# img = np.zeros((300, 512, 3), np.uint8)
# cv2.namedWindow('Imagem')
# cv2.setMouseCallback('Imagem', desenhar)
#
# cv2.createTrackbar('R', 'Imagem', 0, 255, nothing)
# cv2.createTrackbar('G', 'Imagem', 0, 255, nothing)
# cv2.createTrackbar('B', 'Imagem', 0, 255, nothing)
# cv2.createTrackbar('Raio', 'Imagem', 10, 70, nothing)
#
# switch = '0 : OFF \n1 : ON'
# cv2.createTrackbar(switch, 'Imagem', 0, 1, nothing)
#
# while 1:
#     cv2.imshow('Imagem', img)
#     k = cv2.waitKey(1) & 0xFF
#     if k == ord('q'):
#         break
#
#     lendo_trackbar()
#
#     if s == 0:
#         img[:] = 255
#         draw = False
#
# cv2.destroyAllWindows()