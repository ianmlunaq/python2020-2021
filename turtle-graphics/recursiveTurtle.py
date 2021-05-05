import turtle
import math
import random
spiralGlobalRep = 0

def spiral(turtle, sideLength, angle, scaleFactor, minLength, setReps=1, red=255, grn=0, blu=0):
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

                if red == 255 and grn < 255 and blu == 0:
                    grn += 1
                if grn == 255 and blu == 0:
                    red -= 1
                if red == 0 and grn == 255:
                    blu += 1
                if blu == 255 and grn > 0:
                    grn -= 1
                if blu == 255 and grn == 0:
                    red += 1
                if red == 255 and grn == 0:
                    blu -= 1

                turtle.color(red/255, grn/255, blu/255)
                reps += 1
                heading = startDir + (angle * reps)
                turtle.seth(heading)
                forwardLength = forwardLength * scaleFactor
                turtle.forward(forwardLength)
        
        turtle.up()
        turtle.home()
        turtle.down()
        spiralGlobalRep += 1

        spiral(turtle, sideLength, angle, scaleFactor, minLength, setReps, red, grn, blu)

def main():
    try:
        turtle.TurtleScreen._RUNNING = True
        turtle.screensize(canvwidth=1920, canvheight=1080, bg=None)
        print(turtle.Screen().screensize())

        turtle.tracer(0, 0)

        window = turtle.Screen()
        will = turtle.Turtle()
        window.bgcolor('black')
        will.color(1, 0, 0)
        will.speed(0)
        will.ht()
        will.pensize(3)

        will.up()
        will.home()
        will.down()

        spiral(will, 400, 118, .98, 50)    # spiral(turtle, sideLength, angle, scaleFactor, minLength, setReps=0)

        """
        # turtle: turtle that you need to pass into spiral()
        # sideLength: the initial side length
        # angle: angle that the will be added to turtle's heading when drawing shape (*kind of* defines the drawn shape)
        # scaleFactor: if set to 1 it will not spiral; if set to 1.0 > scaleFactor > 0.0, defines
        # minLength: defines the point at which turtle will stop drawing; turtle will stop drawing after drawing a line equal in length to minLength
        """

        window.update()
        
        window.exitonclick()

    finally:
        turtle.Terminator()

print('Running ' + '\'' + __file__ + '\'' '...')

if __name__ == '__main__':
    print('Running main()')
    main()