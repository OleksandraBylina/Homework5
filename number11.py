import turtle

class number11:
    def __init__(self):
        self.position = (-125, 205)

    def draw(self):
        turtle.color("#0000FF")
        turtle.penup()
        turtle.goto(self.position)
        turtle.pendown()
        turtle.up()
        turtle.setheading(180)
        turtle.forward(13)
        turtle.down()
        turtle.setheading(90)
        turtle.forward(38)
        turtle.setheading(225)
        turtle.forward(38)
        turtle.penup()
        turtle.goto(self.position[0]-13, self.position[1])
        turtle.pendown()
        turtle.setheading(270)
        turtle.forward(38)

        turtle.setheading(0)
        turtle.forward(15)
        turtle.back(38)
        turtle.penup()
        turtle.goto(self.position[0]+50, self.position[1])
        turtle.up()
        turtle.setheading(180)
        turtle.forward(13)
        turtle.down()
        turtle.setheading(90)
        turtle.forward(38)
        turtle.setheading(225)
        turtle.forward(38)
        turtle.penup()
        turtle.goto(self.position[0] +37, self.position[1])
        turtle.pendown()
        turtle.setheading(270)
        turtle.forward(38)
        turtle.setheading(0)
        turtle.forward(15)
        turtle.back(38)


if __name__ == '__main__':
    eleven=number11()
    eleven.draw()
