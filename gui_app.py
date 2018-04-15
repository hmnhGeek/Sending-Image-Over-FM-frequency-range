from Tkinter import *
import ttk
from tkFileDialog import *
from ImageManipulator import ImageManipulator
import matplotlib.pyplot as plt 
from PIL import Image, ImageTk
import numpy as np
import cv2
import os
import tkMessageBox
# from ImgFit import ImgFit
from spectrum import spectrum
from imageFit import imageFit
import scipy.misc

buttonBackground = "#D0D3D4"
buttonBackground_active = "#FDFEFE"

class Page(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)

    def show(self):
        self.lift()


# define pages here which inherit from page class. Below is an example page.
class examplePage(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

class fftPage(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        backGROUND = "#979A9A"
        self.config(bg=backGROUND)

        self.heading = Label(self, text="Magnitude Spectrum", bg=backGROUND, fg="white", 
        	font=("Arial", 15)).pack(pady=5)
        self.magnitude = Label(self)
        self.magnitude.pack()

        self.save_image = Button(self, text="Save Spectrum", command = self.save_spectrum,
			bg=buttonBackground, activebackground=buttonBackground_active, width=15)
        self.save_image.pack(pady=10)

        self.goback = Button(self, text="Go Back", command = lambda:hp.show(),
			bg=buttonBackground, activebackground=buttonBackground_active, width=15)
        self.goback.pack(pady=10)

    def save_spectrum(self):
    	mag, phase = spectrum.completeFourier(currentImage)
    	address_to_loc = asksaveasfile()
    	scipy.misc.imsave(address_to_loc.name, mag)

    def updatefft(self):
		best_width = 400
		best_height = 300

		mag, phase = spectrum.completeFourier(currentImage)

		icon1 = imageFit.fit(Image.fromarray(mag), best_height, best_width)

		self.magnitude.image=icon1
		self.magnitude.configure(image=icon1)

class SSTVGenPage(Page):
	def __init__(self, *args, **kwargs):
		Page.__init__(self, *args, **kwargs)
		backGROUND = "#979A9A"
		self.config(bg=backGROUND)

		self.CheckVar1 = IntVar()
		self.CheckVar2 = IntVar()
		C1 = Checkbutton(self, text = "Sharpen", variable = self.CheckVar1, \
		                 onvalue = 1, offvalue = 0, \
		                 width = 20, \
			bg=backGROUND, activebackground=backGROUND, bd=0, fg="#424949", activeforeground="#F2F3F4")
		C2 = Checkbutton(self, text = "Increase Contrast", variable = self.CheckVar2, \
		                 onvalue = 1, offvalue = 0, \
		                 width = 20, \
		                 bg=backGROUND, activebackground=backGROUND, bd=0, fg="#424949", activeforeground="#F2F3F4")
		C1.pack(pady=10)
		C2.pack(pady=10)

		self.var = IntVar()
		R1 = Radiobutton(self, text="Robot36", variable=self.var, value=1, command=self.submit,
			bg=backGROUND, activebackground="#95A5A6", width=20, bd=0, fg="#424949", activeforeground="#F2F3F4")
		R1.pack(pady=10)

		R2 = Radiobutton(self, text="PD240", variable=self.var, value=2, command=self.submit,
			bg=backGROUND, activebackground=backGROUND, width=20, bd=0, fg="#424949", activeforeground="#F2F3F4")
		R2.pack(pady=10)

		self.goback = Button(self, text="Go Back", command = lambda:hp.show(),
			bg=buttonBackground, activebackground=buttonBackground_active)
		self.goback.pack(pady=10)

		# adding original image as label
		self.ImageLabel = Label(self)
		self.ImageLabel.pack(pady=10)

	def updateLabel(self):
		# try:
		best_height=200
		best_width=400
		img = Image.open(currentImage)
		w, h = img.size
		aspect_ratio = w*h**(-1)

		if h >= w:
		    newWidth = int(aspect_ratio*best_height)
		    img = img.resize((newWidth,best_height), Image.ANTIALIAS)
		else:
		    newHeight = int(best_width*aspect_ratio**(-1))
		    img = img.resize((best_width,newHeight), Image.ANTIALIAS)

		icon = ImageTk.PhotoImage(img)

		self.ImageLabel.image=icon
		self.ImageLabel.configure(image=icon)

	def submit(self):
		print "[SSTV GUI]: Working on "+currentImage
		if self.var.get() == 1:
			if self.CheckVar1.get() == 1 and self.CheckVar2.get() == 0:
				os.system('python sstv.py --mode "Robot36" "'+currentImage+'" --sharpen')
			elif self.CheckVar1.get() == 0 and self.CheckVar2.get() == 1:
				os.system('python sstv.py --mode "Robot36" "'+currentImage+'" --contrast')
			elif self.CheckVar1.get() == 1 and self.CheckVar2.get() ==1:
				os.system('python sstv.py --mode "Robot36" "'+currentImage+'" --sharpen --contrast')
			else:
				os.system('python sstv.py --mode "Robot36" "'+currentImage+'"')

		else:
			if self.CheckVar1.get() == 1 and self.CheckVar2.get() == 0:
				os.system('python sstv.py --mode "PD240" "'+currentImage+'" --sharpen')
			elif self.CheckVar1.get() == 0 and self.CheckVar2.get() == 1:
				os.system('python sstv.py --mode "PD240" "'+currentImage+'" --contrast')
			elif self.CheckVar1.get() == 1 and self.CheckVar2.get() ==1:
				os.system('python sstv.py --mode "PD240" "'+currentImage+'" --sharpen --contrast')
			else:
				os.system('python sstv.py --mode "PD240" "'+currentImage+'"')

		tkMessageBox.showinfo("SSTV GUI!", "Process completed!")

class HomePage(Page):
	def __init__(self, *args, **kwargs):
		Page.__init__(self, *args, **kwargs)
		self.config(bg="#616A6B")
		self.image = ""

		self.browse = Button(self, text="Browse an Image", command=self.browse_image,
			bg=buttonBackground, activebackground=buttonBackground_active, width=15)
		self.browse.pack(pady=10)

		self.button1 = Button(self, text="Analyse Image", command=self.analyse,
			bg=buttonBackground, activebackground=buttonBackground_active, width=15)
		self.button1.pack(pady=10)

		self.button4 = Button(self, text="Fourier Analysis", command=self.fourier,
			bg=buttonBackground, activebackground=buttonBackground_active, width=15)
		self.button4.pack(pady=10)

		self.button2 = Button(self, text="SSTV Generator", command=self.sstv_gen,
			bg=buttonBackground, activebackground=buttonBackground_active, width=15)
		self.button2.pack(pady=10)

		self.button1.config(state="disabled")
		self.button2.config(state="disabled")
		self.button4.config(state="disabled")

		logoPanel = Label(self, bg = "#616A6B")
		logoPanel.pack()
		logoPanel.place(x=160, y=210)

		logo = ImageTk.PhotoImage(Image.open("logo.png"))
		logoPanel.image = logo
		logoPanel.configure(image=logo)

	def fourier(self):
		global currentImage
		currentImage = self.image
		fourierpgae.updatefft()
		fourierpgae.show()

	def browse_image(self):
		f = askopenfile()
		self.image = f.name 
		self.button1.config(state="normal")
		self.button2.config(state="normal")
		self.button4.config(state="normal")

	def sstv_gen(self):
		global currentImage
		currentImage = self.image
		sstvpage.updateLabel()
		sstvpage.show()

	def convertToRGB(self, image_array):
		destRGB = cv2.cvtColor(image_array, cv2.COLOR_BGR2RGB)
		return destRGB

	def analyse(self):
		img = Image.open(self.image)

		# sharp image
		sharp = ImageManipulator.sharpen(self.image)
		sharp = self.convertToRGB(sharp)

		# high contrast image
		contrast = ImageManipulator.equaliseColored(self.image)
		contrast = self.convertToRGB(contrast)

		# both
		sharp_and_contrast = ImageManipulator.manipulate(self.image)
		sharp_and_contrast = self.convertToRGB(sharp_and_contrast)

		plt.subplot(221), plt.imshow(img)
		plt.title("Original Image"), plt.xticks([]), plt.yticks([])
		plt.subplot(222), plt.imshow(sharp)
		plt.title("Sharpened Image"), plt.xticks([]), plt.yticks([])
		plt.subplot(223), plt.imshow(contrast)
		plt.title("High Contrast Image"), plt.xticks([]), plt.yticks([])
		plt.subplot(224), plt.imshow(sharp_and_contrast)
		plt.title("Sharpened & High Contrast Image"), plt.xticks([]), plt.yticks([])
		plt.show()

class MainView(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
        global hp, sstvpage, fourierpgae
        hp = HomePage()
        sstvpage = SSTVGenPage()
        fourierpgae = fftPage()

        self.container = Frame(self)
        self.container.pack(side = 'top', fill = 'both', expand = True)
        hp.place(in_ = self.container, x = 0, y = 0, relwidth = 1, relheight = 1)
        sstvpage.place(in_ = self.container, x = 0, y = 0, relwidth = 1, relheight = 1)
        fourierpgae.place(in_ = self.container, x = 0, y = 0, relwidth = 1, relheight = 1)
        hp.show()


if __name__ == '__main__':
    root = Tk()

    main = MainView(root)
    main.pack(side = 'top', fill = 'both', expand = True)

    root.wm_geometry('500x500')
    root.resizable(height=0, width=0)

    root.title('SSTV Generator')

    root.mainloop()
        
        
