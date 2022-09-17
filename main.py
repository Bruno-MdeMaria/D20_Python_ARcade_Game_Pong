from turtle import Screen, Turtle, goto, position
from padle import Padle
from ball import Ball
from scoreboard import Scoreboard


#CONSTRUÇÃO DA TELA:
screen = Screen()
screen.setup(width= 800, height= 600)
screen.bgcolor("black")
screen.title("Pong - Arcade Game")
screen.tracer(0)    #o zero elimina a animação na tela. por isso é necessáro chamar o metodo .update dentro de um laço a diante.

#OBJETOS:
r_padle = Padle((350,0))
l_padle = Padle((-350,0))
ball = Ball()
scoreboard = Scoreboard()

#OUVIR O TECLADO PARA PODER MOVER A PÁ:
screen.listen()
screen.onkeypress(r_padle.go_up, "Up")
screen.onkeypress(r_padle.go_down, "Down")
screen.onkeypress(l_padle.go_up, "w")
screen.onkeypress(l_padle.go_down, "s")

game_on = True
while game_on == True:
    screen.update()
    ball.mover()
    
#DETECTAR COLISÃO COM A PAREDE:
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bater_y()

#DETECTAR COLISÃO COM AS DUAS PADLE:
    if ball.distance(r_padle) < 50 and ball.xcor() > 340 or ball.distance(l_padle) < 50 and ball.xcor() <-340:  #se a distancia da bola e a raquete direita for menor que 50px e a distancia da bola na cordenada x for menor que 340 então ela atingiu a raquete. O mesmo (or) com a raquete esquerda.
        ball.bater_x()

#DETECTAR QUANDO AS PADLE NÃO CONSEGUEM BATER NA BOLA:
    if ball.xcor() > 410:
        ball.reset_position()
        scoreboard.l_point()
    
    if ball.xcor() < -410:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()