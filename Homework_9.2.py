print('Задача 1: Фабрика функций')


def math_operation(operation):
    if operation == 'multiplier':
        def multiplier(x, y):
            return x * y

        return multiplier
    elif operation == 'division':
        def division(x, y):
            return x / y

        return division


my_func_multiplier = math_operation('multiplier')
print(my_func_multiplier(10, 3))
my_func_division = math_operation('division')
print(my_func_division(10, 2))
print('Задача 2: Лямбда функция')
square = (lambda x: x ** 2)
print(square(3))


def square_f(x):
    return x ** 2


print(square_f(3))
print('Задача 3: Вызываемые объекты')


class Rect:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self):
        print(f'Стороны: {self.a}, {self.b}')
        area = self.a * self.b
        return f'Площадь: {area}'


square_ = Rect(5, 5)
print(square_.__call__())
