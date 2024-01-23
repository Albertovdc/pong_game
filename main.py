from turtle import Screen, Turtle
from paddle import Paddle
screen = Screen()
# Screen set up
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Ping pong game")

# Create paddle

l_paddle = Paddle((-370, 0))
r_paddle = Paddle((370, 0))


# Controls paddle
screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")

screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

screen.exitonclick()
