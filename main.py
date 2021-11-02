# TODO 3. Create another paddle
# TODO 4. Create the ball and make it move
# TODO 5. Detect collision with wall and bounce
# TODO 6. Detect collision with paddle
# TODO 7. Detect when paddle misses# TODO 1. Create the Screen
# TODO 8. Keep Score
import random
import time
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

screen.listen()
screen.onkeypress(pad1.move_up, "w")
screen.onkeypress(pad1.move_down, "s")

screen.onkeypress(pad2.move_up, "Up")
screen.onkeypress(pad2.move_down, "Down")

game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)



screen.exitonclick()




