from log_file_manage import log_message
import cv2 as cv
import numpy as np
import os

def frame_generate(i,name_video,log_file,o):
    log_message("img_from_video.py",log_file,"Processing the video ...", output)
    print("Processing the video ...")
    cam = cv.VideoCapture(i)
    currentframe = 0
    
    while(True):
        is_frame,frame = cam.read()
        if is_frame:
            name = f'{o}/{name_video}_{str(currentframe)}.jpg'
            cv.imwrite(name, frame)
            currentframe += 1
        else:
            break
    cam.release()
    cv.destroyAllWindows()
    log_message("img_from_video.py",log_file,"Video processed !", output)
    print("Video processed !")

def img_from_video(input,video,output):
    isFile = os.path.isfile(input)
    isDirectory = os.path.isdir(input)
    if (isFile == False and isDirectory == False):
        log_message("img_from_video.py",log_file,"Exception : File or Directory doesn't exit", output)
        print("Exception : File or Directory doesn't exit")
    else:
        file = os.path.basename(input).split('/')[-1]
        name_video = os.path.splitext(file)[0]
        _, ext = os.path.splitext(file)
        if ext not in [".mp4"]:
            log_message("img_from_video.py",log_file,f"Exception : {file} is not a video", output)
            print(f"Exception : {file} is not a video")
        else:
            isFile = os.path.isfile(output)
            isDirectory = os.path.isdir(output)
            if (isFile == False and isDirectory == False):
                    os.mkdir(output)
            frame_generate(input,name_video,output)