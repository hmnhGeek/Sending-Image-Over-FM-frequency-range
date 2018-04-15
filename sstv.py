import generateSSTV, ImageManipulator, spectrum
import argparse as ap
import os

parser = ap.ArgumentParser()
parser.add_argument('image', type=str, help="Pass the image.")
parser.add_argument('--mode', type=str, help="Pass PD240 or Robot36.")
parser.add_argument('--sharpen', action='store_true', help="Sharp the image before SSTV generation.")
parser.add_argument('--contrast', action='store_true', help="Increase the contrast befor SSTV generation.")
parser.add_argument('--freeze', action='store_true', help="Save the manipulated image.")
parser.add_argument('--nosstv', action='store_true', help="Do not generate SSTV for now.")
args = parser.parse_args()

if args.image and args.mode:
    if args.sharpen or args.contrast:
        if args.sharpen and args.contrast:
            #generate sharpened and high contrast image.
            img = ImageManipulator.ImageManipulator.manipulate(args.image)
        elif args.sharpen and not args.contrast:
            img = ImageManipulator.ImageManipulator.sharpen(args.image)
        elif args.contrast and not args.sharpen:
            img = ImageManipulator.ImageManipulator.equaliseColored(args.image)

        # save the manipulated image temporarily.
        ImageManipulator.ImageManipulator.save(img, args.image+"temp_image.jpg")

        if not args.nosstv:
            # Now generate SSTV
            if args.mode == "PD240":
                generateSSTV.generateSSTV.generatePD240(args.image+"temp_image.jpg")
            elif args.mode == "Robot36":
                generateSSTV.generateSSTV.generateRobot36(args.image+"temp_image.jpg")
            else:
                print "Wrong arguments for --mode."
            
        if not args.freeze:
            #remove the manipulated image.
            os.remove(args.image+"temp_image.jpg")
    else:
        if not args.nosstv:
            # Now generate SSTV
            if args.mode == "PD240":
                generateSSTV.generateSSTV.generatePD240(args.image)
            elif args.mode == "Robot36":
                generateSSTV.generateSSTV.generateRobot36(args.image)
            else:
                print "Wrong arguments for --mode."

else:
    print "Wrong arguments."
    
