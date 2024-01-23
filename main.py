import time
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
# Screen set up
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Ping pong game")
screen.tracer(0)

# Create paddle

l_paddle = Paddle((-370, 0))
r_paddle = Paddle((370, 0))

#Create ball
ball = Ball()

#Create scoreboard
scoreboard = Scoreboard()

# Controls paddle
screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")

screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

pong_on = True
while pong_on:
  screen.update()
  time.sleep(0.1)
  ball.move()
  print(r_paddle.distance(ball))

  # Ball detects a collision with wall
  if ball.ycor() > 280 or ball.ycor() < -280:
    ball.bounce()

  # Ball detects a collision with paddle
  if r_paddle.distance(ball) < 100 and ball.xcor() == 350:
    ball.bounce_paddle()

  if l_paddle.distance(ball) < 100 and ball.xcor() == -350:
    ball.bounce_paddle()

  if ball.xcor() > 300:
    pass
  if ball.ycor() < -300:
    pass
screen.exitonclick()
