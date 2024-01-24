from turtle import Turtle

SPEED = 0.1


class Ball(Turtle):
  def __init__(self):
    super().__init__()
    self.shape("circle")
    self.color("white")
    self.penup()
    self.speed(SPEED)
    self.change_y = 1
    self.change_x = 1
    self.move()

  def move(self):
    self.goto(self.xcor() + (10 * self.change_x), self.ycor() + (10 * self.change_y))

  def bounce(self):
    self.change_y *= -1

  def bounce_paddle(self):
    self.change_x *= -1

  def respawn(self):
    self.goto(0, 0)
    self.change_x *= -1
