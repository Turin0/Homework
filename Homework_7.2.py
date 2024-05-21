file_name = 'Poem.txt'
with open(file_name, mode='r', encoding='utf8') as file:  # Оператор with позволяет контролировать вход и выход из файла
    for line in file:
        print(line, end="")
