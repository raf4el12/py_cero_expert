import math
import turtle

# Configuración inicial
turtle.bgcolor("black")
turtle.pencolor("black")
turtle.shape("triangle")
turtle.speed(0)
turtle.fillcolor("orangered")

# Parámetro phi para dibujar el patrón en espiral
phi = 137.508 * (math.pi / 180.0)

# Dibujar el patrón en espiral
for i in range(180 + 40):
    r = 4 * math.sqrt(i)
    theta = i * phi
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(i * 137.508)
    turtle.pendown()
    if i < 160:
        turtle.stamp()
    else:
        turtle.fillcolor("yellow")
        turtle.begin_fill()
        turtle.left(-5)
        turtle.circle(500, 25)
        turtle.right(-155)
        turtle.circle(500, 25)
        turtle.end_fill()

# Añadir el mensaje al final
turtle.penup()
turtle.goto(0, 300)  # Ajusta la posición vertical según sea necesario
turtle.color("white")  # Color del texto
turtle.write("Ya tienes tu ramo en fisico y tambien virtual, te amo mi vida", align="center", font=("Arial", 24, "bold"))

# Ocultar la tortuga y finalizar
turtle.hideturtle()
turtle.done()
