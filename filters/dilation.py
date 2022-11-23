import cv2 as cv
import numpy as np
import os

def dilation(path,num,output):
    isFile = os.path.isfile(path)
    isDirectory = os.path.isdir(path)
    if (isFile == False and isDirectory == False):
        print("Exception : File doesn't exit")
    else:
        try:
            img = cv.imread(cv.samples.findFile(path))
            print(f"\nProcessing '{path}'")
            img = cv.dilate(img, np.ones((num, num), np.uint8) , 1)
            print("Image processed")
            file_name = os.path.basename(path).split('/')[-1]
            cv.imwrite(f"output/{file_name}", img)
            file_name = os.path.basename(path).split('/')[-1]
            print(f"Image '{output}/{file_name}' saved in output directory")
        except ValueError:
                print("Exception : No numbers below zero")