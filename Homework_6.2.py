class Vehicle:
    vehicle_type = 'none'


class Car:
    price = 1000000

    def horse_powers(self):
        horse_power = 200
        return horse_power


class Nissan(Car, Vehicle):
    price = 500000
    vehicle_type = 'Автомобиль'

    def horse_powers(self):
        horse_power = 150
        return horse_power

car_1 = Nissan()
print('Nissan')
print('Тип транспортного средства:', car_1.vehicle_type, 'Цена:', car_1.price)
