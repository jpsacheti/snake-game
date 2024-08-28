from turtle import Turtle
import time

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for i in range(3):
            coordinates = (i * -20, 0)
            self.create_single_segment(coordinates)

    def extend_snake(self):
        self.create_single_segment(self.segments[-1].position())

    def collided_with_self(self):
        for seg in self.segments[1:]:
            if self.head.distance(seg) < 10:
                return True
        return False

    def create_single_segment(self, position: (int, int) = (0, 0)):
        snake_segment = Turtle(shape="square")
        snake_segment.color("white")
        snake_segment.penup()
        snake_segment.goto(position)
        self.segments.append(snake_segment)

    def get_new_coordinates(self, index):
        return self.segments[index - 1].xcor(), self.segments[index - 1].ycor()

    def move(self):
        time.sleep(0.1)
        for i in range(len(self.segments) - 1, 0, -1):
            new_x, new_y = self.get_new_coordinates(i)
            self.segments[i].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() == DOWN:
            return
        self.head.setheading(UP)

    def down(self):
        if self.head.heading() == UP:
            return
        self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() == LEFT:
            return
        self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() == RIGHT:
            return
        self.head.setheading(LEFT)

    def collided_with_wall(self):
        if self.head.xcor() > 290 or self.head.xcor() < -290 or self.head.ycor() > 290 or self.head.ycor() < -290:
            return True
        return False
