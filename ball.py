from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
      

    def move(self):
        new_y = self.ycor() +0.5
        new_x = self.xcor() +0.5
        self.goto(new_x, new_y)

    def bater(self):
        new_y = self.ycor() -0.5

