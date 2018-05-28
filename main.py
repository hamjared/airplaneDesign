from Wing import Wing
from Empennage import Empennage
import operatingConditions as opCond

import matplotlib.pyplot as plt



wing = Wing()
print("wing area: ", wing.wingArea)
print("wingspan: ", wing.wingSpan)
print("root chord: ", wing.rootChord)
print("tip chord: ", wing.tipChord)
print()
empennage = Empennage()
empennage.calcHTGeometry(wing.wingArea,wing.MAC)
print("ht area: ", empennage.ht.wingArea)
print("ht span: ", empennage.ht.wingSpan)
print("ht root chord: ", empennage.ht.rootChord)
print("ht tip chord: ", empennage.ht.tipChord)


x1 = 0
y1 = opCond.cg - .25*wing.MAC

x2 = -1 * wing.wingSpan/2
y2 = y1 + (wing.rootChord-wing.tipChord)

x3 = x2
y3 = y2 + wing.tipChord

x4 = 0
y4 = y3

X_wing = [x1, x2, x3, x4, -x1, -x2, -x3, -x4]
Y_wing = [-y1, -y2, -y3, -y4, -y1, -y2, -y3, -y4]

x1 = 0
y1 = opCond.l_ht + opCond.cg - 0.25 * empennage.ht.MAC

x2 = -1* empennage.ht.wingSpan/2
y2 = y1 + (empennage.ht.rootChord- empennage.ht.tipChord)

x3 = x2
y3 = y2 + empennage.ht.tipChord

x4 = 0
y4 = y3

X_ht = [x1, x2, x3, x4, -x1, -x2, -x3, -x4]
Y_ht = [-y1, -y2, -y3, -y4, -y1, -y2, -y3, -y4]

plt.plot(X_wing,Y_wing, X_ht, Y_ht)
plt.axis('equal')
plt.show()


