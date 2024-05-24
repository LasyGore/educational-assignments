class EvenNumbers:
    def __init__(self, start=0, end=1):
        self.start = start if start % 2 == 0 else start + 1  # если start нечетное, увеличиваем на 1
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= self.end:
            result = self.start
            self.start += 2  # увеличиваем на 2 для следующего четного числа
            return result
        else:
            raise StopIteration

# Пример использования
en = EvenNumbers(10, 25)
for i in en:
    print(i)
