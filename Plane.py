from Fuselage import Fuselage
from Wing import Wing
from Empennage import Empennage
from Component import Component

class Plane:

    def __init__(self, fuselage, wing, empennage, components):
        self.fuselage = Fuselage(fuselage)
        self.wing = Wing(wing)
        self.empennage = Empennage(empennage)


