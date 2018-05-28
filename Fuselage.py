import operatingConditions as opCond

class Fuselage:
    def __init__(self):
        self.noseTaperLength = opCond.noseTaperLength
        self.fuselageLength = opCond.fuselength
        self.fuselageHeight = opCond.fuselageHeight
        self.thrustTubeLength = opCond.thrustTubeLength
        self.thrustTubeOutletDiameter = opCond.thrustTubeOutletDiameter
        self.fuselageWidth = opCond.fuselageWidth

    def sideViewPoints(self):
        x1 = 0
        y1 = 50

        x2 = x1 + self.noseTaperLength
        y2 =  self.fuselageHeight

        x3 = x2+ self.fuselageLength - self.noseTaperLength - self.thrustTubeLength
        y3 = y2

        x4 = self.fuselageLength
        y4 = self.thrustTubeOutletDiameter

        x5 = x4
        y5 = 0

        x6 = x1
        y6 = 0

        return [x1, x2, x3, x4, x5, x6], [y1, y2, y3, y4, y5, y6]
