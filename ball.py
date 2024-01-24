from turtle import Turtle


class Ball(Turtle):
  def __init__(self):
    super().__init__()
    self.shape("circle")
    self.color("white")
    self.penup()
    self.change_y = 3
    self.change_x = 3
    self.move()
    self.move_speed = 0.1

  def move(self):
    x_coord = self.xcor() + self.change_x
    y_coord = self.ycor() + self.change_y
    self.goto(x_coord, y_coord)

  def bounce(self):
    self.change_y *= -1

  def bounce_paddle(self):
    self.change_x *= -1
    self.move_speed *= 0.7


  def respawn(self):
    self.goto(0, 0)
    self.bounce_paddle()
    self.move_speed = 0.1

