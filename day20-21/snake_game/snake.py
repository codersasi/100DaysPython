from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.turtles = []
        self.create_snake()
        self.head: Turtle = self.turtles[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_turtle(position)

    def add_turtle(self, position):
        new_tutle = Turtle("square")
        new_tutle.penup()
        new_tutle.color("white")
        new_tutle.goto(position)
        self.turtles.append(new_tutle)

    def extend(self):
        self.add_turtle(self.turtles[-1].position())

    def move(self):
        for turtle_index in range(len(self.turtles) - 1, 0, -1):
            new_x = self.turtles[turtle_index - 1].xcor()
            new_y = self.turtles[turtle_index - 1].ycor()
            self.turtles[turtle_index].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

