from turtle import Screen
from player import Player
from car import Car
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=700)
screen.tracer(0)
player = Player()
car = Car()
score = Scoreboard()
screen.listen()
screen.onkeypress(player.move, "Up")
game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move_cars()
    for auto in car.all_cars:
        if auto.distance(player) < 25:
            game_on = False
            score.game_over()

    if player.ycor() > 350:
        car.level_up()
        player.goto(0,-330)
        score.update()


screen.exitonclick()