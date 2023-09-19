from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()

    def move_ball(self):
        new_x_position = self.xcor() + 10
        new_y_position = self.ycor() + 10
        self.goto(new_x_position, new_y_position)
