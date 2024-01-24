import time
from turtle import Screen
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
  time.sleep(ball.move_speed)
  ball.move()


  # Ball detects a collision with wall
  if ball.ycor() > 280 or ball.ycor() < -280:
    ball.bounce()
  print(ball.distance(r_paddle))
  print(ball.xcor())
  # Ball detects a collision with paddle
  if ball.distance(r_paddle) < 50 and ball.xcor() > 350 or ball.distance(l_paddle) < 50 and ball.xcor() < -350:
    ball.bounce_paddle()

  # if ball.distance(l_paddle) < 40 and ball.xcor() < -350:
  #   ball.bounce_paddle()

  # Points
  if ball.xcor() > 380:
    scoreboard.l_point()
    ball.respawn()
  if ball.xcor() < -380:
    scoreboard.r_point()
    ball.respawn()

screen.exitonclick()
