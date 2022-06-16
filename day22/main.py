from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

HEIGHT = 600
WIDTH = 800
BG_COLOR = "black"

screen = Screen()
screen.bgcolor(BG_COLOR)
screen.setup(width=WIDTH, height=HEIGHT)
screen.title("Pong")
screen.tracer(n=0)
l_paddle = Paddle(x=-350, y=0)
r_paddle = Paddle(x=350, y=0)

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

ball = Ball()
scoreboard = Scoreboard()
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    ball.move()
    screen.update()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or \
            (ball.distance(l_paddle) < 50 and ball.ycor() < -320):
        ball.bounce_x()
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
