import os
os.system('CLS')
os.system('COLOR 1e')
os.system('VER')

#Ваша задача:
#Создайте новый класс Buiding
#Создайте инициализатор для класса Buiding, который будет задавать целочисленный атрибут этажности
#self.numberOfFloors и строковый атрибут self.buildingType
#Создайте(перегрузите) __eq__, используйте атрибут numberOfFloors и buildingType для сравнения
#Полученный код напишите в ответ к домашему заданию


class Building:
    def __init__(self, number_of_floors, building_type):
        self.number_of_floors = number_of_floors
        self.building_type = building_type

    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors and self.building_type == other.building_type