from turtle import Screen, Turtle


#FAZER A TELA
screen = Screen()
screen.setup(width= 800, height= 600)
screen.bgcolor("black")
screen.title("Pong - Arcade Game")


#FAZER A PÁ
padle = Turtle()                   #produzir a pá
padle.shape("square")              #alterar o formato da tartaruga para um quadrado de 20px x 20px
padle.shapesize(stretch_wid= 5 , stretch_len= 1) #aumentar o tamanho da na altura 5 x os 20px padrao e a largura manter 1x os 20px
padle.color("white")




screen.exitonclick()