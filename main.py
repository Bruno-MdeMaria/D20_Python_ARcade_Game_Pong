from turtle import Screen, Turtle, goto, position
from padle import Padle
from ball import Ball


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

#OUVIR O TECLADO PARA PODER MOVER A PÁ:
screen.listen()
screen.onkeypress(r_padle.go_up, "Up")
screen.onkeypress(r_padle.go_down, "Down")
screen.onkeypress(l_padle.go_up, "w")
screen.onkeypress(l_padle.go_down, "s")

game_on = True
while game_on == True:
    screen.update()
    ball.move()
    
#DETECTAR COLISÃO COM A PAREDE:
    if ball.ycor() > 300 or ball.ycor < -300:
        pass

screen.exitonclick()