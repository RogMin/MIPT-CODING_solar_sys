# coding: utf-8
# license: GPLv3

import pygame as pg

"""Модуль визуализации.
Нигде, кроме этого модуля, не используются экранные координаты объектов.
Функции, создающие гaрафические объекты и перемещающие их на экране, принимают физические координаты
"""

header_font = "Arial-16"
"""Шрифт в заголовке"""

window_width = 900
"""Ширина окна"""

window_height = 12
"""Высота окна"""

scale_factor = 1
"""Масштабирование экранных координат по отношению к физическим.

Тип: float

Мера: количество пикселей на один метр."""


def calculate_scale_factor(max_distance):
    """Вычисляет значение глобальной переменной **scale_factor** по данной характерной длине"""
    global scale_factor
    scale_factor = 0.5*min(window_height, window_width)/max_distance
    print('Scale factor:', scale_factor)


def scale_x(x):
    """Возвращает экранную **x** координату по **x** координате модели.
    Принимает вещественное число, возвращает целое число.
    В случае выхода **x** координаты за пределы экрана возвращает
    координату, лежащую за пределами холста.

    Параметры:

    **x** — x-координата модели.
    """

    return int(x*scale_factor) + window_width//2


def scale_y(y):
    """Возвращает экранную **y** координату по **y** координате модели.
    Принимает вещественное число, возвращает целое число.
    В случае выхода **y** координаты за пределы экрана возвращает
    координату, лежащую за пределами холста.
    Направление оси развёрнуто, чтобы у модели ось **y** смотрела вверх.

    Параметры:

    **y** — y-координата модели.
    """
    # pass  #FIXME
    return int(y*scale_factor) + window_height // 2



if __name__ == "__main__":
    print("This module is not for direct call!")


class Drawer:
    def __init__(self, screen = 0, objects = []):
        self.screen = screen
        self.objects = objects

    def draw(self, object):
        self.objects.append(object)
        self.update(self.objects)

    def update(self, figures):
        self.screen.fill((0, 0, 0))

        for figure in figures:
            pg.draw.circle(self.screen, figure.color, (int(figure.x), int(figure.y)), figure.R)
        #self.screen.blit()
        #self.screen.update()
        pg.display.update()

