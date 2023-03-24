# Реализовать дескрипторы для любых двух классов
"""
Реализовать базовый класс Worker (работник),
в котором определить публичные атрибуты name, surname, position (должность),
и защищенный атрибут income (доход). Последний атрибут должен ссылаться
на словарь, содержащий элементы: оклад и премия, например,
{"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker. В классе Position
реализовать публичные методы
получения полного имени сотрудника (get_full_name) и дохода с учетом премии
(get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса
Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров).
П.С. попытайтесь добить вывода информации о сотруднике также через перегрузку
str
str(self) - вызывается функциями str, print и format.
 Возвращает строковое представление объекта.
"""
# Реализовать дескриптор класса


class TypeSt:

    def __set__(self, instance, value):
        if type(value) != str:
            raise ValueError("Должно иметь строковый тип!")
        instance.__dict__[self.my_attr] = value

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr


class Worker:
    name = TypeSt()
    surname = TypeSt()
    position = TypeSt()

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}
        print(self._income)


class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return f'Полное имя: {self.surname} {self.name}'

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']

    def __str__(self):
        return 'Star Wars'


worker1 = Position('Лея', 'Органа', 'princes', 750, 80)
#worker2 = Position(453, 'Скайуокер', 'jedi', 349, 90)
print(worker1)
print(worker1.get_full_name())
print(f'Total income: {worker1.get_total_income()}')
print(worker1.position)

#print(worker2.get_full_name())
#print(f'Total income: {worker2.get_total_income()}')
#print(worker2.position)