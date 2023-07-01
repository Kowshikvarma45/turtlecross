from turtle import Turtle
FONT = ("courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.pencolor("white")
        self.level = 1
        self.goto(-280,310)
        self.write(f'LEVEL - {self.level}', align='left', font=FONT)

    def update(self):
        self.clear()
        self.level += 1
        self.write(f'LEVEL - {self.level}', align='left', font=FONT)
    def game_over(self):
        self.home()
        self.write(f'GAME OVER!', align='center', font=FONT)
