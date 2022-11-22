import cv2 as cv
import numpy as np
import sys

def open_img(path):
    img = cv.imread(cv.samples.findFile(path))
    if img is None:
        sys.exit("Could not read the image.")
    cv.imshow("Display window", img)
    k = cv.waitKey(0)
    if k == ord("s"):
        cv.imwrite("assets/starry_night.png", img)

def blur_img(path):
    img = cv.imread(cv.samples.findFile(path))
    if img is None:
        sys.exit("Could not read the image.")
    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    cv.imshow("Display window", img)
    cv.imwrite("assets/starry_night2.png", img)
