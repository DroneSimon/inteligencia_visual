
import cv2
from Perceptron1 import predict
import numpy as np
import subsampling
import Blur


def generarImagenesVideo(video,tamx,tamy):

    cap = cv2.VideoCapture(video)
    i = 1
    while True:
        ret, frame = cap.read()
        i += 1
        #Probar cambiando el tiempo
        if i%5 ==0:

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            smallImage = Blur.aplicarDiferenciasGaussianas(gray, 64, 64, 9, 9, 4, 9, 9, 8)
            #==== matriz a vector ================================================================
            vector = np.resize(smallImage,(1,smallImage.size))
            vectorImage = np.concatenate(([[1]], vector), axis=1)

            pred = predict(vectorImage)
            lista = pred.tolist()
            peak = pred.max()

            neuron = lista.index(peak) + 1 #neuron activado y buscado en la lista
            rojo = 0
            azul = 0
            verde = 0

            if peak > 0.7:

                if neuron == 1:
                    titulo = "FUEGO"
                    rojo = 255
                else:
                    if neuron == 2:
                        titulo = "ALERTA"
                        verde = 255
                    else:
                        titulo = ""
                        azul = 255
            else:
                titulo = " "

            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(frame, titulo ,(19,90), font, 2, (azul,verde,rojo),5)
            #cv2.imshow("nitidaGris", gray)
            cv2.imshow("original", frame)
            k = cv2.waitKey(90)
            if k == 90:
                break
    cv2.destroyAllWindows()


def pintarFuego(frame, font):
    cv2.putText(frame, "FUEGO", (19, 90), font, 2, (0, 0, 255), 5)

def pintarAlerta(frame, font):
    cv2.putText(frame, "ALERTA", (19, 90), font, 2, (0, 255, 0), 5)

def pintarAnomalia(frame, font):
    cv2.putText(frame, "", (19, 90), font, 2, (255, 0, 0), 5)

dir = 'fuego.mp4'

generarImagenesVideo(dir,64,64)
