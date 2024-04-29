import os

os.system('CLS')
os.system('COLOR 1e')
os.system('VER')

#Ваша задача:
#Создайте родительский(базовый) класс Vehicle, который имеет свойство vehicle_type = "none"
#Создайте родительский(базовый) класс Car, который имеет свойство price = 1000000 и функцию def horse_powers,
#которая возвращает количество лошидиных сил для автомобиля
#Создайте наследника класса Car и Vehicle - класс Nissan и переопределите свойство price и vehicle_type,
#а также переопределите функцию horse_powers
#Создайте экзмепляр класса Nissan и распечайте через функцию print vehicle_type, price
#Получившийся код прикрепите к заданию текстом

class Vehicle:
    def __init__(self):
        self.vehicle_type = "none"

class Car(Vehicle):
    def __init__(self):
        super().__init__()
        self.price = 1500000

    def horse_powers(self):
        return 150  # Здесь можно вернуть реальные лошадиные силы автомобиля

class Nissan(Car, Vehicle):
    def __init__(self):
        super().__init__()
        self.vehicle_type = "car: Nissan, model Z350" # Переопределение свойства vehicle_type
        self.price = 12000000  # Переопределение свойства price

    def horse_powers(self):
        return 350  # Переопределение функции horse_powers

nissan_instance = Nissan()

print("Тип транспортного средства:", nissan_instance.vehicle_type)
print("Цена:", nissan_instance.price)
print("Количество лошадиных сил:", nissan_instance.horse_powers())