import turtle
import math
import random


twin = turtle.Screen()
twin.clear()
t = turtle.Turtle()
#tWin = turtle.Screen()
t.penup()
t.goto(100,100)
t.pendown()   
t.color("#ff0000")
t.width(5)
t.goto(100,100)
t.goto(-100,100)
t.goto(-100,-100)
t.goto(100,-100)
t.goto(100,100)
twin.exitonclick()