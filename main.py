import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car = CarManager()

scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.up, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move()

    # detect collision with car and remove car once it's off screen
    for i in car.all_cars:
        if i.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False
        if i.xcor() < -320:
            car.all_cars.remove(i)

    # level up
    if player.ycor() > 280:
        player.create()
        scoreboard.increase()
        car.level_up()


screen.exitonclick()
