class Car:
    price = 1000000

    def horse_powers(self):
        horse_power = 200
        return horse_power


class Nissan(Car):
    price = 500000

    def horse_powers(self):
        horse_power = 150
        return horse_power


class Kia(Car):
    price = 300000

    def horse_powers(self):
        horse_power = 100
        return horse_power


car_1 = Nissan()
print('Nissan')
print('Цена машины:', car_1.price)
print('Лошадинные силы:', car_1.horse_powers())
car_2 = Kia()
print('Kia')
print('Цена машины:', car_2.price)
print('Лошадинные силы:', car_2.horse_powers())
