import turtle

class number7:
    def __init__(self):
        self.position = (-115, -205)

    def draw(self):
        turtle.color("#FF0000")
        turtle.penup()
        turtle.goto(self.position)
        turtle.pendown()
        turtle.setheading(70)
        turtle.forward(60)
        turtle.setheading(190)
        turtle.forward(15)
        turtle.setheading(170)
        turtle.forward(15)
        turtle.setheading(225)
        turtle.forward(15)
        turtle.penup()
        turtle.goto(self.position)
        turtle.pendown()
        turtle.setheading(0)
        turtle.forward(15)
        turtle.setheading(180)
        turtle.forward(30)
        turtle.setheading(0)
        turtle.forward(15)
        turtle.setheading(250)
        turtle.forward(45)

if __name__ == '__main__':
    seven=number7()
    seven.draw()
