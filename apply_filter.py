from filters import black_white, blur, dilation
from log_file_manage import log_message
import cv2 as cv
import numpy as np
import os

def apply_filter(input,filtr,log_file,output):
        list_filter = []
        args = filtr.split("|")
        file_name = os.path.basename(input).split('/')[-1]
        for c in range(len(args)):
            list_filter.append(args[c].split(":"))
        
            if list_filter[c][0] == "blur":
                if c == 0:
                    blur.blur(input, int(list_filter[0][1]), "Blur", log_file, output)
                else:
                    blur.blur(output, int(list_filter[c][1]), "Blur", log_file, output)
                
            elif list_filter[c][0] == "medianblur":
                if c == 0:
                    blur.blur(input, int(list_filter[0][1]), "MedianBlur", log_file, output)
                else:
                    blur.blur(output, int(list_filter[c][1]), "MedianBlur",log_file, output)

            elif list_filter[c][0] == "gaussianblur":
                if c == 0:
                    blur.blur(input, int(list_filter[0][1]), "GaussianBlur",log_file, output)
                else:
                    blur.blur(output, int(list_filter[c][1]), "GaussianBlur",log_file, output)

            elif list_filter[c][0] == "grayscale":
                if c == 0:
                    black_white.black_white(input, log_file, output)
                else:
                    black_white.black_white(f"{output}/{file_name}", log_file, output)

            elif list_filter[c][0] == "dilate":
                if c == 0:
                    dilation.dilation(input, int(list_filter[0][1]), log_file, output)
                else:
                    dilation.dilation(f"{output}/{file_name}", int(list_filter[c][1]), log_file, output)