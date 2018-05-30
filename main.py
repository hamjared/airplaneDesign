from Wing import Wing
from Empennage import Empennage
import operatingConditions as opCond
from Component import Component
from Fuselage import Fuselage
import matplotlib.pyplot
from Plane import Plane

wing = Wing()
fuselage = Fuselage()
print("wing area: ", wing.wingArea)
print("wingspan: ", wing.wingSpan)
print("MAC: ", wing.MAC)
print("root chord: ", wing.rootChord)
print("tip chord: ", wing.tipChord)
print()
empennage = Empennage()
empennage.calcHTGeometry(wing.wingArea, wing.MAC)
empennage.calcVTGeometry(wing.wingArea, wing.wingSpan)
print("ht area: ", empennage.ht.wingArea)
print("ht span: ", empennage.ht.wingSpan)
print("ht root chord: ", empennage.ht.rootChord)
print("ht tip chord: ", empennage.ht.tipChord)
print()
print("vt area: ", empennage.vt.wingArea)
print("vt span: ", empennage.vt.wingSpan)
print("vt root chord: ",  empennage.vt.rootChord)
print("vt tip chord : ", empennage.vt.tipChord)


battery = Component(1.1*9.81, 180)
edf = Component(0.5*9.81, 350)
payload = Component(1*9.81, 100)

components = [battery, edf, payload]
plane = Plane(fuselage, wing, empennage, components)
print()
print(plane.calcCG())
cg = plane.calcCG()


x1 = -1* fuselage.fuselageWidth/2
y1 = cg -  0.25*wing.MAC

x2 = x1 + -1 * wing.wingSpan/2
y2 = y1 + (wing.rootChord-wing.tipChord)

x3 = x2
y3 = y2 + wing.tipChord

x4 = x1
y4 = y3

x5 = -x1
y5 = y1

x6 = x5 + wing.wingSpan/2
y6 = y2

x7 = x6
y7 = y3

x8 = x5
y8 = y7

X_Right_wing = [x1, x2, x3, x4]
Y_Right_wing = [-y1, -y2, -y3, -y4]

X_Left_wing = [ x5, x6, x7, x8]
Y_Left_wing = [-y5, -y6, -y7, -y8]

x0 = 0
y0 = opCond.l_ht + cg - 0.25 * empennage.ht.MAC

x1 = -1* fuselage.thrustTubeOutletDiameter/2
y1 = opCond.l_ht + cg - 0.25 * empennage.ht.MAC

x2 = x1 + -1 * empennage.ht.wingSpan/2
y2 = y1 + (empennage.ht.rootChord- empennage.ht.tipChord)

x3 = x2
y3 = y2 + empennage.ht.tipChord

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

X_fuse, Y_fuse = fuselage.topViewPoints()
plt = matplotlib.pyplot
plt.figure(1)
plt.plot(X_Right_wing, Y_Right_wing, X_Left_wing, Y_Left_wing, X_ht, Y_ht, X_fuse, Y_fuse, [fuselage.fuselageWidth/2,-fuselage.fuselageWidth/2], [-cg, -cg])
plt.axis('equal')

plt.figure(2)
alpha = [x for x in range(-5, 10)]
C_l = wing.calcC_lRange(-5,10)
plt.plot(alpha, C_l)
plt.grid()

plt.figure(3)
C_d = wing.calcC_dRange(-5, 10)
plt.plot(alpha, C_d)
plt.grid()

plt.show()





