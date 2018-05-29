from Fuselage import Fuselage
from Wing import Wing
from Empennage import Empennage
from Component import Component

class Plane:

    def __init__(self, fuselage, wing, empennage, components):
        self.fuselage = fuselage
        self.wing = wing
        self.empennage = empennage
        self.compoents = components

    def calcCG(self):
        return -1


