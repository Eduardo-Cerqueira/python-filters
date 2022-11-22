import cv2 as cv

def black_white_img(path):
    img = cv.imread(cv.samples.findFile(path))
    print(f"\nProcessing '{path}'")
    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    cv.imshow("Display window", img)
    print("Image processed")
    cv.imwrite("output/megumin_black_white.png", img)
    print(f"Image '{path}' saved in output directory")