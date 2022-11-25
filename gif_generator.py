from log_file_manage import log_message
import cv2 as cv
import numpy as np
import os
from PIL import Image

def gif_generator(input,name_file,log_file,output,):
    isFile = os.path.isfile(input)
    isDirectory = os.path.isdir(input)
    if (isFile == False and isDirectory == False):
        log_message("gif_generator.py",log_file,"Exception : File or Directory doesn't exit", output)
        print("Exception : File or Directory doesn't exit")
    else:
        list_of_files = []
        for root, dirs, files in os.walk(input):
                for file in files:
                    _, ext = os.path.splitext(file)
                    if ext not in [".png",".jpg",".jpeg"]:
                        log_message("gif_generator.py",log_file,f"Exception : {file} is not an image", output)
                        print(f"Exception : {file} is not an image")
                    else:
                        list_of_files.append(os.path.join(root,file))
                images = []
                for c in list_of_files:
                    new_image = Image.open(c)
                    image_resized = new_image.resize((800,400))
                    images.append(image_resized)
                images[0].save(f"{output}/{name_file}.gif", format = 'GIF', append_images= images[1:], save_all=True, duration = 500, loop = 0)