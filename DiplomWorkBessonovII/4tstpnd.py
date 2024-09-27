import pandas as pd
import numpy as np
import time

# Запись времени начала выполнения
start_time = time.time()

# Загрузка данных с указанием разделителя
data = pd.read_csv('data.csv', delimiter=';')

# Обработка данных
result = data.groupby('column').agg({'value': 'sum'})  # Используем правильные названия колонок

# Время выполнения агрегации
agg_time = time.time() - start_time

# Транспонирование матрицы
matrix = pd.DataFrame(np.random.rand(10000, 10000))
transposed_data = matrix.T

# Умножение матриц
matrix1 = np.random.rand(10000, 10000)
matrix2 = np.random.rand(10000, 10000)
multiplied_matrix = np.dot(matrix1, matrix2)

# Замер времени выполнения
total_execution_time = time.time() - start_time
time_matrix = total_execution_time - agg_time

# Вывод результата на экран
print("Pandas Result:")
print(result)
print(f"Время на агрегацию и сортировку данных: {agg_time:.6f} sec.")
print(f"Время на работу с матрицами: {time_matrix:.6f} sec.")
print(f"Общее время выполнения задач: {total_execution_time:.6f} sec.")

# Запись результатов в файл result.txt
with open('result.txt', 'w') as f:
    f.write("Pandas Result:\n")
    f.write(result.to_string())
    f.write(f"\nAgg Time: {agg_time:.6f} seconds\n")
    f.write(f"Matrix Time: {time_matrix:.6f} seconds\n")
    f.write(f"Total Execution Time: {total_execution_time:.6f} seconds\n")