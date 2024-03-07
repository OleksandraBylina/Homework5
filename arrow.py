import turtle
import time
class arrow:
    def second(self):
        turtle.penup()
        turtle.goto(0, 0)
        turtle.pendown()
        turtle.color("#000000")
        for i in range(0, 360, 6):
            turtle.speed(0)

            turtle.goto(0, 0)
            turtle.setheading(90-i)
            turtle.forward(150)
            time.sleep(1)
            turtle.undo()
if __name__ == '__main__':
    arrow=arrow()
    arrow.second()