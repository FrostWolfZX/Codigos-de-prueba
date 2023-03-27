from cgi import parse_multipart
from tkinter import Y
import turtle

#ventana
wn = turtle.Screen()
wn.title("Turbo Pong ver.1.0")
wn.bgcolor("black")
wn.setup(width = 800, height = 600)
wn.tracer(0)

#marcador
marcadorA = 0
marcadorB = 0


#jugadorA
jugadorA = turtle.Turtle()
jugadorA.speed(0)
jugadorA.shape("square")
jugadorA.color("red")
jugadorA.penup()
jugadorA.goto(-350,0)
jugadorA.shapesize(stretch_wid=5, stretch_len = 0.50)

#jugadorB
jugadorB = turtle.Turtle()
jugadorB.speed(0)
jugadorB.shape("square")
jugadorB.color("blue")
jugadorB.penup()
jugadorB.goto(350,0)
jugadorB.shapesize(stretch_wid=5, stretch_len = 0.50)

#pelota
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 3.10
ball.dy = 3.10

#division
division = turtle.Turtle()
division.color("white")
division.goto(0,400)
division.goto(0,-400)

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Jugador1 : 0    Jugador2: 0", align = "center", font=("courier", 24, "normal"))

#1
def jugadorA_up():
    y = jugadorA.ycor()
    y += 108
    jugadorA.sety(y)
    if jugadorA.ycor() > 250:
       jugadorA.sety(250)

def jugadorA_down():
    y = jugadorA.ycor()
    y -= 108
    jugadorA.sety(y)
    if jugadorA.ycor() < -250:
       jugadorA.sety(-250)


#2
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

wn.listen()
wn.onkeypress(jugadorA_up, "w")
wn.onkeypress(jugadorA_down, "s")
wn.onkeypress(jugadorB_up, "i")
wn.onkeypress(jugadorB_down, "k")


while True:
    wn.update()

    ball.setx(ball.xcor() +  ball.dx)
    ball.sety(ball.ycor() +  ball.dy)

    #bordes
    if ball.ycor() > 290:
        ball.dy*= -1
    if ball.ycor() < -290:
        ball.dy*= -1

    #borde derecho/izquierdo
    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        marcadorA += 1
        pen.clear()
        pen.write("Jugador1 : {}    Jugador2: {}".format(marcadorA,marcadorB), align = "center", font=("courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0,0) 
        ball.dx *= -1
        marcadorB += 1
        pen.clear()
        pen.write("Jugador1 : {}    Jugador2: {}".format(marcadorA,marcadorB), align = "center", font=("courier", 24, "normal"))


    if ((ball.xcor() > 340 and ball.xcor() < 350)
            and (ball.ycor() < jugadorB.ycor() + 50
            and ball.ycor() > jugadorB.ycor() - 50)):
        ball.dx *= -1


    if ((ball.xcor() < -340 and ball.xcor() < -350)
            and (ball.ycor() < jugadorA.ycor() + 50
            and ball.ycor() > jugadorA.ycor() - 50)):
        ball.dx *= -1


