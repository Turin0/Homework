team_num1 = 5
team_num2 = 6

print('В команде %s участников: %s!' % ('Мастера кода', team_num1))
print('Итого сегодня в командах участников: %s и %s!' % (team_num1, team_num2))

score_2 = 42

print('Команда {} решила задач: {}!' .format('Волшебники данных', score_2))

team1_time = 17699.3
team2_time = 18015.2

print('{} решили задачи за {} с!' .format('Волшебники данных', team2_time))

score_1 = 40

print(f'Команды решили {score_1} и {score_2} задач.')

if score_1 > score_2 or score_1 == score_2 and team1_time < team2_time:
    challenge_result = 'победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time > team2_time:
    challenge_result = 'победа команды Волшебники данных!'
else:
    challenge_result = 'ничья!'

print(f'Результат битвы: {challenge_result}')

task_total = score_1 + score_2
time_avg = round((team1_time + team2_time) / task_total, 2)

print(f'Сегодня было решено {task_total} задач, в среднем по {time_avg} секунды на задачу!')
