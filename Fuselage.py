import operatingConditions as opCond
from Empennage import Empennage
from Wing import Wing
class Fuselage:
    def __init__(self):
        self.noseTaperLength = opCond.noseTaperLength
        self.fuselageLength = opCond.fuselength
        self.fuselageHeight = opCond.fuselageHeight
        self.thrustTubeLength = opCond.thrustTubeLength
        self.thrustTubeOutletDiameter = opCond.thrustTubeOutletDiameter
        self.fuselageWidth = opCond.fuselageWidth

    def sideViewPoints(self):
        emppenage = Empennage()

        wing = Wing()
        emppenage.calcVTGeometry(wing.wingArea, wing.wingSpan)
        vt = emppenage.vt
        lengthToLeadingEdge_vt = opCond.cg + opCond.l_ht - (vt.rootChord - vt.MAC + 0.25 * vt.MAC)
        slopeToOutlet = (self.fuselageHeight - self.thrustTubeOutletDiameter)/self.thrustTubeLength
        x1 = 0
        y1 = 50

        x2 = x1 + self.noseTaperLength
        y2 = self.fuselageHeight

        x3 = x2 + self.fuselageLength - self.noseTaperLength - self.thrustTubeLength
        y3 = y2

        x4 = lengthToLeadingEdge_vt
        y4 = y2 - x4 * slopeToOutlet

        x5 = x4 + ( vt.rootChord - vt.tipChord)
        y5 = y4 + vt.wingSpan

        x6 = x5 + vt.tipChord
        y6 = y5

        x7 = x6
        y7 = y2 - x6 * slopeToOutlet

        x8 = self.fuselageLength
        y8 = self.thrustTubeOutletDiameter

        return [x1, x2, x3, x4, x5, x6, x7, x8], [y1, y2, y3, y4, y5, y6, y7, y8]
