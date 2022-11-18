# coding: utf-8
# license: GPLv3

class Space_Body:
    """Тип данных, описывающий объект.
       Содержит массу, координаты, его скорость,
       а также визуальный радиус в пикселах и её цвет.
       """
    def __init__(self, type, m, x, y, Vx, Vy, Fx, Fy, R, color):
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


class Star(Space_Body):
    pass


class Planet(Space_Body):
    pass
