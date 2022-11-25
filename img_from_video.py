"""OS find and manages files - OpenCV for image and video process"""
import os
import cv2 as cv
from log_file_manage import log_message


def frame_generate(input_path, name_video, log_file, output):
    """Take a video and process all frames to give images"""
    message = "img_from_video.py"
    log_message(message, log_file, "Processing the video ...", output)
    print("Processing the video ...")
    cam = cv.VideoCapture(f"{input_path}/{name_video}")
    currentframe = 0

    while True:
        is_frame, frame = cam.read()
        if is_frame:
            name = f"{output}/{name_video}_{str(currentframe)}.jpg"
            cv.imwrite(name, frame)
            currentframe += 1
        else:
            break
    cam.release()
    cv.destroyAllWindows()
    log_message(message, log_file, "Video processed !", output)
    print("Video processed !")


def img_from_video(input_dir, video, log_file, output):
    """Check condition to transform video to images and invoke frame_generate"""
    message = "img_from_video.py"
    is_file = os.path.isfile(input_dir)
    is_directory = os.path.isdir(input_dir)
    if is_file is False and is_directory is False:
        log_message(
            message,
            log_file,
            "Exception : File or Directory doesn't exit",
            output,
        )
        print("Exception : File or Directory doesn't exit")
    else:
        file_name = os.path.basename(input_dir).split("/")[-1]
        name_video = os.path.splitext(video)[0]
        _, ext = os.path.splitext(video)
        if ext not in [".mp4"]:
            log_message(
                message,
                log_file,
                f"Exception : {video} is not a video",
                output,
            )
            log_message(
                message, log_file, f"Exception : {video} is not a video", output
            )
            print(f"Exception : {video} is not a video")
        else:
            is_file += os.path.isfile(output)
            is_directory += os.path.isdir(output)
            if is_file is False and is_directory is False:
                os.mkdir(output)
            frame_generate(input_dir, video, log_file, output)
