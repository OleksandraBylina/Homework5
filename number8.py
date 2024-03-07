import turtle

class number8:
    def __init__(self):
        self.position = (-205, -120)

    def draw(self):
        turtle.color("#FFA500")
        turtle.penup()
        turtle.goto(self.position)
        turtle.pendown()
        turtle.setheading(30)
        turtle.forward(30)
        turtle.setheading(90)
        turtle.forward(30)
        turtle.setheading(150)
        turtle.forward(30)
        turtle.setheading(210)
        turtle.forward(30)
        turtle.setheading(270)
        turtle.forward(30)
        turtle.setheading(330)
        turtle.forward(30)
        turtle.penup()
        turtle.goto(self.position)
        turtle.pendown()
        turtle.setheading(330)
        turtle.forward(30)
        turtle.setheading(270)
        turtle.forward(30)
        turtle.setheading(210)
        turtle.forward(30)
        turtle.setheading(150)
        turtle.forward(30)
        turtle.setheading(90)
        turtle.forward(30)
        turtle.setheading(30)
        turtle.forward(30)

if __name__ == '__main__':
    eight=number8()
    eight.draw()
