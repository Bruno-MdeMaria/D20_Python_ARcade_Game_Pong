from turtle import Screen, Turtle, goto
from padle import Padle


#CONSTRUÇÃO DA TELA:
screen = Screen()
screen.setup(width= 800, height= 600)
screen.bgcolor("black")
screen.title("Pong - Arcade Game")
screen.tracer(0)    #o zero elimina a animação na tela. por isso é necessáro chamar o metodo .update dentro de um laço a diante.

r_padle = Padle(goto(350,0))
l_padle = Padle(goto(-350,0))


#OUVIR O TECLADO PARA PODER MOVER A PÁ:
screen.listen()
screen.onkey(r_padle.go_up, "Up")
screen.onkey(r_padle.go_down, "Down")

game_on = True
while game_on == True:
    screen.update()


screen.exitonclick()