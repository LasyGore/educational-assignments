
import os
os.system('CLS')
os.system('COLOR 1e')
os.system('VER')
#Домашнее задание по уроку "Пространство имен"
#Создайте новый проект в PyCharm. Запустите созданный проект.
#Ваша задача:
#Создайте новый класс House
#Создайте инициализатор для класса House, который будет задавать атрибут этажности self.numberOfFloors = 0
#Создайте метод setNewNumberOfFloors(floors), который будет изменять атрибут numberOfFloors на параметр
# floors и выводить в консоль numberOfFloors
#Полученный код напишите в ответ к домашему заданию




class House:
    def __init__(self):
        self.numberOfFloors = 0

    def setNewNumberOfFloors(self, floors):
        self.numberOfFloors = floors
        print("Number of floors:", self.numberOfFloors)


# Пример использования класса House
myHouse = House()
#myHouse.setNewNumberOfFloors(3)
# Вызов метода для изменения этажности и вывода в консоль
num_flo=int(input ("Укажите требуемую этажность:"))
myHouse.setNewNumberOfFloors(num_flo)