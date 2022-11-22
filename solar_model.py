# coding: utf-8
# license: GPLv3
import numpy

gravitational_constant = 6.67408E-11
"""Гравитационная постоянная Ньютона G"""


def calculate_force(body, space_objects):
    """Вычисляет силу, действующую на тело.

    Параметры:

    **body** — тело, для которого нужно вычислить дейстующую силу.

    **space_objects** — список объектов, которые воздействуют на тело.
    """
    for obj in space_objects:
        if body == obj:
            continue  # тело не действует гравитационной силой на само себя!
        r = ((body.x - obj.x) ** 2 + (body.y - obj.y) ** 2) ** 0.5
        #r = max(r, body.R)  # FIXME: обработка аномалий при прохождении одного тела сквозь другое
        if r == 0:
            return
        if r - body.R:
            body.Fx = (gravitational_constant * body.m * obj.m * (r**-3)) * (obj.x - body.x)
            body.Fy = (gravitational_constant * body.m * obj.m * (r**-3)) * (obj.y - body.y)
            print(body.Fx, body.Fx)
        else:

            body.Vx = -body.Vx
            body.Vy = -body.Vy



def move_space_object(body, dt):
    """Перемещает тело в соответствии с действующей на него силой.

    Параметры:

    **body** — тело, которое нужно переместить.
    """
    ax = body.Fx / body.m
    body.Vx += ax * dt
    body.x += body.Vx

    ay = body.Fy / body.m
    body.Vy += ay * dt
    body.y += body.Vy

    print(body.Vx, body.Vy, body.Vy / body.Vy)
def recalculate_space_objects_positions(space_objects, dt):
    """Пересчитывает координаты объектов.

    Параметры:

    **space_objects** — список оьъектов, для которых нужно пересчитать координаты.

    **dt** — шаг по времени
    """
    for body in space_objects:
        calculate_force(body, space_objects)
    for body in space_objects:
        move_space_object(body, dt)


if __name__ == "__main__":
    print("This module is not for direct call!")
