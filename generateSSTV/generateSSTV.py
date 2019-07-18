from PIL import Image
import os

def generatePD240(image_addr):
    print("[SSTV SuperDoer]: Generating PD240...")
    img = Image.open(image_addr)
    img = img.resize((640, 496), Image.ANTIALIAS)
    img.save(image_addr+"temp.jpg")

    cwd = os.getcwd()
    os.chdir(os.path.join(cwd, 'generateSSTV'))
    os.system('python3 __main__.py --mode PD240 --rate 44100 '+ image_addr+"temp.jpg"+ ' ' +image_addr+".wav")
    os.remove(image_addr+"temp.jpg")
    os.chdir(cwd)

def generateRobot36(image_addr):
    print("[SSTV SuperDoer]: Generating Robot36...")
    img = Image.open(image_addr)
    img = img.resize((320, 240), Image.ANTIALIAS)
    img.save(image_addr+"temp.jpg")

    cwd = os.getcwd()
    os.chdir(os.path.join(cwd, 'generateSSTV'))
    os.system('python3 __main__.py --mode Robot36 --rate 44100 '+ image_addr+"temp.jpg"+ ' ' +image_addr+".wav")
    os.remove(image_addr+"temp.jpg")
    os.chdir(cwd)
