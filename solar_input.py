# coding: utf-8
# license: GPLv3

from solar_objects import AstroObject
from solar_vis import DrawableObject


def load_objects_data(input_filename):
    """Cчитывает данные о космических объектах из файла, создаёт сами объекты
    и вызывает создание их графических образов

    """
    objects = []
    with open(input_filename, 'r', encoding="utf8") as input_file:
        for line in input_file:
            if len(line.strip()) == 0 or line[0] == '#':
                continue  # пустые строки и строки-комментарии пропускаем
            line = line.split(' ')
            obj = AstroObject()
            parse_star_object_parameters(line, obj)
            objects.append(obj)

    return [DrawableObject(obj) for obj in objects]


def parse_star_object_parameters(line, obj):
    obj.type = line[0]
    obj.R = float(line[1])
    obj.color = line[2]
    obj.m = float(line[3])
    obj.x = float(line[4])
    obj.y = float(line[5])
    obj.Vx = float(line[6])
    obj.Vy = float(line[7])
    """Считывает данные о звезде из строки.
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
    """
    return obj


def save_objects_data(output_filename, space_objects):
    """Сохраняет данные о космических объектах в файл.

    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    """
    with open(output_filename, 'w') as out_file:
        for obj in space_objects:
            print(out_file, "%s %d %s %f" % ('1', 2, '3', 4.5))
            out_file.write(f'{obj.obj.type}, {obj.obj.R}, {obj.obj.color}, {obj.obj.m}, {obj.obj.x}, {obj.obj.y}, {obj.obj.Vx}, {obj.obj.Vy},\n')

if __name__ == "__main__":
    print("This module is not for direct call!")
