#PLACAR QUANDO A RAQUETE ERRAR
from turtle import Turtle   

class Scoreboard(Turtle):
    
    def __init__(self):          #atributos:
        super().__init__()       #importado atributos da super classe
        self.color("white")
        self.penup()
        self.hideturtle()        #esconde a turtle
        self.l_score = 0
        self.r_score = 0
        self.atualizar_scoreboard()

    def atualizar_scoreboard(self):
        self.clear()             #limpar antes de atualizar para não sobrepor.
        self.goto(x=-100, y= 200)#colocar no centro e na parte superior
        self.write(self.l_score, align="center", font=("Courier", 50, "bold" ))
        self.goto(100,200)
        self.write(self.r_score, align="center", font=("Courier", 50, "bold" ))

    #MÉTODO PARA MARCAR PONTO:

    def l_point(self):
        self.l_score +=1
        self.atualizar_scoreboard()

    def r_point(self):
        self.r_score +=1
        self.atualizar_scoreboard()

