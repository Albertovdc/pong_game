from turtle import Turtle
class Paddle(Turtle):
  def __init__(self, coord):
    super().__init__()
    self.goto(coord)
    self.penup()
    self.color("white")
    self.shape("square")
    self.shapesize(stretch_wid=5, stretch_len=1)

  def move_up(self):
    self.goto(self.xcor(), self.ycor() + 20)

  def move_down(self):
    self.goto(self.xcor(), self.ycor() - 20)