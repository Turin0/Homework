def square(x):
    return x ** 2


def odd(x):
    return x % 2


numbers = [1, 2, 5, 7, 12, 11, 35, 4, 89, 10]
result = map(square, filter(odd, numbers))
print(list(result))