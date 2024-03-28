num_1 = int(input('Введите число для получения факториала: '))


def factorial_2(n):
    if n == 0:
        return 1
    else:
        return n * factorial_2(n - 1)


print(factorial_2(num_1))
factorial_1 = 1
while num_1 > 1:
    factorial_1 *= num_1
    num_1 -= 1
print(factorial_1)
num_2 = int(input('Введите длительность ряда Фиббоначчи(2 <): '))
fib_series = [0, 1]

for i in range(2, num_2):
    fib_series.append(fib_series[-1] + fib_series[-2])
print(fib_series)
num_3 = int(input('Введите номер числа последовательности Фиббоначчи: '))


def recursiveFib(n):
    if n == 1 or n == 2:
        return 1
    return recursiveFib(n - 1) + recursiveFib(n - 2)


print(recursiveFib(num_3))
