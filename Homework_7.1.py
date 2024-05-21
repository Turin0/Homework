file_name = 'Poem.txt'
file = open(file_name, mode='r', encoding='utf8')
print(file.read())
file.close()
