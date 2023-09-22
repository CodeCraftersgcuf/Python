from turtle import *
from colorsys import *
from time import *

bgcolor('black')
speed(10000)
setup(768,700)
tracer(9)
pensize(3)
sleep(1)
h=1

for i in range(1000):
    c=hsv_to_rgb(h,1,1)
    h+=0.003
    color(c)
    penup()
    goto(0,0)
    forward(i/3)
    pendown()
    right(89)
    fillcolor('black')
    begin_fill()
    circle(70,110)
    end_fill()
    left(179)
    left(6)

done()