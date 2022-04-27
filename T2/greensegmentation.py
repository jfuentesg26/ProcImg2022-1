import cv2
import parametros as p
import numpy as np
from auxfunc import RGB2CMYK

def HSV_green_segmentation(img_og, img_hsv):
    mask = cv2.inRange(img_hsv, p.umbrales['HSVlow'], p.umbrales['HSVhigh'])
    result = cv2.bitwise_and(img_og, img_og, mask=mask)
    return result

def HSL_green_segmentation(img_og, img_hsl):
    A_low = (img_hsl >= p.umbrales['HLSlow']).all(axis = 2).astype(np.uint8)
    A_high = (img_hsl <= p.umbrales['HLShigh']).all(axis = 2).astype(np.uint8)
    mask = np.logical_and(A_low, A_high).astype(np.uint8)
    result = cv2.bitwise_and(img_og, img_og, mask=mask)
    return result

def RGB_green_segmentation(img_og, img_rgb):
    A_low = (img_rgb >= p.umbrales['RGBlow']).all(axis = 2).astype(np.uint8)
    A_high = (img_rgb <= p.umbrales['RGBhigh']).all(axis = 2).astype(np.uint8)
    mask = np.logical_and(A_low, A_high).astype(np.uint8)
    result = cv2.bitwise_and(img_og, img_og, mask=mask)
    return result

def CMYK_green_segmentation(img_og, img_cmyk):
    A_low = (img_cmyk >= p.umbrales['CMYKlow']).all(axis = 2).astype(np.uint8)
    A_high = (img_cmyk <= p.umbrales['CMYKhigh']).all(axis = 2).astype(np.uint8)
    mask = np.logical_and(A_low, A_high).astype(np.uint8)
    result = cv2.bitwise_and(img_og, img_og, mask=mask)
    return result
    

# Cargamos imagen
img = cv2.imread(p.imagenes['img1'])
# cambios base de color a RGB, HSV, HSL, CMYK, LUV
img_RGB = img
img_HSV = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
img_HLS = cv2.cvtColor(img, cv2.COLOR_RGB2HLS)
img_CMYK = RGB2CMYK(img)

# obtenemos imagen segmentada
img_HSV_seg = HSV_green_segmentation(img, img_HSV)
img_RGB_seg = RGB_green_segmentation(img, img_RGB)
img_HSL_seg = HSL_green_segmentation(img, img_HLS)
img_CMYK_seg = CMYK_green_segmentation(img, img_CMYK)

# hacemos display de los resultados
# cv2.imshow('og', img)
# cv2.imshow('HSV', img_HSV_seg)
# cv2.imshow('RGB', img_RGB_seg)
# cv2.imshow('HSL', img_HSL_seg)
# cv2.imshow('CMYK', img_CMYK_seg)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
