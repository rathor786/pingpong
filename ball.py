import turtle
from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(0.5, 0.5, 1)
        self.color("white")
        self.penup()
        self.move_speed=0.1
        self.x_move=10
        self.y_move=10


    def move(self):

        self.goto(self.xcor()+self.x_move,self.ycor()+self.y_move)


    def bounce_y(self):
        self.y_move*=-1
        self.move_speed*=0.9
    def bounce_x(self):
        self.x_move*=-1
    def ball_reset(self):
        self.home()
        self.move_speed=0.1
        self.bounce_x()







