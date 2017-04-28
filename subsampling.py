import numpy as np
import cv2


def escalar(image, columRes, filaRes):

    altura, anchura = image.shape[:2]
    saltos_fila = int(round(altura / (filaRes)))
    saltos_colum = int(round(anchura / (columRes)))
    imagen_adaptada = cv2.resize(image, (int(saltos_colum * columRes), int(saltos_fila * filaRes)))
    imagen_subsampling = aplicar_subsampling(imagen_adaptada, saltos_fila, saltos_colum)
    imagen_res = np.array(imagen_subsampling)
    return imagen_res

def aplicar_subsampling(imagen, saltos_fila, saltos_colum):  #saltosfila y saltoscolumna son el kernel

    matriz_res = []
    altura, anchura = imagen.shape[:2]
    for i in range(0, altura - 1, saltos_fila):
        fila_res = []
        for j in range(0, anchura - 1, saltos_colum):
            submat = imagen[i:i + saltos_fila, j:j + saltos_colum]
            valor_promedio = round(submat.sum() / (saltos_colum * saltos_fila), 0)
            val = int(valor_promedio)
            fila_res.append(val)
        matriz_res.append(fila_res)
    return matriz_res

imagen = cv2.imread('img1.jpg')
#v1 = np.array(imagen)
