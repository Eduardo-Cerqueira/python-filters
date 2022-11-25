"""OS find and manages files - Datatime give the current time"""
import os
from datetime import datetime


def time():
    """current time for logs"""
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y | %H:%M:%S")
    return dt_string


def log_message(filename, log_file, name_log, output):
    """Provides to others files a away to send logs during execution"""
    if log_file is not None:
        with open(os.path.join(output, log_file), "a") as file_logs:
            file_logs.write(f"{time()} - {filename} : {name_log}\n")


def log_flags(i, filters, log_file, output_format, video, output):
    """Sends flags user used to launch main to the logs"""
    with open(os.path.join(output, log_file), "a") as file:
        params = (
            f" --log-file {log_file} --output-format {output_format} --video {video}"
        )
        file.write(
            f"{time()} - main.py : python3 main.py -i {i} -o {output} --filters {filters}{params}\n"
        )


def log_file_manage(name_log, output):
    """Create logs at start of main if they don't exist"""
    is_file = os.path.isfile(f"{output}/{name_log}")
    if is_file is False:
        with open(os.path.join(output, name_log), "x") as file_logs:
            file_logs.write(f"{time()} : Log file created\n")
            file_logs.close()
