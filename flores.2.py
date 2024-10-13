import colorsys
from turtle import *
import math
import turtle

speed(0.25)
bgcolor("black")
goto(0, -40)
h = 0
for i in range(16):
    for j in range(18):
        c = colorsys.hsv_to_rgb(0.125 * j, 1, 1)
        color(c)
        rt(90)
        circle(150 - j * 6, 90)
        lt(90)
        circle(150 - j * 6, 90)
        rt(180)
    circle (40,24)

# Genera la parte central de la flor
color("black")
shape("turtle")
fillcolor("brown")
phi = 137.508 * (math.pi / 180.0)

for i in range(200):
    r = 4 * math.sqrt(i)
    theta = i * phi
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    penup()
    goto(x, y)
    setheading(i * 137.508)
    pendown()
    stamp()

#Añadir el mensaje al final
turtle.penup()
turtle.goto(0, 300)  # Ajusta la posición vertical según sea necesario
turtle.color("white")  # Color del texto
turtle.write("Ya tienes tu ramo en fisico y tambien virtual, te amo mi vida", align="center", font=("Arial", 24, "bold"))


done()


