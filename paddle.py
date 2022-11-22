from turtle import Turtle


class Paddle(Turtle):
    def __init__(self,x=10,y=10):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(0.7, 6)
        self.right(-90)
        self.penup()
        self.goto(x,y)

    def go_up(self):
        self.forward(30)
        self.penup()

    def go_down(self):
        self.backward(30)
        self.penup()
