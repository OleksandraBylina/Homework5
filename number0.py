import turtle

class number0:
    def __init__(self):
        self.position = (0, 0)

    def draw(self):
        turtle.penup()
        turtle.forward(30)
        turtle.pendown()
        turtle.setheading(90)
        turtle.forward(60)
        turtle.setheading(135)
        turtle.forward(30)
        turtle.setheading(180)
        turtle.forward(50)
        turtle.setheading(225)
        turtle.forward(30)
        turtle.setheading(270)
        turtle.forward(120)
        turtle.setheading(315)
        turtle.forward(30)
        turtle.setheading(0)
        turtle.forward(50)
        turtle.setheading(45)
        turtle.forward(30)
        turtle.setheading(90)
        turtle.forward(60)
        turtle.mainloop()
if __name__ == '__main__':
    zero=number0()
    zero.draw()
