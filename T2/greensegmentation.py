from unittest import result
import cv2
import parametros as p
import numpy as np

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


def HSV_with_opening(img, HSV):
    mask = cv2.inRange(HSV, p.umbrales['HSVlow'], p.umbrales['HSVhigh'])
    kernel1 = np.ones((3,3),np.uint8)
    kernel2 = np.ones((5,5),np.uint8)
    kernel3 = np.ones((7,7),np.uint8)
    opening1 = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel1)
    opening2 = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel2)
    opening3 = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel3) 
    result1 = cv2.bitwise_and(img, img, mask=opening1)
    result2 = cv2.bitwise_and(img, img, mask=opening2)
    result3 = cv2.bitwise_and(img, img, mask=opening3)
    # cv2.imwrite('op1.png', result1)
    # cv2.imwrite('op2.png', result2)
    cv2.imwrite('op3.png', result3)



img = cv2.imread(p.imagenes['img3'])

# img_RGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# img_HLS = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)
HSV_with_opening(img, img_HSV)
# RGB = cv2.cvtColor(RGB_green_segmentation(img, img_RGB), cv2.COLOR_RGB2BGR)
# HSV = cv2.cvtColor(HSV_green_segmentation(img, img_HSV), cv2.COLOR_HSV2BGR)
# HSL = cv2.cvtColor(HSL_green_segmentation(img, img_HLS), cv2.COLOR_HLS2BGR)


