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
    self.write(f"{self.r_score} : {self.l_score}", align="center", font=FONT)