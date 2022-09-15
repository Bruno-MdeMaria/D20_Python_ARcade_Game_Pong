from turtle import Turtle



#CONSTRUÇÃO DA PÁ:
class Padle(Turtle):
    def __init__(self):
        super().__init__()
        self = Turtle()                   #produzir a pá
        self.shape("square")              #alterar o formato da tartaruga para um quadrado de 20px x 20px
        self.penup()             
        self.shapesize(stretch_wid= 5 , stretch_len= 1) #aumentar o tamanho da na altura 5 x os 20px padrao e a largura manter 1x os 20px
        self.color("white")
        self.goto(350,0)

#FUNÇÕES DA PÁ:
    def go_up(self):
        nova_posi_y = self.ycor() +20    # a nova posioção y será a posição atual y (.ycor) + 20px.
        self.goto(self.xcor(),nova_posi_y) #a nova posição (.goto) quando a função for chamada será x igual a nada pois não movimenta nesse eixo e a posicao ycor será 20px para cima.

    def go_down(self):
        nova_posi_y = self.ycor() -20
        self.goto(self.xcor(), nova_posi_y) 