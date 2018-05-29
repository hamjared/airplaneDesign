import math

# physical Properties
weight = 3 * 9.81 # N
cg = 200

# wing geometry
taperRatio = 0.5
aspectRatio = 5

#wing properties
a_0 = 0.12 *180/math.pi # c_l/rad
e = 0.95 #efficiency factor
zeroLift_alpha = math.radians(-2) # rad
c_d_zerolift = 0.015

#  empennage geometry
horizontalStabTaperRatio = 0.8
horizontalStabAspectRatio = 3
l_ht = 300 # mm from the CG of airplane to the aerodynamic center of the horizontal stabilizer
V_ht = 0.7
verticalStabTaperRatio = 0.8
verticalStabAspectRatio = 5
V_vt = 0.01

#fuselage geometry
noseTaperLength = 150 #mm
fuselageHeight = 90 #mm
fuselageWidth = 50 #mm
fuselength = 620 # mm
thrustTubeLength = 270 #mm
thrustTubeOutletDiameter = 72 # mm


# cruise conditions
airDensity = 0.9 # kg/m^3
velocity = 50 # m/s
cruiseC_l = 0.5

#EDF properties
staticThrustAirDesnity = 1.2
inletDiam = 90 # mm
maxMotorDiam = 40 #mm
fanSweptArea = math.pi/4 *(inletDiam**2 - maxMotorDiam**2)
staticThrust = 40 #N
efflux = math.sqrt( staticThrust / (staticThrustAirDesnity*fanSweptArea))


