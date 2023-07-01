from turtle import Turtle
import random
STARTING_CAR_SPEED = 5
MOVE_INCREMENT = 10
COLORS = ["white", "red", "green", "blue", "yellow", "orange", "purple", "pink", "brown", "gray", "cyan", "magenta"]


class Car:
    def __init__(self):
        self.all_cars = []
        self.carspeed = STARTING_CAR_SPEED

    def create_car(self):
        random_number = random.randint(1, 6)
        if random_number == 1:
            new_car = Turtle()
            new_car.shape("square")
            random_color = random.choice(COLORS)
            new_car.color(random_color)
            new_car.penup()
            new_car.setheading(180)
            new_car.shapesize(stretch_wid=0.8, stretch_len=2)
            random_y = random.randint(-320, 320)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)
    def move_cars(self):
        for car in self.all_cars:
            car.fd(self.carspeed)
    def level_up(self):
        self.carspeed += MOVE_INCREMENT