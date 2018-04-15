import cv2
import matplotlib.pyplot as plt 
import numpy as np

def increase_contrast(image_address):
	img = cv2.imread(image_address, 0)
	equaliser = cv2.equalizeHist(img)
	res = np.hstack(( equaliser, ))
	cv2.imwrite(image_address+'high_contrast.jpg', res)

def equaliseColored(image_address):
        img = cv2.imread(image_address)
        ycrcb = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB)
        channels = cv2.split(ycrcb)
        cv2.equalizeHist(channels[0], channels[0])
        cv2.merge(channels, ycrcb)
        cv2.cvtColor(ycrcb, cv2.COLOR_YCR_CB2BGR, img)
        cv2.imwrite(image_address+'high_contrast_color.jpg', img)

def sharpen(image_address):
        im = cv2.imread(image_address)
        kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
        im = cv2.filter2D(im, -1, kernel)
        cv2.imwrite(image_address+"sharpened.jpg", im)

def do_both(image_address):
        img = cv2.imread(image_address)
        ycrcb = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB)
        channels = cv2.split(ycrcb)
        cv2.equalizeHist(channels[0], channels[0])
        cv2.merge(channels, ycrcb)
        cv2.cvtColor(ycrcb, cv2.COLOR_YCR_CB2BGR, img)
        
        kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
        im = cv2.filter2D(img, -1, kernel)
        cv2.imwrite(image_address+"sstv_ready.jpg", im)
        
