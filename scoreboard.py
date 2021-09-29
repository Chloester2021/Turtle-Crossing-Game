from turtle import *
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = 0
        self.increase()

    def increase(self):
        self.clear()
        self.setpos(-250, 260)
        self.write(f'Score: {self.score}', align="left", font=FONT)
        self.score += 1

    def game_over(self):
        self.setpos(-20, 0)
        self.write(f'GAME OVER', align="center", font=FONT)
