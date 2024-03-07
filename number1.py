import turtle

class number1:
    def __init__(self):
        self.position = (125, 205)

    def draw(self):
        turtle.color("#FF0000")
        turtle.penup()
        turtle.goto(self.position)
        turtle.pendown()
        turtle.setheading(90)
        turtle.forward(38)
        turtle.setheading(225)
        turtle.forward(38)
        turtle.penup()
        turtle.goto(self.position)
        turtle.pendown()
        turtle.setheading(270)
        turtle.forward(38)

        turtle.setheading(0)
        turtle.forward(18)
        turtle.back(38)
        #turtle.penup()

if __name__ == '__main__':
    one=number1()
    one.draw()
