from filters import black_white, blur, dilation
#import manage
import os

#manage.open_img("imgs/megumin.jpeg")
black_white.black_white("imgs/megumin.jpeg")
blur.blur("imgs/megumin.jpeg",55,"GaussianBlur") # GaussianBlur, MedianBlur, Blur
dilation.dilation("imgs/megumin.jpeg",10)

def reprocess():
    path = "imgs"
    list_of_files = []
    
    for root, dirs, files in os.walk(path):
        for file in files:
            list_of_files.append(os.path.join(root,file))
    for name in list_of_files:
        black_white.black_white(name)
        file_name = os.path.basename(name).split('/')[-1]
        blur.blur(f"output/{file_name}", 55, "GaussianBlur")