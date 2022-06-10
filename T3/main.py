from re import I
import parametros as p
from logic import DFT, gaussian, ideal, inverse_DFT, butterworth, LP_gaussian
import cv2
import matplotlib.pyplot as plt
import numpy as np

# leemos imagen en escala de grises
img = cv2.imread(p.img[2], 0)
h,w = img.shape[0:2]
# aplicamos transformada y shift
tf = DFT(img)
for i in range(len(p.D0)):
    for j in range(len(p.D02)):
        butter_filter = butterworth(60, h, w, 2)
        gaussian_LP_filter = LP_gaussian(80, h, w)
        mult = tf*butter_filter
        mult1 = mult*gaussian_LP_filter
        inversa_mult1 = inverse_DFT(mult1)
        cv2.imwrite("2butterHP-" + str(p.D0[i])+ "-" + str(p.D02[j])+ ".png", inversa_mult1)
