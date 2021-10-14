import turtle
import time
from turtle import Screen
import paddle,ball,score,divider
position = [(370, 0), (-370, 0)]
score_position=[(-100,250),(100,250)]
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
turtle.tracer(0)
left_paddle = paddle.Paddle(position[1])
right_paddle = paddle.Paddle(position[0])

right_score=score.Score(score_position[0])
left_score=score.Score(score_position[1])
ball=ball.Ball()
divider=divider.Divider()
turtle.update()
screen.listen()
while True:

    game_is_on=True
    while game_is_on:
        time.sleep(0.1)
        ball.move()
        #detect collision with  up and lower wall
        if ball.ycor()>=280 or ball.ycor()<=-280:
            ball.bounce_y()
        #detect collsion with paddle
        if ball.xcor()>=350 and ball.distance(right_paddle)<50:
            ball.bounce_x()

        #detect collision with left paddle
        if ball.xcor()<=-350 and ball.distance(left_paddle)<50:
            ball.bounce_x()

        #detect if ball misses the paddle
        if ball.distance(right_paddle)>50 and ball.xcor()>400:
            time.sleep(0.4)

            ball.ball_reset()
            right_score.update()
            game_is_on=False
        if ball.distance(left_paddle) > 50 and ball.xcor()<-380:
            time.sleep(0.4)

            ball.ball_reset()
            left_score.update()
            game_is_on = False

        screen.onkey(key="w", fun=left_paddle.up)
        screen.onkey(key="s", fun=left_paddle.down)
        screen.onkey(key="Up", fun=right_paddle.up)
        screen.onkey(key="Down", fun=right_paddle.down)
        turtle.update()
screen.exitonclick()