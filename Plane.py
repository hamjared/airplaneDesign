from Fuselage import Fuselage
from Wing import Wing
from Empennage import Empennage
from Component import Component

class Plane:

    def __init__(self, fuselage, wing, empennage, components):
        self.fuselage = fuselage
        self.wing = wing
        self.empennage = empennage
        self.components = components

    def calcCG(self):
        xW = 0
        W = 0
        for component in self.components:
            xW += component.weight * component.x_location
            W += component.weight
        return xW/W



