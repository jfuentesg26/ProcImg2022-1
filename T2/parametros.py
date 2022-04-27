import numpy as np
import cv2
from auxfunc import RGB2CMYK

imagenes = {
    'img1': "../../ImagenesT2/Off side 1.png",
    'img2': "../../ImagenesT2/Off side 2.png",
    'img3': "../../ImagenesT2/Off side 3.png",
    'img4': "../../ImagenesT2/Off side 4.png",
    'img5': "../../ImagenesT2/Off side 5.png",
    'img6': "../../ImagenesT2/Off side 6.png",
}

umbrales = {
    'RGBlow': np.array([15, 100, 15]),
    'RGBhigh': np.array([90, 255, 120]),
    'HSVlow': (70, 100, 100),
    'HSVhigh': (80, 255, 255),
    'HLSlow': np.array([65, 40, 30]),
    'HLShigh': np.array([100, 220, 220]),
    'CMYKhigh': np.array([255, 160, 255, 160]),
    'CMYKlow': np.array([25, 0, 100, 0])
}

umbrales_white = {
    'RGBlow': np.array([250, 250, 250]),
    'RGBhigh': np.array([255, 255, 255]),
    'HSVlow': (0, 0, 200),
    'HSVhigh': (255, 55, 255),
    'HLSlow': np.array([0, 90, 0]),
    'HLShigh': np.array([255, 100, 255]),
    'CMYKhigh': np.array([10, 10, 10, 10]),
    'CMYKlow': np.array([0, 0, 0, 0])

}