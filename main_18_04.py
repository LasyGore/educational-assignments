#Создайте новый проект в PyCharm
#Запустите созданный проект
#Ваша задача:
#Создайте новый класс House
#Задайте ему новый атрибут numberOfFloors = 10
#В цикле пройдитесь по атрибуту numberOfFloors и распечайте значение "Текущий этаж равен"
#Полученный код напишите в ответ к домашему заданию

import os
os.system('CLS')
os.system('COLOR 1e')
os.system('VER')

class House:
    def __init__(self):
        self.numberOfFloors = 10

house = House()
for floor in range(1, house.numberOfFloors + 1):
    print(f"Текущий этаж равен {floor}")