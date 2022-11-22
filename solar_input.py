# coding: utf-8
# license: GPLv3

from solar_objects import Star, Planet




def read_space_objects_data_from_file(input_filename,Drawer):
    """Cчитывает данные о космических объектах из файла, создаёт сами объекты
    и вызывает создание их графических образов

    Параметры:

    **input_filename** — имя входного файла
    """

    objects = []
    with open(input_filename, 'r', encoding="utf8") as input_file:
        for line in input_file.readlines():
            if len(line.strip()) == 0 or line[0] == '#':
                continue  # пустые строки и строки-комментарии пропускаем
            object_type = line.split()[0].lower()
            line = line.split(' ')
            if object_type == "star":
                star = Star()
                parse_object_parameters(line, star)
                objects.append(star)
            elif object_type == "planet":
                planet = Planet()
                parse_object_parameters(line, planet)
                objects.append(planet)
            else:
                print("Unknown space object")
    Drawer.draw(objects)
    return objects


def parse_object_parameters(line, obj):
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


def write_space_objects_data_to_file(output_filename, space_objects):
    """Сохраняет данные о космических объектах в файл.

    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
]
    Параметры:

    **output_filename** — имя входного файла

    **space_objects** — список объектов планет и звёзд
    """
    with open(output_filename, 'w') as out_file:
        for obj in space_objects:
            print(out_file, "%s %d %s %f" % ('1', 2, '3', 4.5))
            out_file.write(f'{str(obj.type)}, {obj.R}, {obj.color}, {obj.m}, {obj.x}, {obj.y}, {obj.Vx}, {obj.Vy}')


if __name__ == "__main__":
    print("This module is not for direct call!")
