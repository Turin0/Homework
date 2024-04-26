class Building:
    def __init__(self):
        self.numberOfFloors = 0
        self.buildingType = ''

    def __eq__(self, other):
        return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType


my_building = Building()
my_building_2 = Building()
if Building.__eq__(my_building, my_building_2):
    print('Здания идентичны')
