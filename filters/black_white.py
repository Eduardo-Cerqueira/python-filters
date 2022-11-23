import cv2 as cv
import numpy as np
import os

def black_white(path):
    isFile = os.path.isfile(path)
    isDirectory = os.path.isdir(path)
    if (isFile == False and isDirectory == False):
        print("Exception : File doesn't exit")
    else:
        img = cv.imread(cv.samples.findFile(path))
        if img is None:
            print("Exception : Could not read the image. Make the file is an image")
        else:
            print(f"\nProcessing '{path}'") # Followup for user
            img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
            print("Image processed") # Followup for user
            file_name = os.path.basename(path).split('/')[-1]
            cv.imwrite(f"output/{file_name}", img)
            print(f"Image '{path}' saved in output directory")