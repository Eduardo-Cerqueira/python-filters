from filters import black_white, blur, dilation
from gif_generator import gif_generator
from img_from_video import img_from_video
from apply_filter import apply_filter
import os, click


isDirectory = os.path.isdir("output")
if (isDirectory == False):
    os.mkdir("output")

"""
black_white.black_white("imgs/megumin.jpeg","output")
blur.blur("imgs/megumin.jpeg",55,"GaussianBlur","output") # GaussianBlur, MedianBlur, Blur
dilation.dilation("imgs/megumin.jpeg",10,"output")
"""

@click.command()
@click.option('-i', default="imgs", help='--input-dir <directory>')
@click.option('-o', default="output", help='--output-dir <directory>')
@click.option('--filters', default="None", help="Choose filter from blur, gaussianblur, medianblur, dilate, grayscale")
@click.option('--log-file', help="Log all actions in a file")
@click.option('--output-format', help="Choose the name of the gif")
@click.option('--video', help="Choose a video to transform into images")


def main(i,filters,log_file,output_format,video,o):
    if os.path.isdir(i) == False:
        apply_filter(i,filters,o)
    else:
        list_of_files = []
        for root, dirs, files in os.walk(i):
            for file in files:
                list_of_files.append(os.path.join(root,file))
        for name in list_of_files:
            apply_filter(name,filters,o)

    if output_format is not None:
        gif_generator(o,output_format,o)

    if video is not None:
        img_from_video(video, o)

if __name__ == '__main__':
    try:
        main()
    except AttributeError:
        os.system("python3 main.py --help")