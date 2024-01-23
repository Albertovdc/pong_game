from turtle import Screen, Turtle

screen = Screen()
# Screen set up
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Ping pong game")

# Create paddle
r_paddle = Turtle()
r_paddle.goto(-380, 0)
r_paddle.penup()
r_paddle.color("white")
r_paddle.shape("square")
r_paddle.shapesize(stretch_wid=4, stretch_len=1)

def move_up():
  r_paddle.goto(r_paddle.xcor(), r_paddle.ycor() + 20)

def move_down():
  r_paddle.goto(r_paddle.xcor(), r_paddle.ycor() - 20)

# Controls paddle
screen.listen()
screen.onkey(move_up, "W")
screen.onkey(move_down, "S")

screen.exitonclick()
