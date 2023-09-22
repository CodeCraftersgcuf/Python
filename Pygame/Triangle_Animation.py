from turtle import *
import colorsys
speed(1000)
width(2)
h=0.0

for i in range(250):
    c=colorsys.hsv_to_rgb(h,1,1)
    color(c)
    forward(i*2)
    right(1200)
    h+=0.1

done()