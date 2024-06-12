import time
from threading import Thread


class Knight(Thread):
    def __init__(self, name, skills, *args, **kwargs):
        super(Knight, self).__init__(*args, **kwargs)
        self.name = name
        self.skills = skills

    def run(self):
        print(f'{self.name}, на нас напали!')
        enemy = 100
        day = 0
        while enemy > 0:
            enemy = enemy - self.skills
            day += 1
            time.sleep(1)
            if enemy <= 0:
                return print(f'{self.name}, одержал победу спустя {day} дней!')
            print(f'{self.name}, сражается {day} день(дня)..., осталось {enemy} воинов.')


sir_L = Knight('Сир Ланселот', 10)
sir_P = Knight('Сир Персиваль', 12)
sir_L.start()
time.sleep(0.001)
sir_P.start()
sir_L.join()
sir_P.join()
print('Все битвы закончились!')
