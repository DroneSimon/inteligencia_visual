import numpy as np
import cv2

def aplicarBlur(imagen,tamx,tamy,kernelx,kernely):
    grayImagen = adaptarImagen(imagen,tamx,tamy)
    blurImage = cv2.blur(grayImagen,(kernelx,kernely))
    smallImage = cv2.resize(blurImage,(tamx,tamy))
    return smallImage

def aplicarMedianBlur(imagen,tamx,tamy,difuminado):
    grayImagen = adaptarImagen(imagen,tamx,tamy)
    medianBlurImage = cv2.medianBlur(grayImagen,difuminado)
    smallImage = cv2.resize(medianBlurImage,(tamx,tamy))
    return smallImage

def aplicarGaussianBlur(imagen,tamx,tamy,kernelx,kernely,difuminado):
    grayImagen = adaptarImagen(imagen, tamx, tamy)
    gaussianBlurImage = cv2.GaussianBlur(grayImagen, (kernelx,kernely),difuminado)
    smallImage = cv2.resize(gaussianBlurImage, (tamx,tamy))
    return  smallImage
#bordes
def aplicarDiferenciasGaussianas(imagen, tamx, tamy, kerAX, kerAY, difA, kerBX, kerBY, difB):
    grayImage = adaptarImagen(imagen, tamx, tamy)
    image1 = cv2.GaussianBlur(grayImage, (kerAX,kerAY), difA)
    image2 = cv2.GaussianBlur(grayImage, (kerBX, kerBY), difB)
    imagenRes = image2 - image1
    imagenRes = cv2.resize(imagenRes, (tamx, tamy))
    return  imagenRes

def aplicarLaplacian(imagen, tamx, tamy, valorLap):
    grayImage = adaptarImagen(imagen, tamx, tamy)
    imagenRes = cv2.Laplacian(grayImage, valorLap)
    imagenRes = cv2.resize(imagenRes, (tamx, tamy))
    return imagenRes

def aplicarCanny(imagen, tamx, tamy, x, y):
    grayImage = adaptarImagen(imagen, tamx, tamy)
    imagenRes = cv2.Canny(grayImage, x, y)
    return imagenRes

#ruido

def aplicarMorfologiaDilate(imagen, tamx, tamy, kernelX, kernelY, iterationsValor):
    grayImage = adaptarImagen(imagen, tamx,tamy)
    kernel = np.ones((kernelX, kernelY), np.uint16)
    imagenRes = cv2.dilate(grayImage,kernel,iterations=iterationsValor)
    return imagenRes

def aplicarMorfologiaErode(imagen, tamx, tamy, kernelX, kernelY, iterationsValor):
    grayImage = adaptarImagen(imagen, tamx, tamy)
    kernel = np.ones((kernelX, kernelY), np.uint16)
    imagenRes = cv2.erode(grayImage, kernel, iterations=iterationsValor)
    return imagenRes

def aplicarMorfologiaGradiente(imagen, tamx, tamy, kernelDilX, kernelDilY, kernelEroX, kernelEroY, iterationsVal):
    grayImage = adaptarImagen(imagen, tamx, tamy)
    kernelDilate = np.ones((kernelDilX, kernelDilY), np.uint16)
    imagenDilate = cv2.dilate(grayImage,kernelDilate,iterations=iterationsVal)
    kernelErode = np.ones((kernelEroX, kernelEroY), np.uint16)
    imagenErode = cv2.erode(grayImage, kernelErode, iterations=iterationsVal)
    imagenRes = imagenDilate - imagenErode
    return imagenRes


def adaptarImagen(imagen,columnaResx,filaResy):
    altura, anchura = imagen.shape[:2]
    saltos_fila = int(round(altura / (filaResy)))
    saltos_colum = int(round(anchura / (columnaResx)))
    image = cv2.resize(imagen, (int(saltos_colum * columnaResx), int(saltos_fila * filaResy)))
    return image

###sobel
###laplce
###canny
