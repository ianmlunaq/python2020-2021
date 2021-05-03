import turtle
import math
import random

def spiral(sideLength, angle, scaleFactor, minLength):
    print()


def main():
    try:
        turtle.TurtleScreen._RUNNING = True
        turtle.screensize(canvwidth=700, canvheight=700, bg=None)
        print(turtle.Screen().screensize())

        window = turtle.Screen()
        will = turtle.Turtle()
        window.bgcolor('black')
        will.color("cornflowerblue")
        will.speed(3)
        will.pensize(3)

        will.up()
        will.goto(-400, -300)
        will.down()
        will.forward(700)

        will.seth(95)
        forwardLength = 700 * .93
        will.forward(forwardLength)

        will.seth(190)
        forwardLength = 700 * .93
        will.forward(forwardLength)

        heading

        
        

        window.exitonclick()

    finally:
        turtle.Terminator()

print('Running ' + '\'' + __file__ + '\'' '...')

if __name__ == '__main__':
    main()