"""OS find and manages files - OpenCV for image and video process - PIL for image process to gif"""
import os
from PIL import Image
from log_file_manage import log_message


def gif_generator(
    input_dir,
    name_file,
    log_file,
    output,
):
    """Generate a gif using a images from a given directory"""
    is_file = os.path.isfile(input_dir)
    is_directory = os.path.isdir(input_dir)
    if is_file is False and is_directory is False:
        log_message(
            "gif_generator.py",
            log_file,
            "Exception : File or Directory doesn't exit",
            output,
        )
        print("Exception : File or Directory doesn't exit")
    else:
        list_of_files = []
        for root, dirs, files in os.walk(input_dir):
            for file in files:
                _, ext = os.path.splitext(file)
                if ext not in [".png", ".jpg", ".jpeg"]:
                    log_message(
                        "gif_generator.py",
                        log_file,
                        f"Exception : {file} is not an image",
                        output,
                    )
                    print(f"Exception : {file} is not an image")
                else:
                    list_of_files.append(os.path.join(root, file))
            images = []
            for name in list_of_files:
                image_resized = Image.open(name).resize((800, 400))
                images.append(image_resized)
            images[0].save(
                f"{output}/{name_file}.gif",
                format="GIF",
                append_images=images[1:],
                save_all=True,
                duration=50,
                loop=0,
            )
