# Создание собственных исключений
class InvalidDataException(Exception):
    """Исключение для неверных данных."""
    pass

class ProcessingException(Exception):
    """Исключение для ошибок обработки данных."""
    pass

# Функция, которая генерирует исключения
def process_data(data):
    if not isinstance(data, int):
        raise InvalidDataException("Переданные данные не являются целым числом.")
    if data < 0:
        raise ProcessingException("Обработка отрицательных чисел не поддерживается.")
    return data * 2

# Функция, вызывающая process_data и обрабатывающая исключения
def handle_data(data):
    try:
        result = process_data(data)
    except InvalidDataException as e:
        print(f"Ошибка в данных: {e}")
        raise  # Передача исключения дальше
    except ProcessingException as e:
        print(f"Ошибка обработки: {e}")
        raise  # Передача исключения дальше
    else:
        print("Обработка данных прошла успешно.")
    finally:
        print("Завершение работы с данными.")

# Основная часть программы
if __name__ == "__main__":
    try:
        handle_data("abc")  # Попытка обработать строку (ненужную строчку или строчки прикрываем #)
        handle_data(-5)     # Попытка обработать отрицательное число
        handle_data(5)      # Обработка без ошибки

    except (InvalidDataException, ProcessingException) as e:
        print(f"Исключение в основной части программы: {e}")

print ('****** Конец урока ******')
#В этом коде:
#1. Создаются два собственных исключения `InvalidDataException` и `ProcessingException`.
#2. Функция `process_data` проверяет, является ли входной параметр целым числом и неотрицательным,
# и генерирует соответствующие исключения.
#3. Функция `handle_data` вызывает `process_data`, обрабатывает возникающие исключения и передает
# их дальше с помощью `raise`.
#4. В основной части программы вызывается `handle_data` с различными аргументами,
# и происходит последующая обработка исключений.
# Код демонстрирует использование блоков `try`, `except`, `else` и `finally` для обработки исключений
# и передачи их по стеку вызовов.
