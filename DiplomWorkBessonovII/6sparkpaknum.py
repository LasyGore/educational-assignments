from pyspark.sql import SparkSession
import time
import numpy as np

# Запись времени начала выполнения
start_time = time.time()

# Инициализация SparkSession
spark = SparkSession.builder.appName("SparkApp").getOrCreate()

# Загрузка данных
spark_data = spark.read.csv('data.csv', header=True, inferSchema=True)

# Обработка данных
result = spark_data.groupBy('column').agg({'value': 'sum'}).collect()

# Время выполнения агрегации
agg_time = time.time() - start_time

# Генерация двумерных матриц 10000x10000
matrix1 = np.random.rand(10000, 10000)
matrix2 = np.random.rand(10000, 10000)

# Замер времени выполнения для транспонирования
transpose_start_time = time.time()
transposed_matrix1 = matrix1.T  # Транспонирование матрицы
transpose_time = time.time() - transpose_start_time

# Замер времени выполнения для перемножения матриц
multiply_start_time = time.time()
product_matrix = np.dot(transposed_matrix1, matrix2)  # Перемножение матриц
multiply_time = time.time() - multiply_start_time

# Общее время выполнения
total_execution_time = time.time() - start_time

# Вывод результата
print("Spark Result:")
for row in result:
    print(row)

print(f"Agg Time: {agg_time:.6f} seconds")
print(f"Transpose Time: {transpose_time:.6f} seconds")
print(f"Multiplication Time: {multiply_time:.6f} seconds")
print(f"Total Execution Time: {total_execution_time:.6f} seconds")

# Вывод размеров полученной матрицы
print(f"Product matrix shape: {product_matrix.shape}")
#Объяснение изменений:
#Генерация матриц: Созданы две матрицы размером 10000 на 10000 с использованием numpy.
#Транспонирование: Мы добавили код для транспонирования первой матрицы и замерили время выполнения этой операции.
#Перемножение матриц: Мы используем функцию np.dot() для перемножения транспонированной матрицы с второй матрицей и замеряем время этой операции.
#Вывод: Добавили вывод времени выполнения для транспонирования и перемножения, а также размер получившейся матрицы.