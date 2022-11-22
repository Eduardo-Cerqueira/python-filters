import cv2 as cv
import numpy as np

def dilation(path,num):
    img = cv.imread(cv.samples.findFile(path))
    print(f"\nProcessing '{path}'")
    img = cv.dilate(img, np.ones((num, num), np.uint8) , 1)
    cv.imshow("Display window", img)
    print("Image processed")
    cv.imwrite("output/megumin_dilation.png", img)
    print(f"Image '{path}' saved in output directory")