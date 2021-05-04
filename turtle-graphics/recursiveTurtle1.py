import turtle
import math
import random
spiralGlobalRep = 0

def spiral(turtle, sideLength, angle, scaleFactor, minLength, setReps=1):
    global spiralGlobalRep

    while spiralGlobalRep < 6:
        print('Running spiral()...')
        reps = 0
        forwardLength = sideLength

        startDir = 60 * spiralGlobalRep
        turtle.seth(startDir)
        turtle.forward(forwardLength)

        if scaleFactor == 1:
            while setReps >= reps:
                reps += 1
                heading = startDir + (angle * reps)
                turtle.seth(heading)
                forwardLength = forwardLength * scaleFactor
                turtle.forward(forwardLength)
        else:
            while forwardLength >= minLength:
                reps += 1
                heading = startDir + (angle * reps)
                turtle.seth(heading)
                forwardLength = forwardLength * scaleFactor
                turtle.forward(forwardLength)
        
        turtle.home()
        spiralGlobalRep += 1

        #spiral(turtle, 800, 121, .99, 30)

def main():
    try:
        turtle.TurtleScreen._RUNNING = True
        turtle.screensize(canvwidth=700, canvheight=700, bg=None)
        print(turtle.Screen().screensize())

        window = turtle.Screen()
        will = turtle.Turtle()
        window.bgcolor('black')
        will.color("cornflowerblue")
        will.speed(0)
        will.pensize(3)

        will.up()
        will.home()
        will.down()

        spiral(will, 800, 90, .99, 30)   # #spiral(turtle, sideLength, angle, scaleFactor, minLength, setReps=0)
        
        window.exitonclick()

    finally:
        turtle.Terminator()

print('Running ' + '\'' + __file__ + '\'' '...')

if __name__ == '__main__':
    print('Running main()')
    main()