from turtle import Turtle

class Paddle(Turtle):


    def __init__(self, start_x):
        super(Paddle, self).__init__()

        self.y_cords = [0, 20, 40]
        self.turtles = []
        self.start_x = start_x

        for num in range(0,3):
            segment = Turtle()
            segment.goto(self.start_x, self.y_cords[num])
            segment.color('white')
            segment.penup()
            segment.shape('square')
            self.turtles.append(segment)

    def move_up(self):
        for t in self.turtles:
            t.setheading(90)
            t.forward(100)

    def move_down(self):
        for t in self.turtles:
            t.setheading(270)
            t.forward(100)