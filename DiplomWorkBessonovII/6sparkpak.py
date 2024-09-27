from pyspark.sql import SparkSession
import time

# Инициализация SparkSession
#spark = SparkSession.builder.appName("SparkApp").getOrCreate()
spark = SparkSession.builder \
    .appName("SparkApp") \
    .config("spark.driver.extraJavaOptions", "-D java.security.manager=allow") \
    .getOrCreate()

# Запись времени начала выполнения
start_time = time.time()

# Загрузка данных
spark_data = spark.read.csv('data.csv', header=True, inferSchema=True)

# Обработка данных
result = spark_data.groupBy('column').agg({'value': 'sum'}).collect()

# Время выполнения агрегации
agg_time = time.time() - start_time

# Создание двумерных матриц 10000x10000 в виде DataFrame
rows1 = [(i, j, float(i + j)) for i in range(10000) for j in range(10000)]
rows2 = [(i, j, float(i * j)) for i in range(10000) for j in range(10000)]

matrix1 = spark.createDataFrame(rows1, ["row", "col", "value"])
matrix2 = spark.createDataFrame(rows2, ["row", "col", "value"])

# Замер времени выполнения для транспонирования
transpose_start_time = time.time()
transposed_matrix1 = matrix1.groupBy("col").pivot("row").agg({"value": "first"})  # Транспонирование
transpose_time = time.time() - transpose_start_time

# Замер времени выполнения для перемножения матриц
multiply_start_time = time.time()

# Получение транспонированной матрицы как RDD для умножения
transposed_rdd = transposed_matrix1.rdd.map(lambda row: row.asDict()).collect()
matrix1_as_dict = {row['row']: row for row in transposed_rdd}

# Функция для умножения матриц
def matrix_multiplication(row):
    result = []
    for col in range(10000):
        sum_product = sum(matrix1_as_dict.get(r, {}).get(col, 0) * matrix2.filter(matrix2.row == r).filter(matrix2.col == col).select("value").first()[0]
                          for r in range(10000))
        result.append((row[0], col, sum_product))
    return result

product_rdd = matrix1.rdd.map(matrix_multiplication).flatMap(lambda x: x)

# Перевод результата обратно в DataFrame
product_matrix = product_rdd.toDF(["row", "col", "value"])

multiply_time = time.time() - multiply_start_time

# Общее время выполнения
total_execution_time = time.time() - start_time

# Вывод результата
print("Результат Spark:")
for row in result:
    print(row)

print(f"Время агрегации: {agg_time:.6f} секунды")
print(f"Время транспонирования: {transpose_time:.6f} секунды")
print(f"Время умножения: {multiply_time:.6f} секунды")
print(f"Общее время выполнения: {total_execution_time:.6f} секунды")

# Вывод размеров полученной матрицы
print(f"Количество в результирующей матрице: {product_matrix.count()}")