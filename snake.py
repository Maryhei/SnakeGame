from turtle import Turtle

START_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.place = []
        self.create_snake()
        self.head = self.place[0]


    def create_snake(self):
        for position in START_POSITION:
            self.add(position)

    def add(self, position):
        hei = Turtle(shape="square")
        hei.color("white")
        hei.penup()
        hei.goto(position)
        self.place.append(hei)


    def extend(self):
        self.add(self.place[-1].position())



    def move(self):
        for new_position in range(len(self.place) - 1, 0, -1):
            new_x = self.place[new_position - 1].xcor()
            new_y = self.place[new_position - 1].ycor()
            self.place[new_position].goto(new_x, new_y)
        self.head.forward(MOVE)

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

    def reset(self):
        self.setposition(0, 0)
        self.create_snake()