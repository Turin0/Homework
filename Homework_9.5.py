import math


def is_prime(func):
    def wrapper(*args, **kwargs):
        result_ = func(*args, **kwargs)
        d = 2
        while result_ % d != 0:
            d += 1
        if d == result_:
            return 'Число простое'
        else:
            return 'Число составное'
    return wrapper


@is_prime
def sum_three(a, b, c):
    sum_ = a + b + c
    print(sum_)
    return sum_


result = sum_three(2, 3, 6)
print(result)
