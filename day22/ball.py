from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.step_x = 10
        self.step_y = 10

    def move(self):
        new_x = self.xcor() + self.step_x
        new_y = self.ycor() + self.step_y
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.step_y *= -1

    def bounce_x(self):
        self.step_x *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()
