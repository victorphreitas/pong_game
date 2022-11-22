from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self,x=0,y=0):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(0.8,0.8)
        self.goto(0, 0)
        self.penup()
        self.goto(x,y)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.07

    def moving(self):
        if self.ycor() >= 340 or self.ycor() <= -340:
            self.y_move *= -1
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_paddle(self):
        self.x_move *= -1
        self.move_speed *= 0.9


    def restart_game(self):
        random_num = random.randint(0,2)
        if random_num == 0:
            self.x_move *= -1
        elif random_num == 1:
            self.y_move *= -1
        elif random_num == 2:
            self.x_move *= -1
            self.y_move *= -1
        self.move_speed = 0.07
        self.goto(0,0)