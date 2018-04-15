from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack as fftpack
import scipy.misc
import cv2

def shiftedFT(image_address):
	"""Generates the Shifted Fourier Transform of the image."""
	img = Image.open(image_address)
	img1 = img.convert('L') # convert image to black and white
	f = np.fft.fft2(img1)
	fshift = np.fft.fftshift(f)
	magnitude = 20*np.log(np.abs(fshift))
	scipy.misc.imsave(image_address+"shifted_magnitude.png", magnitude)
	plt.subplot(111),plt.imshow(magnitude, cmap = 'gray')
	plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
	plt.show()


def normalFT(image_address):
	"""Generates the Normal Fourier Transform of the image."""
	img = Image.open(image_address)
	img1 = img.convert('L') # convert image to black and white
	f = np.fft.fft2(img1)
	magnitude = 20*np.log(np.abs(f))
	scipy.misc.imsave(image_address+"magnitude.png", magnitude)
	plt.subplot(111),plt.imshow(magnitude, cmap = 'gray')
	plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
	plt.show()


def phaseSpectrum(image_address):
	"""Generates the Phase Spectrum the image."""
	img = Image.open(image_address)
	img1 = img.convert('L')
	f = np.fft.fft2(img1)
	fshift = np.fft.fftshift(f)
	phase = np.angle(fshift)
	scipy.misc.imsave(image_address+"phase.png", magnitude)
	plt.subplot(111), plt.imshow(phase, cmap='gray')
	plt.title("Phase Spectrum"), plt.xticks([]), plt.yticks([])
	plt.show()

def save_transform(image_address):
	"""Generates the .npy of FT."""
	img = Image.open(image_address)
	img1 = img.convert('L') # convert image to black and white
	f = np.fft.fft2(img1)
	fshift = np.fft.fftshift(f)

	np.save(image_address+"fourier", fshift)

def all(image_address):
	"""Generates the Shifted Fourier Transform and the phase spectrum of the image."""
	img = Image.open(image_address)
	img1 = img.convert('L') # convert image to black and white
	f = np.fft.fft2(img1)
	fshift = np.fft.fftshift(f)
	magnitude = 20*np.log(np.abs(fshift))
	phase = np.angle(fshift)
	scipy.misc.imsave(image_address+"shifted_magnitude.png", magnitude)
	scipy.misc.imsave(image_address+"phase.png", phase)
	plt.subplot(211),plt.imshow(magnitude, cmap = 'gray')
	plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
	plt.subplot(212),plt.imshow(phase, cmap = 'gray')
	plt.title('Phase Spectrum'), plt.xticks([]), plt.yticks([])
	plt.show()

def hpf(image_address):
	"""Generates the High frequency content of the image."""
	img = cv2.imread(image_address, 0)
	f = np.fft.fft2(img)
	fshift = np.fft.fftshift(f)
	rows, cols = img.shape
	crow,ccol = rows/2 , cols/2
	fshift[crow-30:crow+30, ccol-30:ccol+30] = 0
	f_ishift = np.fft.ifftshift(fshift)
	img_back = np.fft.ifft2(f_ishift)
	img_back = np.abs(img_back)
	scipy.misc.imsave(image_address+"hpf.png", img_back)
	plt.subplot(121),plt.imshow(img, cmap = 'gray')
	plt.title('Input Image'), plt.xticks([]), plt.yticks([])
	plt.subplot(122),plt.imshow(img_back, cmap = 'gray')
	plt.title('Image after HPF'), plt.xticks([]), plt.yticks([])

	plt.show()

def lpf(image_address):
	"""Generates the Low frequency content of the image."""
	img = cv2.imread(image_address, 0)

	dft = cv2.dft(np.float32(img),flags = cv2.DFT_COMPLEX_OUTPUT)
	dft_shift = np.fft.fftshift(dft)
	rows, cols = img.shape
	crow,ccol = rows/2 , cols/2

	# create a mask first, center square is 1, remaining all zeros
	mask = np.zeros((rows,cols,2),np.uint8)
	mask[crow-30:crow+30, ccol-30:ccol+30] = 1

	# apply mask and inverse DFT
	fshift = dft_shift*mask
	f_ishift = np.fft.ifftshift(fshift)
	img_back = cv2.idft(f_ishift)
	img_back = cv2.magnitude(img_back[:,:,0],img_back[:,:,1])
	scipy.misc.imsave(image_address+"lpf.png", img_back)
	plt.subplot(121),plt.imshow(img, cmap = 'gray')
	plt.title('Input Image'), plt.xticks([]), plt.yticks([])
	plt.subplot(122),plt.imshow(img_back, cmap = 'gray')
	plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
	plt.show()
