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


X_Right_wing, Y_Right_wing, X_Left_wing, Y_Left_wing = plane.wingTopViewPoints()

X_ht, Y_ht = plane.empennageTopViewPoints()

X_fuse, Y_fuse = fuselage.topViewPoints()

plt = matplotlib.pyplot
plt.figure(1)
plt.plot(X_Right_wing, Y_Right_wing, X_Left_wing, Y_Left_wing, X_ht, Y_ht, X_fuse, Y_fuse, [fuselage.fuselageWidth/2, -fuselage.fuselageWidth/2], [-cg, -cg])
plt.axis('equal')

# plt.figure(2)
# alpha = [x for x in range(-5, 10)]
# C_l = wing.calcC_lRange(-5,10)
# plt.plot(alpha, C_l)
# plt.grid()
#
# plt.figure(3)
# C_d = wing.calcC_dRange(-5, 10)
# plt.plot(alpha, C_d)
# plt.grid()

plt.show()





