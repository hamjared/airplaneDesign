from Fuselage import Fuselage
from Wing import Wing
from Empennage import Empennage
from Component import Component
import operatingConditions as opCond

class Plane:

    def __init__(self, fuselage, wing, empennage, components):
        self.fuselage = fuselage
        self.wing = wing
        self.empennage = empennage
        self.components = components
        self.cg = -1
        self.calcCG()

    def calcCG(self):
        xW = 0
        W = 0
        for component in self.components:
            xW += component.weight * component.x_location
            W += component.weight
        self.cg = xW/W
        return xW/W

    def wingTopViewPoints(self):
        x1 = -1 * self.fuselage.fuselageWidth / 2
        y1 = self.cg - 0.3 * self.wing.MAC

        x2 = x1 + -1 * self.wing.wingSpan / 2
        y2 = y1 + (self.wing.rootChord - self.wing.tipChord)

        x3 = x2
        y3 = y2 + self.wing.tipChord

        x4 = x1
        y4 = y3

        x5 = -x1
        y5 = y1

        x6 = x5 + self.wing.wingSpan / 2
        y6 = y2

        x7 = x6
        y7 = y3

        x8 = x5
        y8 = y7

        X_Right_wing = [x1, x2, x3, x4]
        Y_Right_wing = [-y1, -y2, -y3, -y4]

        X_Left_wing = [x5, x6, x7, x8]
        Y_Left_wing = [-y5, -y6, -y7, -y8]

        return X_Right_wing, Y_Right_wing, X_Left_wing, Y_Left_wing

    def empennageTopViewPoints(self):
        x0 = 0
        y0 = opCond.l_ht + self.cg - 0.25 * self.empennage.ht.MAC

        x1 = -1 * self.fuselage.thrustTubeOutletDiameter / 2
        y1 = opCond.l_ht + self.cg - 0.25 * self.empennage.ht.MAC

        x2 = x1 + -1 * self.empennage.ht.wingSpan / 2
        y2 = y1 + (self.empennage.ht.rootChord - self.empennage.ht.tipChord)

        x3 = x2
        y3 = y2 + self.empennage.ht.tipChord

        x4 = -x2
        y4 = y3

        x5 = -x2
        y5 = y2

        x6 = -x1
        y6 = y1

        x7 = 0
        y7 = y6

        X_ht = [x0, x1, x2, x3, x4, x5, x6, x7]
        Y_ht = [-y0, -y1, -y2, -y3, -y4, -y5, -y6, -y7]

        return X_ht, Y_ht



