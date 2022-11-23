import cv2 as cv
import numpy as np
import os

def black_white(path,output):
    isFile = os.path.isfile(path)
    isDirectory = os.path.isdir(path)
    if (isFile == False and isDirectory == False):
        print("Exception : File or Directory doesn't exit")
    else:
        _, ext = os.path.splitext(path)
        if ext not in [".png",".jpg",".jpeg"]:
            print("Exception : Could not read the image. Make the file is an image")
        else:
            img = cv.imread(cv.samples.findFile(path))
            print(f"\nProcessing '{path}'") # Followup for user
            img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
            print("Image processed") # Followup for user
            file_name = os.path.basename(path).split('/')[-1]
            cv.imwrite(f"output/{file_name}", img)
            file_name = os.path.basename(path).split('/')[-1]
            print(f"Image '{output}/{file_name}' saved in output directory")