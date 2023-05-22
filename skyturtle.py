from turtle import *
from random import randint

#Page setup
setup (800, 500)
speed(0)
bgcolor("black")
# We made function to draw a star:
def star():
    color("yellow")
    begin_fill()
    for i in range(5):
        forward(10)
        right(144)
    end_fill()


#Draw lot of stars random on screen:
# For it We will create a loop:
for i in range(20):
    x = randint(-400, 400)
    y = randint(-250, 250)
    star()
    #To make stars randomly everywhere on screen, we need:
    penup()
    goto(x, y)
    pendown()
#Moon-Part!
penup()
goto(-300, 100)
pendown()
color("white")
begin_fill()
circle(50)
end_fill()
#Moon-Part2
penup()
goto(-280, 100)
pendown()
color("black")
begin_fill()
circle(50)
end_fill()
