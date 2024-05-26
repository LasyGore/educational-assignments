# декараторы
def is_prime(func):
    def wrapper(*args):
        result = func(*args)
        if result > 1:
            for i in range(2, int(result**0.5) + 1):
                if result % i == 0:
                    print("Составное")
                    break
            else:
                print("Простое")
        return result
    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c


res = sum_three(5, 7, 11)
print(res)
