from filters import black_white, blur, dilation
import cv2 as cv
import numpy as np
import os

def apply_filter(input,filtr,output):
        list_filter = []
        args = filtr.split("|")
        file_name = os.path.basename(input).split('/')[-1]
        for c in range(len(args)):
            list_filter.append(args[c].split(":"))
        
            if list_filter[c][0] == "blur":
                if c == 0:
                    blur.blur(input, int(list_filter[0][1]), "Blur", output)
                else:
                    blur.blur(output, int(list_filter[c][1]), "Blur", output)
                
            elif list_filter[c][0] == "medianblur":
                if c == 0:
                    blur.blur(input, int(list_filter[0][1]), "MedianBlur", output)
                else:
                    blur.blur(output, int(list_filter[c][1]), "MedianBlur", output)

            elif list_filter[c][0] == "gaussianblur":
                if c == 0:
                    blur.blur(input, int(list_filter[0][1]), "GaussianBlur", output)
                else:
                    blur.blur(output, int(list_filter[c][1]), "GaussianBlur", output)

            elif list_filter[c][0] == "grayscale":
                if c == 0:
                    black_white.black_white(input, output)
                else:
                    black_white.black_white(f"{output}/{file_name}", output)

            elif list_filter[c][0] == "dilate":
                if c == 0:
                    dilation.dilation(input, int(list_filter[0][1]), output)
                else:
                    dilation.dilation(f"{output}/{file_name}", int(list_filter[c][1]), output)