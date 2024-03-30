def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(5, 2) # предупреждение в связи с заменой строкового параметра на целочисленный
print_params(b = 25) # предупреждение в связи с заменой строкового параметра на целочисленный
print_params(c = [1, 2, 3]) # предупреждение в связи с заменой булевого параметра на список
values_list = [5, 'str', False]
values_dict = {'a': 10, 'b': 'str', 'c': True}

print_params(*values_list)
print_params(**values_dict)
values_list_2 = [33, 'A']
print_params(*values_list_2, 42) # параметр 'c' ошибочно принят за параметр 'a'