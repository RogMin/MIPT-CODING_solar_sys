# coding: utf-8
# license: GPLv3

class Space_Body:
    """Тип данных, описывающий объект.
       Содержит массу, координаты, его скорость,
       а также визуальный радиус в пикселах и её цвет.
       """

    def __init__(self, type="", m=0, x=0, y=0, Vx=0, Vy=0, Fx=0, Fy=0, R=0, color=0):
        self.type = type
        self.m = m
        self.x = x
        self.y = y
        self.Vx = Vx
        self.Vy = Vy
        self.Fx = Fx
        self.Fy = Fy
        self.R = R
        self.color = color
        print(self)


class Star(Space_Body):
    pass


class Planet(Space_Body):
    pass
