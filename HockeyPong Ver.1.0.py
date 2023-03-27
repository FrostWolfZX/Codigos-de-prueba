import turtle

#Ventana
wn = turtle.Screen()
wn.title("Hockey Pong 4 Player ver.1.0")
wn.bgcolor("black")
wn.setup(width = 1200, height = 600)
wn.tracer(0)

#Marcador
marcadorA = 0
marcadorB = 0

#JugadorA
jugadorA = turtle.Turtle()
jugadorA.speed(0)
jugadorA.shape("square")
jugadorA.color("red")
jugadorA.penup()
jugadorA.goto(-350,0)
jugadorA.shapesize(stretch_wid=5, stretch_len = 0.7)

#JugadorA2
jugadorA2 = turtle.Turtle()
jugadorA2.speed(0)
jugadorA2.shape("square")
jugadorA2.color("dark red")
jugadorA2.penup()
jugadorA2.goto(-500,0)
jugadorA2.shapesize(stretch_wid=5, stretch_len = 0.7)


#JugadorB
jugadorB = turtle.Turtle()
jugadorB.speed(0)
jugadorB.shape("square")
jugadorB.color("blue")
jugadorB.penup()
jugadorB.goto(350,0)
jugadorB.shapesize(stretch_wid=5, stretch_len = 0.7)

#JugadorB2
jugadorB2 = turtle.Turtle()
jugadorB2.speed(0)
jugadorB2.shape("square")
jugadorB2.color("dark blue")
jugadorB2.penup()
jugadorB2.goto(500,0)
jugadorB2.shapesize(stretch_wid=5, stretch_len = 0.7)


#Pelota
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)

#Velocidad y Direccion de la Pelota
ball.dx = 1.90
ball.dy = 1.90

#Division
division = turtle.Turtle()
division.color("white")
division.goto(0,400)
division.goto(0,-400)

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Equipo Rojo : 0    Equipo Azul : 0", align = "center", font=("courier", 24, "normal"))

#Jugador A
def jugadorA_up():
    y = jugadorA.ycor()
    y += 110
    jugadorA.sety(y)
    if jugadorA.ycor() > 250:
       jugadorA.sety(250)

def jugadorA_down():
    y = jugadorA.ycor()
    y -= 108
    jugadorA.sety(y)
    if jugadorA.ycor() < -250:
       jugadorA.sety(-250)

#Jugador A2
def jugadorA2_up():
    y = jugadorA2.ycor()
    y += 108
    jugadorA2.sety(y)
    if jugadorA2.ycor() > 250:
       jugadorA2.sety(250)

def jugadorA2_down():
    y = jugadorA2.ycor()
    y -= 110
    jugadorA2.sety(y)
    if jugadorA2.ycor() < -250:
       jugadorA2.sety(-250)

#Jugador B
def jugadorB_up():
    y = jugadorB.ycor()
    y += 108
    jugadorB.sety(y)
    if jugadorB.ycor() > 250:
       jugadorB.sety(250)

def jugadorB_down():
    y = jugadorB.ycor()
    y -= 108
    jugadorB.sety(y)
    if jugadorB.ycor() < -250:
       jugadorB.sety(-250)

#Jugador B2
def jugadorB2_up():
    y = jugadorB2.ycor()
    y += 108
    jugadorB2.sety(y)
    if jugadorB2.ycor() > 250:
       jugadorB2.sety(250)

def jugadorB2_down():
    y = jugadorB2.ycor()
    y -= 108
    jugadorB2.sety(y)
    if jugadorB2.ycor() < -250:
       jugadorB2.sety(-250)


#Controles
wn.listen()
wn.onkeypress(jugadorA_up, "w")
wn.onkeypress(jugadorA_down, "s")
wn.onkeypress(jugadorA2_up, "q")
wn.onkeypress(jugadorA2_down, "a")

wn.onkeypress(jugadorB_up, "i")
wn.onkeypress(jugadorB_down, "k")
wn.onkeypress(jugadorB2_up, "o")
wn.onkeypress(jugadorB2_down, "l")

while True:
    wn.update()

    ball.setx(ball.xcor() +  ball.dx)
    ball.sety(ball.ycor() +  ball.dy)

    #Bordes
    if ball.ycor() > 290:
        ball.dy*= -1
    if ball.ycor() < -290:
        ball.dy*= -1

    #Borde derecha/izquierda
    if ball.xcor() > 640:
        ball.goto(0,0)
        ball.dx *= -1
        marcadorA += 1
        pen.clear()
        pen.write("Equipo Rojo : {}    Equipo Azul: {}".format(marcadorA,marcadorB), align = "center", font=("courier", 24, "normal"))

    if ball.xcor() < -640:
        ball.goto(0,0) 
        ball.dx *= -1
        marcadorB += 1
        pen.clear()
        pen.write("Equipo Rojo : {}    Equipo Azul: {}".format(marcadorA,marcadorB), align = "center", font=("courier", 24, "normal"))

#Colision
    if ((ball.xcor() > 340 and ball.xcor() < 350)
            and (ball.ycor() < jugadorB.ycor() + 50
            and ball.ycor() > jugadorB.ycor() - 50)):
        ball.dx *= -1

    if ((ball.xcor() > 490 and ball.xcor() < 500)
            and (ball.ycor() < jugadorB2.ycor() + 50
            and ball.ycor() > jugadorB2.ycor() - 50)):
        ball.dx *= -1    

    if ((ball.xcor() < -340 and ball.xcor() < -350)
            and (ball.ycor() < jugadorA.ycor() + 50
            and ball.ycor() > jugadorA.ycor() - 50)):
        ball.dx *= -1

    if ((ball.xcor() < -490 and ball.xcor() < -500)
            and (ball.ycor() < jugadorA2.ycor() + 50
            and ball.ycor() > jugadorA2.ycor() - 50)):
        ball.dx *= -1
