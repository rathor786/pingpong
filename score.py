from turtle import Turtle


class Score(Turtle):
    def __init__(self, score_position):
        super().__init__()
        self.penup()
        self.score=0
        self.color("white")
        self.goto(score_position)
        self.write(arg=f"score {self.score}", align="center",font=("courier",25,"normal"))


        self.hideturtle()

    def update(self):
        self.score+=1
        self.clear()
        self.write(arg=f"score {self.score}", align="center",font=("courier",25,"normal"))

