import numpy as np
import cv2
import parametros as p
'''A = np.asarray([[20, 30, 40], [10, 10, 10]])
low = np.array([10, 15, 10])
high = np.array([30, 30, 40])
A_low = (A >= low).all(axis = 1).astype(int)
A_high = (A <= high).all(axis = 1).astype(int)
result = np.logical_and(A_low, A_high).astype(int)
print(result)'''

# img_og = cv2.imread(p.imagenes['img1'])
# img_rgb = cv2.cvtColor(img_og, cv2.COLOR_BGR2HSV)
# print(img_rgb.shape)
# print(img_rgb)
#    A_low = (img_rgb >= p.umbrales['RGBlow']).all(axis = 2).astype(np.uint8)
#    A_high = (img_rgb <= p.umbrales['RGBhigh']).all(axis = 2).astype(np.uint8)
#    mask = np.logical_and(A_low, A_high).astype(np.uint8)
#    result = cv2.bitwise_and(img_og, img_og, mask=mask)
#    print(result)

green = np.uint8([[[70,255,160]]])
hsv_green = cv2.cvtColor(green, cv2.COLOR_HSV2RGB)
print( hsv_green )

# print(cv2.cvtColor(frame, cv2.COLOR_HSV2RGB))