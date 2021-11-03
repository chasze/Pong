# TODO 5. Detect collision with wall and bounce
# TODO 6. Detect collision with paddle
# TODO 8. Keep Score
import random
import time
from ball import Ball
from turtle import Screen, Turtle
from paddle import Paddle

WIDTH = 600
HEIGHT = 500

screen = Screen()
screen.tracer(0)
screen.bgcolor('black')
screen.screensize(canvheight=HEIGHT, canvwidth=WIDTH)

pad1 = Paddle(450)
pad2 = Paddle(-450)
ball1 = Ball()

screen.listen()
screen.onkeypress(pad1.move_up, "w")
screen.onkeypress(pad1.move_down, "s")

screen.onkeypress(pad2.move_up, "Up")
screen.onkeypress(pad2.move_down, "Down")

game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)

    ball1.move()

    if ball1.ycor() < -400:
        ball1.move_up()
    if ball1.ycor() > 400:
        ball1.move_down()

    for tur in pad1.turtles:
        while tur.distance(ball1) < 15:
            ball1.move_backwards()
    for tur in pad2.turtles:
        while tur.distance(ball1) < 15:
            ball1.move_forwards()

    if ball1.xcor() < - 500 or ball1.xcor() > 500:
        game_on = False
        print("Game Over")





screen.exitonclick()
