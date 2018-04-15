from PIL import ImageTk, Image

def fit(img, best_height, best_width):
    w, h = img.size
    aspect_ratio = w*h**(-1)

    if h >= w:
        newWidth = int(aspect_ratio*best_height)
        img = img.resize((newWidth,best_height), Image.ANTIALIAS)
    else:
        newHeight = int(best_width*aspect_ratio**(-1))
        img = img.resize((best_width,newHeight), Image.ANTIALIAS)

    return ImageTk.PhotoImage(img)
