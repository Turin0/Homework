class Building:
    def __init__(self):
        self.numberOfFloors = 0
        self.buildingType = ''

    def __eq__(self, other):
        return self.numberOfFloors == self.buildingType


my_building = Building()
my_building.__eq__(0)
