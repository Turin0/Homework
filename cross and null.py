def winner_check():
    if area[0][0] == 'X' and area[0][1] == 'X' and area[0][2] == 'X':
        return 'X'
    if area[1][0] == 'X' and area[1][1] == 'X' and area[1][2] == 'X':
        return 'X'
    if area[2][0] == 'X' and area[2][1] == 'X' and area[2][2] == 'X':
        return 'X'
    if area[0][0] == 'X' and area[1][1] == 'X' and area[2][2] == 'X':
        return 'X'
    if area[0][2] == 'X' and area[1][1] == 'X' and area[2][0] == 'X':
        return 'X'
    if area[0][0] == 'X' and area[1][0] == 'X' and area[2][0] == 'X':
        return 'X'
    if area[0][1] == 'X' and area[1][1] == 'X' and area[2][1] == 'X':
        return 'X'
    if area[0][2] == 'X' and area[1][2] == 'X' and area[2][2] == 'X':
        return 'X'
    if area[0][0] == '0' and area[0][1] == '0' and area[0][2] == '0':
        return '0'
    if area[1][0] == '0' and area[1][1] == '0' and area[1][2] == '0':
        return '0'
    if area[2][0] == '0' and area[2][1] == '0' and area[2][2] == '0':
        return '0'
    if area[0][0] == '0' and area[1][1] == '0' and area[2][2] == '0':
        return '0'
    if area[0][2] == '0' and area[1][1] == '0' and area[2][0] == '0':
        return '0'
    if area[0][0] == '0' and area[1][0] == '0' and area[2][0] == '0':
        return '0'
    if area[0][1] == '0' and area[1][1] == '0' and area[2][1] == '0':
        return '0'
    if area[0][2] == '0' and area[1][2] == '0' and area[2][2] == '0':
        return '0'
    return '*'


def draw_area():
    for j in area:
        print(*j)
    print()
area = [['*', '*', '*'],['*', '*', '*'],['*', '*', '*']]
print('Добро пожаловать в крестики нолики!')
print('-----------------------------------')
draw_area()
for turn in range(1,10):
    print(f'Ход {turn}')
    if turn % 2 ==0:
        print('Ходят нолики')
        turn_char = '0'
    else:
        print('Ходят крестики')
        turn_char = 'X'
    X = int(input('Введите номер строки (1,2,3) ')) - 1
    Y = int(input('Введите номер столбца (1,2,3) ')) - 1
    if area[X][Y] == '*':
        area[X][Y] = turn_char
    else:print('Эта ячейка занята, вы пропускаете ход')
    draw_area()
    winner_check
    if winner_check() == 'X':
        print('Победили крестики')
        break
    if winner_check() == '0':
        print('Победили нолики')
        break
    if winner_check() == '*' and turn == 9:
        print('Ничья')






