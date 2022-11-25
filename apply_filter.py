"""OS find and manage files"""
import os
from filters import black_white, blur, dilation


def apply_filter(input_dir, filtr, log_file, output):
    """Uses packages in the module filters to process an entire directory, given multiple params"""
    list_filter = []
    args = filtr.split("|")
    file_name = os.path.basename(input_dir).split("/")[-1]
    for number in range(len(args)):
        list_filter.append(args[number].split(":"))

        if list_filter[number][0] == "blur":
            if number == 0:
                blur.blur(input_dir, int(list_filter[0][1]), "Blur", log_file, output)
            else:
                blur.blur(
                    f"{output}/{file_name}",
                    int(list_filter[number][1]),
                    "Blur",
                    log_file,
                    output,
                )

        elif list_filter[number][0] == "medianblur":
            if number == 0:
                blur.blur(
                    input_dir, int(list_filter[0][1]), "MedianBlur", log_file, output
                )
            else:
                blur.blur(
                    f"{output}/{file_name}",
                    int(list_filter[number][1]),
                    "MedianBlur",
                    log_file,
                    output,
                )

        elif list_filter[number][0] == "gaussianblur":
            if number == 0:
                blur.blur(
                    input_dir, int(list_filter[0][1]), "GaussianBlur", log_file, output
                )
            else:
                blur.blur(
                    f"{output}/{file_name}",
                    int(list_filter[number][1]),
                    "GaussianBlur",
                    log_file,
                    output,
                )

        elif list_filter[number][0] == "grayscale":
            if number == 0:
                black_white.black_white(input_dir, log_file, output)
            else:
                black_white.black_white(f"{output}/{file_name}", log_file, output)

        elif list_filter[number][0] == "dilate":
            if number == 0:
                dilation.dilation(input_dir, int(list_filter[0][1]), log_file, output)
            else:
                dilation.dilation(
                    f"{output}/{file_name}",
                    int(list_filter[number][1]),
                    log_file,
                    output,
                )
