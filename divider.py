from turtle import Turtle
class Divider(Turtle):
    def __init__(self):
        super().__init__()
        self.speed(10)
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0,300)
        self.right(90)
        self.fun()

    def fun(self):
        while self.ycor() > -300:
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(10)
