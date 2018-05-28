from Wing import Wing
import math
import operatingConditions as opCond

class Empennage:

    def __init__(self):
        self.ht = Wing()
        self.ht.aspectRatio = opCond.horizontalStabAspectRatio
        self.ht.taperRatio = opCond.horizontalStabTaperRatio
        self.vt = Wing()


    def calcHTGeometry(self, wingArea, wingMAC, l_ht=opCond.l_ht, V_ht = opCond.V_ht):
        self.ht.wingArea = V_ht *wingArea*wingMAC/l_ht
        self.ht.wingSpan = math.sqrt(self.ht.wingArea * self.ht.aspectRatio)
        self.ht.rootChord = 2*self.ht.wingArea/((1+self.ht.taperRatio)*self.ht.wingSpan)
        self.ht.tipChord = self.ht.taperRatio * self.ht.rootChord
        self.ht.MAC = self.ht.wingSpan/6*(1+2*self.ht.aspectRatio)/(1+self.ht.aspectRatio)
        self.ht.MACLocation = 2/3 * self.ht.rootChord*(1+self.ht.aspectRatio+self.ht.aspectRatio**2)/(1+self.ht.aspectRatio)
