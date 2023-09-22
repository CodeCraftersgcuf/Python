from turtle import *


bgcolor("black")
colors=["red", "green", "blue", "yellow", "purple", "pink", "orange", "white","grey","skyblue", "violet"]

for i in range(360):
    speed(1000)
    pencolor(colors[i%10])
    width(i//100 +10)
    forward(i)
    right(90)
    forward(i)
    left(45)

done()    