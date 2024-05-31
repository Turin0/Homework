class ExZero(Exception):
    def __init__(self, massage, extra_info):
        self.massage = massage
        self.extra_info = extra_info


class TypeEr(Exception):
    def __init__(self, massage, extra_info):
        self.massage = massage
        self.extra_info = extra_info


def f_0(a, b):
    if a == 0 or b == 0:
        raise ExZero('Деление на ноль невозможно', {'a': a, 'b': b})
    if a != int() and b != int():
        raise TypeEr('Неправильный тип данных', {'a': a, 'b': b})
    return a / b


try:
    print(f_0(10, 0))
except ExZero as e:
    print(f'Что-то пошло не так: {e.massage}, вот дополнительная информация {e.extra_info}')
try:
    f_0(10, 's')
except TypeEr as e_1:
    print(f'Что-то пошло не так: {e_1.massage}, вот дополнительная информация {e_1.extra_info}')
