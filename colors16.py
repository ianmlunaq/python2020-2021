import turtle

def draw_circle(turtle, color, size, x, y):
    turtle.penup()
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.goto(x,y)
    turtle.begin_fill()
    turtle.circle(size)
    turtle.end_fill()
    turtle.pendown()

tommy = turtle.Turtle()
tommy.shape("turtle")
tommy.speed(130)
tommy.ht()
'''
0 100.0:0.0,
22 92.718:37.461,
44 71.934:69.466,
66 40.674:91.355,
88 3.49:99.939,
'''
draw_circle(tommy, "#000000", 130, 0, -117)

draw_circle(tommy, "#2C3E50", 13, 100, 0)
draw_circle(tommy, "#34495E", 13, 93, 37)
draw_circle(tommy, "#7F8C8D", 13, 71, 70)
draw_circle(tommy, "#95A5A6", 13, 41, 91)

draw_circle(tommy, "#BDC3C7", 13, -3, 100)
draw_circle(tommy, "#E0E0E0", 13, -41, 91)
draw_circle(tommy, "#F5F5F5", 13, -72, 70)
draw_circle(tommy, "#E74C3C", 13, -93, 37)

draw_circle(tommy, "#E67E22", 13, -100, 0)
draw_circle(tommy, "#F1C40F", 13, -93, -37)
draw_circle(tommy, "#2ECC71", 13, -71, -70)
draw_circle(tommy, "#1ABC9C", 13, -41, -91)

draw_circle(tommy, "#3498DB", 13, 3, -100)
draw_circle(tommy, "#9B59B6", 13, 41, -91)
draw_circle(tommy, "#BE643C", 13, 71, -70)
draw_circle(tommy, "#71B09F", 13, 93, -37)

w = turtle.Screen()
w.exitonclick()