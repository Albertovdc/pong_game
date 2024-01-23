from turtle import Turtle


class Ball(Turtle):
  def __init__(self):
    super().__init__()
    self.shape("circle")
    self.color("white")
    self.penup()
    self.change_y = 1
    self.change_x = 1
    self.move()
    self.bounce()
    self.bounce_paddle()

  def move(self):
    self.goto(self.xcor() - (10 * self.change_x), self.ycor() - (10 * self.change_y))

  def bounce(self):
    self.change_y *= -1

  def bounce_paddle(self):
    self.change_x *= -1