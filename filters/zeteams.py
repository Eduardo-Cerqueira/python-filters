"""OS find and manage files - OpenCV manages image and video processing"""
import os
import cv2 as cv
from log_file_manage import log_message
import rich
from rich.progress import track
import time


def zeteams(input_dir, log_file, message, color_given ,output):
    """Add name of dev team to the image in path"""
    is_file = os.path.isfile(input_dir)
    is_directory = os.path.isdir(input_dir)
    if is_file is False and is_directory is False:
        log_message(
            "ze_teams.py",
            log_file,
            "Exception : File or Directory doesn't exit",
            output,
        )
        print("Exception : File or Directory doesn't exit")
    else:
        _, ext = os.path.splitext(input_dir)
        if ext not in [".png", ".jpg", ".jpeg"]:
            log_message(
                "ze_teams.py",
                log_file,
                "Exception : Could not read the image. Make the file is an image",
                output,
            )
            print("Exception : Could not read the image. Make the file is an image")
        else:
            image = cv.imread(cv.samples.findFile(input_dir))
            log_message(
                "ze_teams.py",
                log_file,
                f"Processing '{input_dir}'",
                output,
            )
            list_rgb = []
            args = color_given.split(",")
            for val_e in range(len(args)):
                list_rgb.append(args[val_e])

            print(f"\nProcessing '{input_dir}'")  # Followup for user
            newimage = cv.putText(
                img=image,
                text=message,
                org=(25, 50),
                fontFace=cv.FONT_HERSHEY_DUPLEX,
                fontScale=1.0,
                color=(int(list_rgb[0]),int(list_rgb[1]),int(list_rgb[2]))
                )
            try:
                file_name = os.path.basename(input_dir).split("/")[-1]
                cv.imwrite(f"output/{file_name}", newimage)
                log_message("ze_teams.py", log_file, "Image processed", output)
                print("Image processed")  # Followup for user
                log_message(
                    "ze_teams.py",
                    log_file,
                    f"Image '{output}/{file_name}' saved in output directory",
                    output,
                )
                rich.progress_bar.ProgressBar(total=100, completed=0)
                for i in track(range(100), description="Processing..."):
                    time.sleep(0.01)  # Simulate work being done
                print(f"Image '{output}/{file_name}' saved in output directory")
            except cv.error:
                print("The image is not realy a image")
                log_message("zeteams.py", log_file, "The image is not realy a image", output)
                pass
