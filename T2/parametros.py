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
    'RGBlow': np.array([250, 250, 250]),
    'RGBhigh': np.array([255, 255, 255]),
    'HSVlow': np.array([0, 0, 0]),
    'HSVhigh': np.array([91, 88, 255]),
    'HLSlow': np.array([0, 90, 0]),
    'HLShigh': np.array([255, 100, 255])

}