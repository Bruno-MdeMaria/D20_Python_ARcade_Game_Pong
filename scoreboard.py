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
        self.goto(x=-100, y= 200)#colocar no centro e na parte superior
        self.write(self.l_score, align="center", font=("Courier", 50, "normal" ))
        self.goto(100,200)
        self.write(self.r_score, align="center", font=("Courier", 50, "normal" ))

