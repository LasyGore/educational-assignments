import random
import time


# Генерация матрицы 1000 на 1000 с случайными действительными числами
def generate_matrix(size):
    return [[random.uniform(10, 100) for _ in range(size)] for _ in range(size)]


# Перемножение двух матриц
def multiply_matrices(matrix_a, matrix_b):
    size = len(matrix_a)
    result = [[0.0 for _ in range(size)] for _ in range(size)]

    for i in range(size):
        for j in range(size):
            element_sum = 0.0
            for k in range(size):
                element_sum += matrix_a[i][k] * matrix_b[k][j]
            result[i][j] = element_sum

    return result


# Основная программа
if __name__ == "__main__":
    size = 1000

    # Генерация двух матриц
    matrix_a = generate_matrix(size)
    matrix_b = generate_matrix(size)

    # Измерение времени выполнения операции перемножения
    start_time = time.time()
    result_matrix = multiply_matrices(matrix_a, matrix_b)
    end_time = time.time()

    # Печать результата
    print(f"Время выполнения операции умножения матриц: {end_time - start_time:.4f} секунд")