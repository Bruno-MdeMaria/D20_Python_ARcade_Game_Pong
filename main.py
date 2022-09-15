from turtle import Screen, Turtle


#CONSTRUÇÃO DA TELA:
screen = Screen()
screen.setup(width= 800, height= 600)
screen.bgcolor("black")
screen.title("Pong - Arcade Game")


#CONSTRUÇÃO DA PÁ:
padle = Turtle()                   #produzir a pá
padle.shape("square")              #alterar o formato da tartaruga para um quadrado de 20px x 20px
padle.shapesize(stretch_wid= 5 , stretch_len= 1) #aumentar o tamanho da na altura 5 x os 20px padrao e a largura manter 1x os 20px
padle.color("white")
padle.goto(350,0)

#FUNÇÕES DA PÁ:
def go_up():
    pass

#OUVIR O TECLADO PARA PODER MOVER A PÁ:
screen.listen()
screen.onkey(go_up, "up")




screen.exitonclick()