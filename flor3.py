import math
import turtle


turtle.speed(0.50)
turtle.bgcolor("black")
turtle.goto(0, -40)


turtle.color("blue")
for i in range(16):
    for j in range(18):
        turtle.rt(90)
        turtle.circle(150 - j * 6, 90)
        turtle.lt(90)
        turtle.circle(150 - j * 6, 90)
        turtle.rt(180)
    turtle.circle(40, 24)


turtle.color("black")
turtle.shape("turtle")
turtle.fillcolor("brown")
phi = 137.508 * (math.pi / 180.0)

for i in range(200):
    r = 4 * math.sqrt(i)
    theta = i * phi
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(i * 137.508)
    turtle.pendown()
    turtle.stamp()


turtle.penup()
turtle.goto(0, 300)  
turtle.color("white")  
turtle.write("Tu ahijado tambien te da una flor amarilla:D", align="center", font=("Arial", 24, "bold"))

turtle.done()
