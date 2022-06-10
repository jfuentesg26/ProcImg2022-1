from unittest import result
import cv2
import parametros as p
import numpy as np
from matplotlib import pyplot as plt
from greensegmentation import HSV_with_opening

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

def create_binary_img(img_gray):
    c = (img_gray > 120).astype(np.uint8)
    c = c*255
    return c

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


img = cv2.imread('img/gray1white.png', 0)
img = laplace(gaussian(img))
cv2.imwrite('final.png', img)

# img_RGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# img_HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# img_HLS = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)
# img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# RGB = cv2.cvtColor(RGB_white_segmentation(img, img_RGB), cv2.COLOR_RGB2BGR)
# HSV = cv2.cvtColor(HSV_white_segmentation(img, img_HSV), cv2.COLOR_HSV2BGR)
# HSL = cv2.cvtColor(HSL_white_segmentation(img, img_HLS), cv2.COLOR_HLS2BGR)
# gray = create_binary_img(img_gray)

# cv2.imwrite('RGB3white.png', RGB)
# cv2.imwrite('HSV3white.png', HSV)
# cv2.imwrite('HSL3white.png', HSL)
# cv2.imwrite('gray1white.png', gray)