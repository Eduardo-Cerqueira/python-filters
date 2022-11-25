from datetime import datetime
import os

def time():
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y | %H:%M:%S")
    return dt_string

def log_message(filename,log_file,name_log,o):
    if log_file != None:
        with open(os.path.join(o, log_file), 'a') as file:
            file.write(f"{time()} - {filename} : {name_log}\n")

def log_flags(i,filters,log_file,output_format,video,o):
    with open(os.path.join(o, log_file), 'a') as file:
            file.write(f"{time()} - main.py : python3 main.py -i {i} -o {o} --filters {filters} --log-file {log_file} --output-format {output_format} --video {video}\n")

def log_file_manage(name_log,o):
    isFile = os.path.isfile(f"{o}/{name_log}")
    if isFile == False:
        file = open(f"{o}/{name_log}", 'x')
        file.write(f"{time()} : Log file created\n")
        file.close()