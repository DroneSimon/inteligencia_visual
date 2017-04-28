import subsampling
import Blur
import cv2
import numpy as np
from os import listdir
import csv

class Muestreo:
    contador = 0
    n = 1
    numero = 1

    archivoCSV = open("train.csv","w")

    def leerDirectorio(self, directorio, columna, fila, id):
        for archivo in listdir(directorio):
            image = cv2.imread(directorio + archivo)
            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            v1 = Blur.aplicarDiferenciasGaussianas(image, columna, fila ,9,9,9,9,9,8)      ### ingresar X,Y + valor difuminado en primer gaussian     A,B + valor difuminado en segundo gaussian

            self.vectorizar(v1, id)



    def vectorizar(self, v1, dato):
        vector = np.resize(v1, (1, v1.size))
        vectorImage = np.concatenate((vector, dato), axis=1)
        self.crearCSV(vectorImage)
        #self.guardar(v1)
        print vectorImage


    def crearCSV(self, vector):
            writer = csv.writer(self.archivoCSV)
            writer.writerows(vector)
        #guarda la imagen editada
    def guardar(self, nueva):
        cv2.imwrite("fotos/escalar"+str(self.contador)+".jpg", nueva)
        self.contador = self.contador + 1



pr = Muestreo()

#pr.leerDirectorio('paquito/', 64, 64, [[1]])



pr.leerDirectorio('fuego/', 64, 64, [[1]])
pr.leerDirectorio('humo/', 64, 64, [[2]])
pr.leerDirectorio('bosque/', 64, 64, [[3]])


#pr.leerDirectorio('fuegoTest/', 64, 64, [[1]])
#pr.leerDirectorio('humoTest/', 64, 64, [[2]])
#pr.leerDirectorio('bosqueTest/', 64, 64, [[3]])


