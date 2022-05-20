import numpy as np
from  scipy.fft import fft2,ifft2,fftshift,ifftshift
import matplotlib.pyplot as plt

# Pading manual
def padding_img(img):
    h, w = img.shape[0:2]
    h_pad = (h//2, h//2)
    w_pad = (w//2, w//2)
    pad_img = np.pad(img, (h_pad, w_pad), 'constant', constant_values=((0,0), (0,0)))
    return pad_img

# Centering manual
def centering(img):
    h,w = img.shape[0:2]
    x = np.ones((h,w),dtype=int)
    x[1::2,::2] = -1
    x[::2,1::2] = -1
    return img*x

# Distancia euclidiana
def D(x, y, cx, cy):
    return np.sqrt((x-cx)**2 + (y-cy)**2)

# Transformada de Fourier y centering
def DFT(img):
    img_dft = fft2(img)
    img_center = fftshift(img_dft)
    return img_center

# Transformada de Fourier inversa
def inverse_DFT(img):
    inverse_shift = ifftshift(img)
    inverse_transform = ifft2(inverse_shift)
    result = np.abs(inverse_transform)
    return result

# Filtro butterworth
def butterworth(D0, h, w, n):
    filter = np.ones((h,w))
    cy, cx = h/2, w/2
    for x in range(w):
        for y in range(h):
            filter[y, x] = 1/(1+(D0/D(x, y, cx, cy))**(2*n))
            if (x == w/2 and y == h/2):
                filter[y,x] = filter[y,x] + 0.2
    return filter

# Filtro Gaussiano
def gaussian(D0, h, w):
    filter = np.ones((h,w))
    cy, cx = h/2, w/2
    for x in range(w):
        for y in range(h):
            filter[y, x] = 1 - np.exp(((-D(x, y, cx, cy)**2)/(2*(D0**2))))
            if (x == w/2 and y == h/2):
                filter[y,x] = filter[y,x] + 0.2
    return filter

def LP_gaussian(D0, h, w):
    filter = np.ones((h,w))
    cy, cx = h/2, w/2
    for x in range(w):
        for y in range(h):
            filter[y, x] = np.exp(((-D(x, y, cx, cy)**2)/(2*(D0**2))))
    return filter

def ideal(img, D0, h, w):
    filter = np.ones((h,w))
    for x in range(w):
        for y in range(h):
            if img[y,x] <= D0:
                filter[y,x] = 0
    return filter

