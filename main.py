"""Click makes easy cli - OS find and manage files"""
import os
import click
from gif_generator import gif_generator
from img_from_video import img_from_video
from apply_filter import apply_filter
from log_file_manage import log_file_manage, log_flags


@click.command()
@click.option("-i", default=f"{'imgs'}", help="--input-dir <directory>")
@click.option("-o", default=f"{'output'}", help="--output-dir <directory>")
@click.option(
    "--filters",
    default=f"{None}",
    help="Choose filter from blur, gaussianblur, medianblur, dilate, grayscale",
)
@click.option("--log-file", help="Log all actions in a file")
@click.option("--config-file", help="For save a .ini files")
@click.option("--output-format", help="Choose the name of the gif")
@click.option("--video", help="Choose a video to transform into images")
@click.option(
    "--list-filters",
    is_flag=True,
    show_default=True,
    default=False,
    help="Greet the world.",
)
def main(i, filters, log_file, output_format, config_file, list_filters, video, o):
    """Main - gather all fonctions and manages them all"""
    if os.path.isdir(o) is False:
        os.mkdir(o)

    is_file = os.path.isfile(f"{output_format}/{log_file}")

    if config_file is not None:
        filetr = open("ConfigFile.ini", "r")
        content = filetr.readlines()
        i = content[0]
        o = content[1]
        filters = content[2]
        print(filetr)

    if log_file:
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

    if list_filters is not False:
        click.echo("Discover all the filters ! :\n")
        filters_dic = {
            "blur": "blur : \nTake : Odd Number \nPun : Looking back, my entire life was just a blur until I got glasses.\n",
            "medianblur": "medianblur : \nTake : Odd Number \nPun : Even though Math is a median of instruction, teachers can be really mean. Sometimes they enjoy students going into range mode.\n",
            "gaussianblur": "gaussianblur : \nTake : Odd Number \nPun : .¯\_(ツ)_/¯.\n",
            "dilate": "dilate : \nTake : odd number \nPun : My optometrist had my pupils dilated today. It was an eye-opening experience.\n",
            "grayscale": "grayscale : \nTake : Nothing \nPun : Roses are gray, violets are gray. I'm colorblind, heck.\n",
            "zeteams": "zeteams : \nTake : Nothing \nPun : There is a guy named Meet in my team.\n",
        }
        click.echo(filters_dic["blur"])
        click.echo(filters_dic["medianblur"])
        click.echo(filters_dic["gaussianblur"])
        click.echo(filters_dic["dilate"])
        click.echo(filters_dic["grayscale"])
        click.echo(filters_dic["zeteams"])


if __name__ == "__main__":
    main()
