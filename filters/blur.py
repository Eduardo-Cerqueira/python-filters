from log_file_manage import log_message
import cv2 as cv
import numpy as np
import os

def process(path,img,log_file,output):
        log_message("blur.py",log_file,"Image processed", output)
        print("Image processed") # Followup for user
        file_name = os.path.basename(path).split('/')[-1]
        cv.imwrite(f"output/{file_name}", img)
        file_name = os.path.basename(path).split('/')[-1]
        print(f"Image '{output}/{file_name}' saved in output directory")
        log_message("blur.py",log_file,f"Image '{output}/{file_name}' saved in output directory", output)

def blur(path,num,typeblur,log_file,output):
    isFile = os.path.isfile(path)
    isDirectory = os.path.isdir(path)
    if (isFile == False and isDirectory == False):
        log_message("blur.py",log_file,"Exception : File or Directory doesn't exit", output)
        print("Exception : File or Directory doesn't exit")
    else:
        _, ext = os.path.splitext(path)
        if ext not in [".png",".jpg",".jpeg"]:
            log_message("blur.py",log_file,"Exception : Could not read the image. Make the file is an image", output)
            print("Exception : Could not read the image. Make the file is an image")
        else:
            try:
                img = cv.imread(cv.samples.findFile(path))
                log_message("blur.py",log_file,f"Processing '{path}'", output)
                print(f"\nProcessing '{path}'") # Followup for user
                if typeblur == "GaussianBlur":
                    log_message("blur.py",log_file,"GaussianBlur choosen", output)
                    img = cv.GaussianBlur(img,(num, num),0)
                    process(path,img,log_file,output)
                elif typeblur == "MedianBlur":
                    log_message("blur.py",log_file,"MedianBlur choosen", output)
                    img = cv.medianBlur(img, num)
                    process(path,img,log_file,output)
                elif typeblur == "Blur":
                    log_message("blur.py",log_file,"Blur choosen", output)
                    img = cv.blur(img, (num,num))
                    process(path,img,log_file,output)
                else:
                    log_message("blur.py",log_file,"Not valid blur", output)
                    print("Not valid blur") # Error input typeblur
            except cv.error:
                log_message("blur.py",log_file,"Exception : No even numbers or numbers below zero", output)
                print("Exception : No even numbers or numbers below zero")