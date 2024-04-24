class House:
    def __init__(self):
        self.numberOfFloors = 10


my_house = House()
i = 0
while i < my_house.numberOfFloors:
    i += 1
    print('Текущий этаж равен: ', i)
