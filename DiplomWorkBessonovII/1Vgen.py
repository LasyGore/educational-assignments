import random
import time

# Задаем длину списка
# Вы можете изменить это значение(скорость примерно сортировки 55000 целых чисел в минуту)
length_of_list = 60000
start_time = time.time()

# Генерируем список псевдослучайных целых чисел
random_list = [random.randint(10, 99) for _ in range(length_of_list)]

#print(random_list)


def select_sort(random_list):
    for i in range(len(random_list) - 1):
        min_index = i
        for k in range(i + 1, len(random_list)):
            if random_list[k] < random_list[min_index]:
                min_index = k
        random_list[i], random_list[min_index] = random_list[min_index], random_list[i]
    return random_list


b = select_sort(random_list)

# print(b)


print("Расчет окончен! Затрачено:")
sort_time = time.time() - start_time
print(int(sort_time))
print("секунд на:")
print(length_of_list, " записей.")
print("Это Очень Медленно!!!")