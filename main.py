"""Click makes easy cli - OS find and manage files"""
import os
import click
from gif_generator import gif_generator
from img_from_video import img_from_video
from apply_filter import apply_filter
from log_file_manage import log_file_manage, log_flags


@click.command()
@click.option("-i", default="imgs", help="--input-dir <directory>")
@click.option("-o", default="output", help="--output-dir <directory>")
@click.option(
    "--filters",
    default="None",
    help="Choose filter from blur, gaussianblur, medianblur, dilate, grayscale",
)
@click.option("--log-file", help="Log all actions in a file")
@click.option("--output-format", help="Choose the name of the gif")
@click.option("--video", help="Choose a video to transform into images")
def main(i, filters, log_file, output_format, video, o):
    """Main - gather all fonctions and manages them all"""
    if os.path.isdir(o) is False:
        os.mkdir(o)
    if log_file is not None:
        log_file_manage(log_file, o)
        log_flags(i, filters, log_file, output_format, video, o)

    if os.path.isdir(i) is False:
        apply_filter(i, filters, log_file, o)
    else:
        list_of_files = []
        for root, dirs, files in os.walk(i):
            for file in files:
                list_of_files.append(os.path.join(root, file))
        for name in list_of_files:
            apply_filter(name, filters, log_file, o)

    if output_format is not None:
        gif_generator(o, output_format, log_file, o)

    if video is not None:
        img_from_video(i, video, log_file, o)

    if log_file is not None:
        log_file_manage(log_file, o)


if __name__ == "__main__":
    main()
