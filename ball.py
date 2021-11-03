import random
from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super(Ball, self).__init__()
        self.color('white')
        self.penup()
        self.speed('fastest')
        self.shape('circle')

    def move(self):
        self.forward(50)

    def move_backwards(self):
        self.setheading(180 + random.randint(0, 45))
        self.move()

    def move_forwards(self):
        self.setheading(0 + random.randint(0,45))
        self.move()

    def move_up(self):
        self.setheading(90 + random.randint(10, 45))
        self.move()

    def move_down(self):
        self.setheading(270 + random.randint(10, 45))
        self.move()