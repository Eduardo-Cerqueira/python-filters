from filters import black_white, blur, dilation
import manage

#manage.open_img("imgs/megumin.jpeg")
black_white.black_white_img("imgs/megumin.jpeg")
blur.blur("imgs/megumin.jpeg",55,"GaussianBlur") # GaussianBlur, MedianBlur, Blur
dilation.dilation("imgs/megumin.jpeg",10)