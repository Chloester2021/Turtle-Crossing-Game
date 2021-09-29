from turtle import *

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.create()

    def create(self):
        self.shape('turtle')
        self.penup()
        self.color('HotPink')
        self.setheading(90)
        self.setpos(STARTING_POSITION)

    def up(self):
        self.sety(self.ycor() + MOVE_DISTANCE)
