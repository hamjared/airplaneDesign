from Wing import Wing
import math
import operatingConditions as opCond

class Empennage:

    def __init__(self):
        self.ht = Wing()
        self.ht.aspectRatio = opCond.horizontalStabAspectRatio
        self.ht.taperRatio = opCond.horizontalStabTaperRatio
        self.vt = Wing()
        self.vt.aspectRatio = opCond.verticalStabAspectRatio
        self.vt.taperRatio = opCond.verticalStabTaperRatio


    def calcHTGeometry(self, wingArea, wingMAC, l_ht=opCond.l_ht, V_ht = opCond.V_ht):
        self.ht.wingArea = V_ht *wingArea*wingMAC/l_ht
        self.ht.wingSpan = math.sqrt(self.ht.wingArea * self.ht.aspectRatio)
        self.ht.rootChord = 2*self.ht.wingArea/((1+self.ht.taperRatio)*self.ht.wingSpan)
        self.ht.tipChord = self.ht.taperRatio * self.ht.rootChord
        self.ht.MAC = self.ht.wingSpan/6*(1+2*self.ht.aspectRatio)/(1+self.ht.aspectRatio)
        self.ht.MACLocation = 2/3 * self.ht.rootChord*(1+self.ht.aspectRatio+self.ht.aspectRatio**2)/(1+self.ht.aspectRatio)

    def calcVTGeometry(self, wingarea, wingSpan, l_vt = opCond.l_ht, V_vt = opCond.V_vt):
        self.vt.wingArea = V_vt * wingSpan * wingarea / l_vt
        self.vt.wingSpan = math.sqrt(self.vt.wingArea*self.vt.aspectRatio)
        self.vt.rootChord = 2*self.vt.wingArea/((1+self.vt.taperRatio)*self.vt.wingSpan)
        self.vt.tipChord = self.vt.taperRatio * self.vt.rootChord
        self.vt.MAC = 2/3 * self.vt.rootChord * ( 1+self.vt.taperRatio + self.vt.taperRatio**2)/(1+self.vt.taperRatio)
        self.vt.MACLocation = 2 * self.vt.wingSpan / 6 * (1 + 2*self.vt.taperRatio)/(1 + self.vt.taperRatio)