import turtle

from random import randint
from math import sin, cos,  radians
import pygame

class Triangle:
    default_color = "#ACDC43"

    def __init__(self, x1, y1, x2, y2, x3, y3, x, y): #
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3
        self.y1 = y1
        self.y2 = y2
        self.y3 = y3
        self.x = x
        self.y = y
        self.color = Triangle.default_color
        self.point_turtle = turtle.Turtle()

        self.position = (0, 0)
    def circle(self, radius): # рисует кружок, на котором будет храниться вершина треугольника
        t = turtle.Turtle() #
        t.speed(0)
        t.penup()
        t.goto(self.x, self.y-radius) #конкретна точка буде встановлена пізніше
        t.pendown()
        t.circle(radius) #намалювали коло
    def running_turtle(self, radius):

        self.point_turtle.shape("circle")
        self.point_turtle.color("ACDC43")
        self.point_turtle.penup()
        for angle in range(0, 360):  # Проходим по всем углам от 0 до 360 градусов
            # Вычисляем координаты точки на окружности для текущего угла
            point_x = self.x + radius * cos(radians(angle))
            point_y = self.y + radius * sin(radians(angle))
            self.point_turtle.goto(point_x, point_y)




    def calculator(self, radius):
        self.point_turtle.shape("circle")
        self.point_turtle.penup()

        for angle in range(0, 360, 10):  # Проходим по всем углам от 0 до 360 градусов
            # Вычисляем координаты точки на окружности для текущего угла

            point_x = self.x + radius * cos(radians(angle))
            point_y = self.y + radius * sin(radians(angle))

            # Перемещаем точку на новые координаты
            self.point_turtle.goto(point_x, point_y)

            # Изменяем координаты треугольника для следующей итерации
            self.x1, self.y1 = self.rotate_point(self.x1, self.y1, self.x, self.y, 1)
            self.x2, self.y2 = self.rotate_point(self.x2, self.y2, self.x, self.y, 1)
            self.x3, self.y3 = self.rotate_point(self.x3, self.y3, self.x, self.y, 1)

            # Рисуем треугольник
            self.point_turtle.penup()
            self.point_turtle.goto(self.x1, self.y1)
            self.point_turtle.pendown()
            self.point_turtle.goto(self.x2, self.y2)
            self.point_turtle.goto(self.x3, self.y3)
            self.point_turtle.goto(self.x1, self.y1)
            self.point_turtle.penup()# Возвращаемся к начальной точке треугольника

    def rotate_point(self, x, y, cx, cy, angle):
        # Поворачиваем точку (x, y) относительно центра (cx, cy) на заданный угол
        angle_rad = radians(angle)
        new_x = cx + (x - cx) * cos(angle_rad) - (y - cy) * sin(angle_rad)
        new_y = cy + (x - cx) * sin(angle_rad) + (y - cy) * cos(angle_rad)
        return new_x, new_y

    def radius(self):
        radius1=(((self.x-self.x1))**2+(self.y-self.y1)**2)**0.5
        radius2 = ((self.x-self.x2)**2+(self.y-self.y2)**2)**0.5
        radius3 = ((self.x-self.x3)**2+(self.y-self.y3)**2)**0.5
        pust=[]
        difpust=[]
        if isinstance(radius1, complex):

            result_list = [round(radius1.real, 8), round(radius1.imag, 8)]
            res=max(result_list)
            pust.append(res)
        else:

            difpust.append(round(radius1, 8))
        if isinstance(radius2, complex):

            result_list = [round(radius2.real, 8), round(radius2.imag, 8)]
            ress=max(result_list)
            pust.append(ress)
        else:

            difpust.append(round(radius2, 8))
        if isinstance(radius3, complex):

            result_list = [round(radius3.real, 8), round(radius3.imag, 8)]
            ressy=max(result_list)
            pust.append(ressy)
        else:

            difpust.append(round(radius3, 8))
        merged_list=pust+difpust
        return merged_list
    def play_music(self, start_time):
        pygame.mixer.init()
        pygame.mixer.music.load("You_spin_me_round.mp3")
        pygame.mixer.music.play(start=start_time)
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

if __name__ == '__main__':
    a=randint(-100,100)
    b=randint(-100,100)
    c=randint(-100,100)
    d=randint(-100,100)
    e=randint(-100,100)
    f=randint(-100, 100)
    triangle = Triangle(a, b, c, d, e, f, 50, 60)

    radiant = triangle.radius()
    triangle.circle(radiant[0])
    triangle.circle(radiant[1])
    triangle.circle(radiant[2])
    triangle.calculator(radiant[0])
    triangle.calculator(radiant[1])
    triangle.calculator(radiant[2])

    turtle.mainloop()




