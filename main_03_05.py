import os
os.system('CLS')
os.system('COLOR 1e')
os.system('VER')
#Всем привет повторю домашнее задание к модулю 6 тут
#Необходимо разработать задачу по нижеперечисленным условиям.
#Нужно написать класс Дом с Подъездами (от 1 до 6 - выбирается случайным образом) и Этажами (от 5 до 12 - выбирается
#случайным образом), на каждом Этаже по 2,3 или 4 Квартиры - выбирается случайным образом для дома в целом.
#Нужно вывести сколько квартир находится в указанном доме. Создать 12 отличающихся друг от друга экземпляров и сравнить
#их между собой по этажности и количеству квартир. Вывести отчет по признаку  этажности,
# вывести отчет по признаку количества подъездов, вывести отчет по признаку количества квартир.
#Далее нужно посчитать сколько домов находится в районе всего
#и нужно посчитать сколько суммарно всего квартир в домах.
# Отправить в личку в телегу ссылку на git

import random

class House:
    def __init__(self, entrances, floors, apartments_per_floor):
        self.entrances = entrances
        self.floors = floors
        self.apartments_per_floor = apartments_per_floor

    def total_apartments(self):
        return self.entrances * self.floors * self.apartments_per_floor

# Создание 12 экземпляров класса House
houses = []
for _ in range(12):
    entrances = random.randint(1, 6)
    floors = random.randint(5, 12)
    apartments_per_floor = random.choice([2, 3, 4])
    house = House(entrances, floors, apartments_per_floor)
    houses.append(house)
    print('Дом с', entrances, 'подЪездами, этажей',floors, ', по', apartments_per_floor, ' квартир на этаже.')
    print(' ')

# Сравнение экземпляров между собой по этажности и количеству квартир
floors_report = {i: 0 for i in range(5, 13)}
entrances_report = {i: 0 for i in range(1, 7)}
apartments_report = {i: 0 for i in range(2, 5)}

total_houses_in_area = len(houses)
total_apartments_in_area = 0

for house in houses:
    floors_report[house.floors] += 1
    entrances_report[house.entrances] += 1
    apartments_report[house.apartments_per_floor] += 1
    total_apartments_in_area += house.total_apartments()

# Вывод отчетов
print('Отчет по этажности:')
for floors, count in floors_report.items():
    print(f'Домов с {floors} этажами: {count}')

print('\nОтчет по количеству подъездов:')
for entrances, count in entrances_report.items():
    print(f'Домов с {entrances} подъездами: {count}')

print('\nОтчет по количеству квартир на этаже:')
for apartments, count in apartments_report.items():
    print(f'Домов с {apartments} квартирами на этаже: {count}')

print(f'\nВ районе всего {total_houses_in_area} домов')

print(f'Суммарно всего {total_apartments_in_area} квартир в домах')