class Building:
    total = 0

    def __init__(self):
        Building.total += 1


building_quantity = 40
while Building.total < building_quantity:
    building = Building()
    print(Building.total)