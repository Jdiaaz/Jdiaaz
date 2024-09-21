import math
import turtle

# Configuraciones iniciales de turtle
turtle.bgcolor("black")
turtle.pencolor("black")
turtle.shape("triangle")
turtle.speed(0)
turtle.fillcolor("orangered")

# Cálculo del ángulo en radianes
phi = 137.508 * (math.pi / 180.0)

# Dibujar el patrón
for i in range(180 + 40):
    r = 4 * math.sqrt(i)
    theta = i * phi
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(i * 137.508)
    turtle.pendown()
    
    # Estampar y dibujar la figura
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

# Escribir "Te quiero mi niña" en la parte inferior
turtle.penup()
turtle.goto(0, -320)  # Colocación más abajo en la pantalla
turtle.pendown()
turtle.pencolor("lightblue")  # Color de las letras
turtle.write("Te quiero mi niña", align="center", font=("Times New Roman", 30, "bold"))

# Finalizar y evitar que la ventana se cierre automáticamente
turtle.hideturtle()
turtle.done()

# Mantener la ventana abierta
turtle.mainloop()
