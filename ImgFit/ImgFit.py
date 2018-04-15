from PIL import Image

def fit(image, best_width=None, best_height=None):
        img = Image.open(image)
        w, h = img.size
        aspect_ratio = w*h**(-1)

        if h >= w:
                newWidth = int(aspect_ratio*best_height)
                img = img.resize((newWidth,best_height), Image.ANTIALIAS)
        else:
                newHeight = int(best_width*aspect_ratio**(-1))
                img = img.resize((best_width,newHeight), Image.ANTIALIAS)

        return img
