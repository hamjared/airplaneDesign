import math
import operatingConditions as opCond
import matplotlib.pyplot

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

        self.a_0 = opCond.a_0
        self.e = opCond.e
        self.zeroLift_alpha = opCond.zeroLift_alpha
        self.c_d_zerolift = opCond.c_d_zerolift

        self.a = self.a_0/(1+self.a_0/(math.pi*self.e*self.aspectRatio))

        self.weight = 0
        self.cg = 0.4 * self.MAC

    def calcWingGeometry(self, velocity = opCond.velocity, cruiseC_l = opCond.cruiseC_l, airDensity = opCond.airDensity,weight = opCond.weight):
        self.wingArea = 2*weight/(airDensity*velocity**2*cruiseC_l) * 1000000 # in mm^2
        self.wingSpan = math.sqrt(self.wingArea*self.aspectRatio)
        self.rootChord = 2*self.wingArea/((1+self.taperRatio)*self.wingSpan)
        self.tipChord = self.taperRatio * self.rootChord
        self.MAC = self.wingSpan/6*(1+2*self.aspectRatio)/(1+self.aspectRatio)
        self.MACLocation = 2/3 * self.rootChord*(1+self.aspectRatio+self.aspectRatio**2)/(1+self.aspectRatio)

    def calcC_lRange(self,alpha_1 = -5, alpha_2 = 10):

        return [self.calcC_l(x) for x in range(alpha_1,alpha_2)]


    def calcC_l(self, alpha):
        return self.a * (math.radians(alpha) - self.zeroLift_alpha)

    def calcC_dRange(self,alpha_1 = -5, alpha_2 = 10):
        return [self.calcC_d(x) for x in range(alpha_1,alpha_2)]


    def calcC_d(self,alpha):
        return self.c_d_zerolift + 1/(math.pi * self.e * self.aspectRatio)*(self.calcC_l(alpha))**2









