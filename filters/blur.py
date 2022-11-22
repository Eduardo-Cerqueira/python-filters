import cv2 as cv

def blur(path,num,typeblur):
    def process(img):
        img = cv.medianBlur(img, num)
        cv.imshow("Display window", img)
        print("Image processed") # Followup for user
        cv.imwrite("output/megumin_blur.png", img)
        print(f"Image '{path}' saved in output directory")
        
    img = cv.imread(cv.samples.findFile(path))

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