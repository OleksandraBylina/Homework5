import turtle

class number4:
    def __init__(self):
        self.position = (205, -120)

    def draw(self):
        turtle.color("#008000")
        turtle.penup()
        turtle.goto(self.position)
        turtle.pendown()
        turtle.setheading(180)
        turtle.forward(30)
        turtle.setheading(60)
        turtle.forward(60)
        turtle.setheading(270)
        turtle.forward(100)
        turtle.penup()
        turtle.goto(self.position)
        turtle.pendown()
        turtle.setheading(0)
        turtle.forward(30)
        turtle.setheading(90)
        turtle.forward(10)
        turtle.setheading(270)
        turtle.forward(20)
        turtle.penup()
        turtle.goto(self.position)
        turtle.pendown()
        turtle.forward(20)
        turtle.setheading(270)
        turtle.forward(30)
        turtle.setheading(0)
        turtle.forward(15)
        turtle.setheading(180)
        turtle.forward(30)

if __name__ == '__main__':
    four=number4()
    four.draw()
