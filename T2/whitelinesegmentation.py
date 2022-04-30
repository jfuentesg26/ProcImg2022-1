import cv2
import parametros as p
import numpy as np
from auxfunc import RGB2CMYK, create_binary_img
from matplotlib import pyplot as plt

def HSV_white_segmentation(img_og, img_hsv):
    mask = cv2.inRange(img_hsv, p.umbrales_white['HSVlow'], p.umbrales_white['HSVhigh'])
    result = cv2.bitwise_and(img_og, img_og, mask=mask)
    return result

def HSL_white_segmentation(img_og, img_hsl):
    A_low = (img_hsl >= p.umbrales_white['HLSlow']).all(axis = 2).astype(np.uint8)
    A_high = (img_hsl <= p.umbrales_white['HLShigh']).all(axis = 2).astype(np.uint8)
    mask = np.logical_and(A_low, A_high).astype(np.uint8)
    result = cv2.bitwise_and(img_og, img_og, mask=mask)
    return result

def RGB_white_segmentation(img_og, img_rgb):
    A_low = (img_rgb >= p.umbrales_white['RGBlow']).all(axis = 2).astype(np.uint8)
    A_high = (img_rgb <= p.umbrales_white['RGBhigh']).all(axis = 2).astype(np.uint8)
    mask = np.logical_and(A_low, A_high).astype(np.uint8)
    result = cv2.bitwise_and(img_og, img_og, mask=mask)
    return result

def CMYK_white_segmentation(img_og, img_cmyk):
    A_low = (img_cmyk >= p.umbrales_white['CMYKlow']).all(axis = 2).astype(np.uint8)
    A_high = (img_cmyk <= p.umbrales_white['CMYKhigh']).all(axis = 2).astype(np.uint8)
    mask = np.logical_and(A_low, A_high).astype(np.uint8)
    result = cv2.bitwise_and(img_og, img_og, mask=mask)
    return result

def gaussian(img):
    w = np.array([[1,4,7,4,1], [4,16,26,16,4], [7,26,41,26,7], [4,16,26,16,4], [1,4,7,4,1]])
    w_1 = (1/273)*w
    smooth = cv2.filter2D(src=img, ddepth=-1, kernel=w_1)
    new_s = ((smooth - smooth.min()) * (1/(smooth.max() - smooth.min()) * 255)).astype('uint8')
    return new_s

def laplace(img):
    w_2 = np.array([[1,1,1], [1,-8,1], [1,1,1]])
    cw_1 = cv2.filter2D(src=img, ddepth=-1, kernel=w_2)
    new_cw1 = ((cw_1 - cw_1.min()) * (1/(cw_1.max() - cw_1.min()) * 255)).astype('uint8')
    return new_cw1


