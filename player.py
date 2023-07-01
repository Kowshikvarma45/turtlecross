from turtle import Turtle
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("white")
        self.setheading(90)
        self.goto(0, -330)

    def move(self):
        self.fd(10)