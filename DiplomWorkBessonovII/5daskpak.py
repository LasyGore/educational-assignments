import dask.dataframe as dd
import time
import dask.array as da
import dask

dask.config.set({'array.blockwise-optimize': True})  # Включает оптимизацию

# Запись времени начала выполнения
start_time = time.time()

# Загрузка данных с указанием разделителя
dask_data = dd.read_csv('data.csv', delimiter=';', blocksize='64MB')
# Проверка столбцов
print(dask_data.columns)

# Обработка данных
result = dask_data.groupby('column').agg({'value': 'sum'}).compute().sort_index()
# Время выполнения агрегации
agg_time = time.time() - start_time

# Транспонирование матрицы
dask_matrix = da.random.random((10000, 10000), chunks=(1000, 1000))
transposed_data = dask_matrix.T

# Умножение матриц
matrix1 = da.random.random((10000, 10000), chunks=(1000, 1000))
matrix2 = da.random.random((10000, 10000), chunks=(1000, 1000))
multiplied_matrix = da.dot(matrix1, matrix2)

# Замер времени выполнения
total_execution_time = time.time() - start_time
tr_time=total_execution_time-agg_time

# Вывод результата
print("Dask Result:")
print(result)
print(f"Agg Time: {agg_time:.6f} seconds")
print(f"Matr Time: {tr_time:.6f} seconds")
print(f"Total Execution Time: {total_execution_time:.6f} seconds")