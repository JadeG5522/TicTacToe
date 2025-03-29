from turtle import Turtle

coordinates = {
    7:   [-150,150],
    8:    [0,150],
    4:    [-150,0],
    5:    [0,0],
    1:   [-150,-150],
    2:    [0,-150],
    3:   [150,-150],
    9:   [150,150],
    6:    [150,0],
}

class SetUp(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.move(x= -225, y=75)
        self.move(x=-225, y=-75)
        self.setheading(270)
        self.move(x=-75, y=225)
        self.move(x=75, y=225)



    def move(self, x, y):
        self.teleport(x, y)
        self.forward(450)



class Moving(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pensize(3)
        self.times = 0

    def draw_circle(self, x, y):
        self.teleport(x, y-70)
        self.circle(71)
        self.times +=1

    def draw_cross(self, x, y):
        self.teleport(x-70, y+70)
        self.goto(x+70, y-70)
        self.teleport(x-70, y-70)
        self.goto(x+70, y+70)
        self.times += 1

    def draw_shape(self, location, player):
        xcor = coordinates[location][0]
        ycor = coordinates[location][1]
        if player == 1:
            self.draw_cross(xcor,ycor)
        else:
            self.draw_circle(xcor,ycor)


