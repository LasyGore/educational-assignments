import os

os.system('CLS')
os.system('COLOR 1e')
os.system('VER')

#Создайте родительский(базовый) класс Car, который имеет свойство price = 1000000
#и функцию def horse_powers, которая возвращает количество лошидиных сил для автомобиля
#Создайте наследника класса Car - класс Nissan и переопределите свойство price,
# а также переопределите функцию horse_powers
#Дополнительно создайте класс Kia, который также будет наследником класса Car
#и переопределите также свойство price, а также переопределите функцию horse_powers


# Базовый класс Car
class Car:
    price = 1000000

    def horse_powers(self):
        return 300  # Пример значения лошадиных сил для всех автомобилей по умолчанию


# Наследник класса Car - класс Nissan
class Nissan(Car):
    price = 900000

    def horse_powers(self):
        return 150  # Пример значения лошадиных сил для автомобилей Nissan


# Наследник класса Car - класс Kia
class Kia(Car):
    price = 800000

    def horse_powers(self):
        return 120  # Пример значения лошадиных сил для автомобилей Kia


# Пример использования классов
car = Car()
print("Цена базового автомобиля:", car.price)
print("Лошадиные силы базового автомобиля:", car.horse_powers())

nissan_car = Nissan()
print("\nЦена автомобиля Nissan:", nissan_car.price)
print("Лошадиные силы автомобиля Nissan:", nissan_car.horse_powers())

kia_car = Kia()
print("\nЦена автомобиля Kia:", kia_car.price)
print("Лошадиные силы автомобиля Kia:", kia_car.horse_powers())