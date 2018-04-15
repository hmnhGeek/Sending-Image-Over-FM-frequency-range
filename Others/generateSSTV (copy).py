from PIL import Image
import os

import argparse as ap
parser = ap.ArgumentParser()
parser.add_argument("image", type=str, help="Pass the image address.")
parser.add_argument("--mode", dest='m', type=str, help="Pass the SSTV Mode.")
args=parser.parse_args()

def generatePD240(image_addr):
    img = Image.open(image_addr)
    img = img.resize((640, 496), Image.ANTIALIAS)
    img.save(image_addr+"temp.jpg")

    os.system('python __main__.py --mode PD240 --rate 44100 '+ image_addr+"temp.jpg"+ ' ' +image_addr+".wav")
    os.remove(image_addr+"temp.jpg")

def generateRobot36(image_addr):
    img = Image.open(image_addr)
    img = img.resize((320, 240), Image.ANTIALIAS)
    img.save(image_addr+"temp.jpg")

    os.system('python __main__.py --mode Robot36 --rate 44100 '+ image_addr+"temp.jpg"+ ' ' +image_addr+".wav")
    os.remove(image_addr+"temp.jpg")

if args.image and args.m=='PD240':
    generatePD240(args.image)
else:
    print "Generating Robot36"
    generateRobot36(args.image)
