from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(0.6, 4)
        self.right(-90)
        self.penup()

    def going(self,x,y):
        self.goto(x,y)

    def up_paddle(self):
        self.forward(20)
        self.penup()

    def down_paddle(self):
        self.backward(20)
        self.penup()
