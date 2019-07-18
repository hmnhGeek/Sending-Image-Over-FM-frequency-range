import cv2
import matplotlib.pyplot as plt 
import numpy as np

def equaliseColored(image_address):
    print("[SSTV SuperDoer]: Generating high contrast image...")
    img = cv2.imread(image_address)
    ycrcb = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB)
    channels = cv2.split(ycrcb)
    cv2.equalizeHist(channels[0], channels[0])
    cv2.merge(channels, ycrcb)
    cv2.cvtColor(ycrcb, cv2.COLOR_YCR_CB2BGR, img)
    return img

def sharpen(image_address):
    print("[SSTV SuperDoer]: Generating sharpened image...")
    im = cv2.imread(image_address)
    kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
    im = cv2.filter2D(im, -1, kernel)
    return im

def save(array, name):
    cv2.imwrite(name, array)

def manipulate(image_address):
    print("[SSTV SuperDoer]: Generating sharpened and high contrast image...")
    img = cv2.imread(image_address)
    ycrcb = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB)
    channels = cv2.split(ycrcb)
    cv2.equalizeHist(channels[0], channels[0])
    cv2.merge(channels, ycrcb)
    cv2.cvtColor(ycrcb, cv2.COLOR_YCR_CB2BGR, img)
    
    kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
    im = cv2.filter2D(img, -1, kernel)
    return im
