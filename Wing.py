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

    def calcWingGeometry(self, velocity = opCond.velocity, cruiseC_l = opCond.cruiseC_l, airDensity = opCond.airDensity,weight = opCond.weight):
        self.wingArea = 2*weight/(airDensity*velocity**2*cruiseC_l) * 1000000 # in mm^2
        self.wingSpan = math.sqrt(self.wingArea*self.aspectRatio)
        self.rootChord = 2*self.wingArea/((1+self.taperRatio)*self.wingSpan)
        self.tipChord = self.taperRatio * self.rootChord
        self.MAC = self.wingSpan/6*(1+2*self.aspectRatio)/(1+self.aspectRatio)
        self.MACLocation = 2/3 * self.rootChord*(1+self.aspectRatio+self.aspectRatio**2)/(1+self.aspectRatio)

    def plotC_l(self,alpha_1 = -5, alpha_2 = 10):
        C_l_plot = matplotlib.pyplot
        C_l = [self.calcC_l(x) for x in range(alpha_1,alpha_2)]
        Alpha = [x for x in range(alpha_1, alpha_2)]
        C_l_plot.plot(Alpha,C_l)
        C_l_plot.show()

    def calcC_l(self, alpha):
        alpha = self.degToRad(alpha)
        return  self.a * (alpha - self.zeroLift_alpha)

    def plotC_d(self,alpha_1 = -5, alpha_2 = 10):
        C_d_plot = matplotlib.pyplot
        C_d = [self.calcC_l(x) for x in range(alpha_1,alpha_2)]
        Alpha = [x for x in range(alpha_1, alpha_2)]
        C_d_plot.plot(Alpha,C_d)
        C_d_plot.show()
    def calcC_d(self,alpha):
        alpha = self.degToRad(alpha)
        return self.c_d_zerolift + 1/(math.pi * self.e * self.aspectRatio)*(self.a * (self.calcC_l(alpha)))**2

    def degToRad(self,alpha):
        return alpha * 0.0174533







