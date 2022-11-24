import cv2 as cv
import numpy as np
import os
from PIL import Image

def gif_generator(i,output):
    isFile = os.path.isfile(i)
    isDirectory = os.path.isdir(i)
    if (isFile == False and isDirectory == False):
        print("Exception : File or Directory doesn't exit")
    else:
        list_of_files = []
        for root, dirs, files in os.walk(i):
                for file in files:
                    list_of_files.append(os.path.join(root,file))
                for name in list_of_files:
                    print(name)
                    img = Image.open(name)
                    img.append(name)
        _, ext = os.path.splitext(i)
        if ext not in [".png",".jpg",".jpeg"]:
            print("Exception : Could not read the image. Make the file is an image")
        else:
            list_of_files = []
            img = Image.open(f"{i}/{name}")
            file_name = os.path.basename(input).split('/')[-1]
            print(file_name)
            img.save(f"{file_name}")
            for root, dirs, files in os.walk(i):
                for file in files:
                    list_of_files.append(os.path.join(root,file))
                for name in list_of_files:
                    print(name)
                    img = Image.open(name)
                    img.append_images(name)
                    

def gif(i,output):
    isFile = os.path.isfile(i)
    isDirectory = os.path.isdir(i)
    if (isFile == False and isDirectory == False):
        print("Exception : File or Directory doesn't exit")
    else:
        list_of_files = []
        for root, dirs, files in os.walk(i):
                for file in files:
                    list_of_files.append(os.path.join(root,file))
                    print(len(list_of_files))
                for e in list_of_files:
                    print(e)
                    e.save(f"{output}/{i}.gif", save_all=True, append_images=images[1:], optimize=False, duration=40, loop=0)

#gif("imgs", "output")