import numpy as np

# codigo extraido de https://code.adonline.id.au/cmyk-in-python/
def RGB2CMYK(img):
    img = img.astype(float)/255
    # Extract channels
    with np.errstate(invalid='ignore', divide='ignore'):
        K = 1 - np.max(img, axis=2)
        C = (1-img[...,2] - K)/(1-K)
        M = (1-img[...,1] - K)/(1-K)
        Y = (1-img[...,0] - K)/(1-K)
    # Convert the input BGR image to CMYK colorspace
    CMYK = (np.dstack((C,M,Y,K)) * 255).astype(np.uint8)
    return CMYK

