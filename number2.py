import turtle

class number2:
    def __init__(self):
        self.position = (205, 125)

    def draw(self):
        turtle.color("#FFA500")
        turtle.penup()
        turtle.goto(self.position)
        turtle.pendown()
        turtle.setheading(60)
        turtle.forward(40)
        turtle.setheading(135)
        turtle.forward(20)
        turtle.setheading(180)
        turtle.forward(20)
        turtle.setheading(225)
        turtle.forward(20)
        turtle.penup()
        turtle.goto(self.position)
        turtle.pendown()
        turtle.setheading(240)
        turtle.forward(40)
        turtle.setheading(135)
        turtle.forward(13)

        turtle.setheading(45)
        turtle.forward(13)
        turtle.setheading(330)
        turtle.forward(38)
        turtle.setheading(45)
        turtle.forward(20)

if __name__ == '__main__':
    two=number2()
    two.draw()
