from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time

# creating pong screen
screen = Screen()
screen.bgcolor("black")
screen.setup(1100,700)
screen.title("Pong Game!")
screen.tracer(0)

# creating the ball from its class
ball = Ball()

# left paddle from its class
paddle_left = Paddle(-530,0)

# right paddle from its class
paddle_right = Paddle(520,0)


# screen listening
screen.listen()
screen.onkeypress(paddle_right.go_up, "Up")
screen.onkeypress(paddle_right.go_down, "Down")

screen.onkeypress(paddle_left.go_up, "w")
screen.onkeypress(paddle_left.go_down, "s")

# to eliminate the animation in the beginning
game_is_on = True
# keep track of score
player1_score = 0
player2_score = 0
# text turtle player one
player1_text = Turtle()
player1_text.shape("square")
player1_text.color("white")
player1_text.hideturtle()
player1_text.penup()
player1_text.goto(-150, 200)
player1_text.clear()
player1_text.write(f"{player1_score}", True, align="center", font=("Courier", 80, "normal"))

# text turtle player two
player2_text = Turtle()
player2_text.shape("square")
player2_text.color("white")
player2_text.hideturtle()
player2_text.penup()
player2_text.goto(150, 200)
player2_text.clear()
player2_text.write(f"{player2_score}", True, align="center", font=("Courier", 80, "normal"))

# the winning turtle
winning_turtle = Turtle()
winning_turtle.shape("square")
winning_turtle.color("white")
winning_turtle.hideturtle()
screen.update()


while game_is_on:
    screen.update()
    ball.moving()
    time.sleep(ball.move_speed)
    if int(ball.distance(paddle_right)) <= 40 or int(ball.distance(paddle_left)) <= 40:
        ball.bounce_paddle()
    elif ball.xcor() > 550 or ball.xcor() < -550:
        if ball.xcor() > 550:
            player1_score += 1
            player1_text.penup()
            player1_text.goto(-150, 200)
            player1_text.clear()
            player1_text.write(f"{player1_score}", True, align="center", font=("Courier", 80, "normal"))
        elif ball.xcor() < -550:
            player2_score += 1
            player2_text.penup()
            player2_text.goto(150, 200)
            player2_text.clear()
            player2_text.write(f"{player2_score}", True, align="center", font=("Courier", 80, "normal"))
        if player1_score == 10:
            winning_turtle.penup()
            winning_turtle.clear()
            winning_turtle.write("Player 1 Wins!", True, align="center", font=("Courier", 60, "normal"))
            break
        elif player2_score == 10:
            winning_turtle.penup()
            winning_turtle.clear()
            winning_turtle.write("Player 2 Wins!", True, align="center", font=("Courier", 60, "normal"))
            break
        ball.restart_game()


# to keep screen open
screen.exitonclick()

