import cv2 as cv
import numpy as np
import os

def blur(path,num,typeblur):
    def process(img):
        print("Image processed") # Followup for user
        file_name = os.path.basename(path).split('/')[-1]
        cv.imwrite(f"output/{file_name}", img)
        file_name = os.path.basename(path).split('/')[-1]
        print(f"Image 'output/{file_name}' saved in output directory")

    isFile = os.path.isfile(path)
    isDirectory = os.path.isdir(path)
    if (isFile == False and isDirectory == False):
        print("Exception : File doesn't exit")
    else:
        img = cv.imread(cv.samples.findFile(path))
        if img is None:
            print("Exception : Could not read the image. Make the file is an image")
        else:
            try:
                print(f"\nProcessing '{path}'") # Followup for user
                if typeblur == "GaussianBlur":
                    img = cv.GaussianBlur(img,(num, num),0)
                    process(img)
                elif typeblur == "MedianBlur":
                    img = cv.medianBlur(img, num)
                    process(img)
                elif typeblur == "Blur":
                    img = cv.blur(img, (num,num))
                    process(img)
                else:
                    print("Not valid blur") # Error input typeblur
            except cv.error:
                print("Exception : No even numbers or numbers below zero")