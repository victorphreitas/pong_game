from turtle import Turtle, Screen
import asyncio
import random
from paddle import Paddle

# creating pong screen
screen = Screen()
screen.bgcolor("black")
screen.setup(1100,700)
screen.title("Pong")

screen.tracer(0)
game_is_on = True

# setting up the dashes in the middle of the screen
def middle_dash():
    screen.update()
    for i in range(320, -330, -40):
        dash = Turtle("square")
        dash.color("white")
        dash.speed("fastest")
        dash.shapesize(1, 0.3)
        dash.penup()
        dash.goto(0, i)

middle_dash()

# creating the ball
ball = Turtle("circle")
ball.color("white")
ball.penup()


# all paddles imported from paddle module
r_paddle = Paddle()
l_paddle = Paddle()

r_paddle.going(530,0)
l_paddle.going(-530,0)

screen.listen()

r_paddle.up_paddle()
r_paddle.down_paddle()
l_paddle.up_paddle()
l_paddle.down_paddle()

screen.onkeypress(r_paddle.up_paddle,"Up")
screen.onkeypress(r_paddle.down_paddle,"Down")
screen.onkeypress(l_paddle.up_paddle,"w")
screen.onkeypress(l_paddle.down_paddle,"s")


while game_is_on:
    screen.update()


screen.exitonclick()




# # controls left bar
# degree = random.randint(0,360)
# if degree == 90 or degree == 270:
#     degree += 30
#
# # degree = 180
# ball.right(degree)
