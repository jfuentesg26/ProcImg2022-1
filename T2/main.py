from cv2 import cvtColor
from numpy import save
from auxfunc import RGB2CMYK
from greensegmentation import CMYK_green_segmentation, HSL_green_segmentation, \
                        HSV_green_segmentation, RGB_green_segmentation
from whitelinesegmentation import CMYK_white_segmentation, HSL_white_segmentation, \
                        HSV_white_segmentation, RGB_white_segmentation
from auxfunc import RGB2CMYK
import cv2
import parametros as p


# Cargamos imagen

def BGR2Bases(img):
    # cambios base de color a RGB, HSV, HSL, CMYK, LUV
    RGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    HLS = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)
    # CMYK = RGB2CMYK(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return [RGB, HSV, HLS]

def segmentar_blanca(lista, img):
    # obtenemos imagen segmentada en blanco
    HSV = HSV_white_segmentation(img, lista[1])
    RGB = RGB_white_segmentation(img, lista[0])
    HSL = HSL_white_segmentation(img, lista[2])
    # CMYK = CMYK_white_segmentation(img, lista[3])
    return [RGB, HSV, HSL]

def segmentar_verde(lista, img):
    # obtenemos imagen segmentada en verde
    HSV = HSV_green_segmentation(img, lista[1])
    RGB = RGB_green_segmentation(img, lista[0])
    HSL = HSL_green_segmentation(img, lista[2])
    # CMYK = CMYK_green_segmentation(img, lista[3])
    return [RGB, HSV, HSL]

def toBGR(LISTA):
    # cambios base de color a RGB, HSV, HSL, CMYK, LUV
    RGB = cv2.cvtColor(LISTA[0], cv2.COLOR_RGB2BGR)
    HSV = cv2.cvtColor(LISTA[1], cv2.COLOR_HSV2BGR)
    HLS = cv2.cvtColor(LISTA[2], cv2.COLOR_HLS2BGR)
    # CMYK = RGB2CMYK(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return [RGB, HSV, HLS]

def save_images(nombre, lista):
    for i in range (len(lista)):
        cv2.imwrite(nombre + "-" + str(i) + ".png", lista[i])

for i in range (1, 4):
    nombre = 'img' + str(i)
    img = cv2.imread(p.imagenes[nombre])
    lista = BGR2Bases(img)
    # lista = segmentar_blanca(img, lista)
    # save_images(nombre + 'white', toBGR(lista))
    # lista = segmentar_verde(img, lista)
    # save_images(nombre + 'green', toBGR(lista))