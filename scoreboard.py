from turtle import Turtle
FONT = ("Courier", 20, "normal")

class Scoreboard(Turtle):
  def __init__(self):
    super().__init__()
    self.goto(0, 270)
    self.color("white")
    self.hideturtle()
    self.r_score = 0
    self.l_score = 0
    self.update_score()

  def update_score(self):
    self.write(f"{self.r_score} : {self.l_score}", align="center", font=FONT)

  def r_point(self):
    self.clear()
    self.r_score += 1
    self.update_score()

  def l_point(self):
    self.clear()
    self.l_score += 1
    self.update_score()