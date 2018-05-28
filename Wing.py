import math
import operatingConditions as opCond

class Wing():
    def __init__(self):
        self.taperRatio = opCond.taperRatio
        self.aspectRatio = opCond.aspectRatio
        self.wingArea = 0
        self.wingSpan = 0
        self.rootChord = 0
        self.tipChord = 0
        self.MAC = 0
        self.MACLocation = 0
        self.calcWingGeometry()

    def calcWingGeometry(self, velocity = opCond.velocity, cruiseC_l = opCond.cruiseC_l, airDensity = opCond.airDensity,weight = opCond.weight):
        self.wingArea = 2*weight/(airDensity*velocity**2*cruiseC_l) * 1000000 # in mm^2
        self.wingSpan = math.sqrt(self.wingArea*self.aspectRatio)
        self.rootChord = 2*self.wingArea/((1+self.taperRatio)*self.wingSpan)
        self.tipChord = self.taperRatio * self.rootChord
        self.MAC = self.wingSpan/6*(1+2*self.aspectRatio)/(1+self.aspectRatio)
        self.MACLocation = 2/3 * self.rootChord*(1+self.aspectRatio+self.aspectRatio**2)/(1+self.aspectRatio)\



