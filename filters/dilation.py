"""OS find and manage files - OpenCV manages image and video processing"""
import os
import cv2 as cv
import numpy as np
from log_file_manage import log_message


def dilation(path, num, log_file, output):
    """Add effect of dilation at image at path with given the parameters and save it at output"""
    is_file = os.path.isfile(path)
    is_directory = os.path.isdir(path)
    if is_file is False and is_directory is False:
        log_message(
            "dilation.py",
            log_file,
            "Exception : File or Directory doesn't exit",
            output,
        )
        print("Exception : File or Directory doesn't exit")
    else:
        _, ext = os.path.splitext(path)
        if ext not in [".png", ".jpg", ".jpeg"]:
            log_message(
                "dilation.py",
                log_file,
                "Exception : Could not read the image. Make the file is an image",
                output,
            )
            print("Exception : Could not read the image. Make the file is an image")
        else:
            try:
                img = cv.imread(cv.samples.findFile(path))
                log_message("dilation.py", log_file, f"Processing '{path}'", output)
                print(f"\nProcessing '{path}'")
                img = cv.dilate(img, np.ones((num, num), np.uint8), 1)
                log_message("dilation.py", log_file, "Image processed", output)
                print("Image processed")
                file_name = os.path.basename(path).split("/")[-1]
                cv.imwrite(f"output/{file_name}", img)
                file_name = os.path.basename(path).split("/")[-1]
                log_message(
                    "dilation.py",
                    log_file,
                    f"Image '{output}/{file_name}' saved in output directory",
                    output,
                )
                print(f"Image '{output}/{file_name}' saved in output directory")
            except ValueError:
                log_message(
                    "dilation.py", log_file, "Exception : No numbers below zero", output
                )
                print("Exception : No numbers below zero")
