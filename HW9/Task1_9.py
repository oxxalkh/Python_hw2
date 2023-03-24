"""
Задание 2.
Реализовать класс Road (дорога), в котором определить защищенные атрибуты:
length (длина в метрах), width (ширина в метрах).
Значения данных атрибутов должны передаваться при создании экземпляра класса.
Реализовать публичный метод расчета массы асфальта, необходимого для покрытия
всего дорожного полотна.
Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв
метра дороги асфальтом, толщиной в 1 см * число м толщины полотна.
Массу и толщину сделать публичными атрибутами.
Проверить работу метода.
Например: 20м*5000м*25кг*0.05м = 125000 кг = 125 т
"""
# Реализовать дескриптор класса


class VerifNum:
    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr

    def __set__(self, instance, value):
        if type(value) != int:
            raise ValueError('Должно быть числом!')
        if value < 0:
            raise ValueError('Должно быть положительным числом!')
        instance.__dict__[self.my_attr] = value


class Road:
    _length = VerifNum()
    _width = VerifNum()

    weight_kg_m2 = 25  # кг/см - вес одного квадратного метра толщиной в
    # 1 см
    depth = 0.05  # число м толщины полотна

    def __init__(self, length, width):
        self._length = length
        self._width = width
        print(f"Дорожное полотно {self._length} * {self._width}")

    def weight(self):
        return road.depth * road.weight_kg_m2 * self._width * self._length


road = Road(5000, 20)
print(f'Масса асфальта, необходимого для покрытия всего дорожного полотна'
      f' {road.weight()} kg, {(road.weight())/1000} t ')
