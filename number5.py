import turtle

class number5:
    def __init__(self):
        self.position = (115, -205)

    def draw(self):
        turtle.color("#0000FF")
        turtle.penup()
        turtle.goto(self.position)
        turtle.pendown()
        turtle.setheading(180)
        turtle.forward(20)
        turtle.setheading(90)
        turtle.forward(45)
        turtle.setheading(350)
        turtle.forward(30)
        turtle.setheading(10)
        turtle.forward(30)
        turtle.penup()
        turtle.goto(self.position)
        turtle.pendown()
        turtle.setheading(330)
        turtle.forward(27)
        turtle.setheading(270)
        turtle.forward(30)
        turtle.setheading(210)
        turtle.forward(27)
        turtle.setheading(180)
        turtle.forward(20)
        turtle.setheading(135)
        turtle.forward(10)

if __name__ == '__main__':
    five=number5()
    five.draw()
