import math
from random import randint

year = int(input('Введите год: '))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('Високосный год')
else:
    print('Не високосный год')
#
delivery = float(input('Введите вес для доставки: '))
price = 50
if delivery <= 2:
    print('Доставка составит ', price, ' рублей')
if 2 < delivery <= 10:
    price = 50 + 20 * (delivery-2)
    print('Доставка составит ', round(price, 2), ' рублей')
else:
    print('Доставка составит 200 рублей')
#
max_num = int(input('Введите число для получения списка простых чисел: '))
primes = [2]
test_num = 3
while test_num < max_num:
    i = 0
    while primes[i] <= math.sqrt(test_num):
        if (test_num % primes[i]) == 0:
            test_num += 1
            break
        else:
            i += 1
    else:
        primes.append(test_num)
        test_num += 1
print(primes)
#
a = 1
random_num = randint(1, 100)
while random_num != a:
    a = int(input('Угадайте число:'))
    if a > random_num:
        print('Введенное число больше искомого')
    if a < random_num:
        print('Введенное число меньше искомого')
    if a == random_num:
        print('Вы угадали число')
#
x = int(input('Введите число для получения таблицы умножения от 1 до 10: '))
for i in range(11):
    if i != 0:
        print(x, '*', i, '=', x * i)
    else:
        continue
#
N = int(input('Введите число:'))
sum_ = 0
for i in range(N+1):
    sum_ += i
print(sum_)
