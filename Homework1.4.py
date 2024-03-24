immutable_var = 1 ,2 , 'string', False
print(immutable_var)
immutable_var[0] = 200 # Кортеж не поддерживает изменение своих данных
mutable_list = [0, 1 , 'string', False]
mutable_list[3] = True
print(mutable_list)
