import numpy as np
import cv2
from auxfunc import RGB2CMYK

imagenes = {
    'img1': "../../ImagenesT2/Off side 1.png",
    'img2': "../../ImagenesT2/Off side 2.png",
    'img3': "../../ImagenesT2/Off side 3.png",
    'img4': "../../ImagenesT2/Off side 4.jpg",
    'img5': "../../ImagenesT2/Off side 5.jpg",
    'img6': "../../ImagenesT2/Off side 6.jpg",
}

umbrales = {
    'RGBlow': np.array([0, 90, 0]),
    'RGBhigh': np.array([106, 255, 82]),
    'HSVlow': (30, 40, 40),
    'HSVhigh': (70, 255, 160),
    'HLSlow': np.array([42, 40, 29]),
    'HLShigh': np.array([85, 201, 205])
}

umbrales_white = {
    'RGBlow': np.array([110, 126, 107]),
    'RGBhigh': np.array([255, 255, 255]),
    'HSVlow': np.array([44, 22, 138]),
    'HSVhigh': np.array([130, 148, 255]),
    'HLSlow': np.array([46, 115, 28]),
    'HLShigh': np.array([111, 255, 185])

}