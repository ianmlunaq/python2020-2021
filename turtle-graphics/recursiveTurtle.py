import turtle
import math
import random

# TODO: 
# - spokes
# - random generation
# - full color wheel

def spiral(will, sideLength, angle, scaleFactor, minLength, repCounter, red=255, grn=0, blu=0):
    

    if repCounter < 6:
        #print('Running spiral()...') 
        reps = 0
        forwardLength = sideLength

        startDir = 60 * repCounter
        will.seth(startDir)
        will.color(red, grn, blu)
        will.forward(forwardLength)

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

            if red > 255:
                red = 255
            if red < 0:
                red = 0
            if grn > 255:
                grn = 255
            if grn < 0:
                grn = 0
            if blu > 255:
                blu = 255
            if blu < 0:
                blu = 0

            

            will.color(red, grn, blu)
            #print(will.color())
            #print(turtle.turtles())

            reps += 1
            heading = startDir + (angle * reps)
            will.seth(heading)
            forwardLength = forwardLength * scaleFactor
            will.forward(forwardLength)
        
        will.up()
        will.home()
        will.down()
        repCounter += 1
    else:
        return()

    spiral(will, sideLength, angle, scaleFactor, minLength, repCounter, red, grn, blu)

def main():
    try:
        turtle.TurtleScreen._RUNNING = True
        turtle.screensize(canvwidth=1920, canvheight=1080, bg=None)
        turtle.colormode(255)
        #print(turtle.Screen().screensize())

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

        repCounter = 0

        sideLength = 400
        randomAngle = random.randint(30, 330)
        randomScaleFactor = random.random()
        randomMinLength = random.randint(1, sideLength)

        spiral(will, sideLength, randomAngle, .98, randomMinLength, repCounter)    # spiral(turtle, sideLength, angle, scaleFactor, minLength, repCounter)

        
        # turtle: turtle that you need to pass into spiral()
        # sideLength: the initial side length
        # angle: angle that the will be added to turtle's heading when drawing shape (*kind of* defines the drawn shape)
        # scaleFactor: must be set to 1.0 > scaleFactor > 0.0
        # minLength: defines the point at which turtle will stop drawing; turtle will stop drawing after drawing a line equal in length to minLength
        

        window.update()
        print("Done!")
        
        window.exitonclick()

    finally:
        turtle.Terminator()

print('Running ' + '\'' + __file__ + '\'' '...')

if __name__ == '__main__':
    #print('Running main()')
    main()