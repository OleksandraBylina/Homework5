import turtle
from number1 import number1
from number2 import number2
from number3 import number3
from number4 import number4
from number5 import number5
from number6 import number6
from number7 import number7
from number8 import number8
from number9 import number9
from number10 import number10
from number11 import number11
from number12 import number12
from arrow import arrow
class circle:
    def __init__(self):
        self.t = turtle.Turtle()

        self.one = number1()
        self.two = number2()
        self.three = number3()
        self.four = number4()
        self.five = number5()
        self.six = number6()
        self.seven = number7()
        self.eight = number8()
        self.nine = number9()
        self.ten = number10()
        self.eleven = number11()
        self.twelve = number12()
        self.arrow=arrow()
    def numbers_painter(self):
        turtle.speed(0)

        self.one.draw()
        self.two.draw()
        self.three.draw()
        self.four.draw()
        self.five.draw()
        self.six.draw()
        self.seven.draw()
        self.eight.draw()
        self.nine.draw()
        self.ten.draw()
        self.eleven.draw()
        self.twelve.draw()
    def arrower(self):
        while True:
            self.arrow.second()
    def circle(self):
        self.t.penup()
        self.t.goto(0, -300)
        self.t.pendown()
        self.t.circle(300)
        self.t.penup()

        self.numbers_painter()

        self.arrower()


if __name__ == '__main__':
    circle=circle()
    circle.circle()


