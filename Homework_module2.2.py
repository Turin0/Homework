from random import randint
print('Функция для определения самого большого числа в списке: ')


def max_number(*args):
    for i in range(len(list_)):
        print(max(list_))
        result.append(max(list_))
        list_.remove(max(list_))


list_ = [1, 5, 20, 34, 200]
result = []
max_number(list_)
print(result)
print('Функция для поиска случайного числа: ')
num = randint(1, 100)


def random_number(random_num, count):
    a = 20
    while random_num != a:
        if a > random_num:
            count += 1
            print(a, 'Введенное число больше искомого', 'Попытка №', count)
            a -= 3
        if a < random_num:
            count += 1
            print(a, 'Введенное число меньше искомого', 'Попытка №', count)
            a += 5
        if a == random_num:
            count += 1
            print(a, 'Вы нашли число', 'Попытка №', count)


count_ = 0
random_number(num, count_)
print('Функция sum_range: ')


def sum_range(x, y):
    sum = x
    while x != y:
        sum += y
        y -= 1
    print(sum)


min_num = int(input('Введите меньшее число: '))
max_num = int(input('Введите большее число: '))
sum_range(min_num, max_num)
print('Функция для определения треугольника: ')
a_1 = int(input('Введите сторону "a": '))
b_1 = int(input('Введите сторону "b": '))
c_1 = int(input('Введите сторону "c": '))


def triangle(a, b, c):
    if a < b + c and b < a + c and c < a + b:
        print('Треугольник с такими сторонами возможен')
        if a == b == c:
            print('Этот треугольник является равносторонним')
        if a == b and c != a:
            print('Этот треугольник является равнобедренным')
        if a != b != c:
            print('Этот треугольник является разносторонним')
    else:
        print('Треугольник с такими сторонами невозможен')


triangle(a_1, b_1, c_1)
print('Функция для определения счасливого билетика: ')


def lucky_ticket(a, b, c, d, e, f):
    if a + b + c == d + e + f:
        print('Билетик является счастливым')
    else:
        print('Билетик не является счастливым')


n_1 = int(input('Введите первое число билетика: '))
n_2 = int(input('Введите второе число билетика: '))
n_3 = int(input('Введите третье число билетика: '))
n_4 = int(input('Введите четвертое число билетика: '))
n_5 = int(input('Введите пятое число билетика: '))
n_6 = int(input('Введите шестое число билетика: '))
lucky_ticket(n_1, n_2, n_3, n_4, n_5, n_6)
print('Функция для определения длины строки: ')
str_ = str(input('Введите строку для определения ее длины: '))


def len_string(find_str):
    count_1 = 0
    for i in find_str:
        count_1 += 1
    print(count_1)


len_string(str_)
