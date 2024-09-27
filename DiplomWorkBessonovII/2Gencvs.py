import csv
import random
import time

# Начинаем замер времени
start_time = time.time()

# Запрашиваем количество строк у пользователя
num_lines = int(input("Введите количество строк для записи в файл: "))

# Создаем или открываем файл data.csv для записи
with open('data.csv', mode='w', newline='') as file:
    writer = csv.writer(file, delimiter=';')  # Используем ; в качестве разделителя

    # Записываем заголовки
    writer.writerow(['column', 'value'])

    for _ in range(num_lines):
        # Генерируем два случайных двухзначных числа
        num1 = random.randint(10, 99)
        num2 = random.randint(10, 99)

        # Записываем числа в файл
        writer.writerow([num1, num2])

# Заканчиваем замер времени
end_time = time.time()
execution_time = end_time - start_time

print(f"Успешно записано {num_lines} строк в файл data.csv.")
print(f"Время выполнения программы: {execution_time:.4f} секунд.")