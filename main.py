from filters import black_white, blur, dilation, gif_generator, img_from_video
import os, sys, click, re


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
@click.option('--output-format', help="Choose the name of the gif")
@click.option('--video', help="Choose a video to transform into images")

def main(i,filters,output_format,video,o):
    def apply_filter(input,filtr,output):
        list_filter = []
        args = filtr.split("|")
        file_name = os.path.basename(input).split('/')[-1]
        for c in range(len(args)):
            list_filter.append(args[c].split(":"))
        
            if list_filter[c][0] == "blur":
                if c == 0:
                    blur.blur(input, int(list_filter[0][1]), "Blur", output)
                else:
                    blur.blur(output, int(list_filter[c][1]), "Blur", output)
                
            elif list_filter[c][0] == "medianblur":
                if c == 0:
                    blur.blur(input, int(list_filter[0][1]), "MedianBlur", output)
                else:
                    blur.blur(output, int(list_filter[c][1]), "MedianBlur", output)

            elif list_filter[c][0] == "gaussianblur":
                if c == 0:
                    blur.blur(input, int(list_filter[0][1]), "GaussianBlur", output)
                else:
                    blur.blur(output, int(list_filter[c][1]), "GaussianBlur", output)

            elif list_filter[c][0] == "grayscale":
                if c == 0:
                    black_white.black_white(input, output)
                else:
                    black_white.black_white(f"{output}/{file_name}", output)

            elif list_filter[c][0] == "dilate":
                if c == 0:
                    dilation.dilation(input, int(list_filter[0][1]), output)
                else:
                    dilation.dilation(f"{output}/{file_name}", int(list_filter[c][1]), output)
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
        gif_generator.gif_generator(o,output_format,o)

    if video is not None:
        img_from_video.img_from_video(video, o)

if __name__ == '__main__':
    try:
        main()
    except AttributeError:
        os.system("python3 main.py --help")