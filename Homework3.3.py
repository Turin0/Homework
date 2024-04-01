def test(*args, **kwargs):
    print('test')
    print('Type args: ', type(args))
    print(args)
    for i, arg in enumerate(args):
        print('Позиционный параметр:', i, arg)
    print('Type kwargs: ', type(kwargs))
    print('kwargs')
    for key, value in kwargs.items():
        print('Именованный параметр:', key, '=', value)


test(1, 2, 5, 6, c=230, d=3241)


def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


print(factorial(5))
