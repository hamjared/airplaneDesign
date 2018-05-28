import math

# physical Properties
weight = 3 * 9.81 # N
cg = 200

# wing geometry
taperRatio = 0.5
aspectRatio = 8


#  geometry
horizontalStabTaperRatio = 0.8
horizontalStabAspectRatio = 3
l_ht = 450 # mm from the CG of airplane to the aerodynamic center of the horizontal stabilizer
V_ht = 0.7
# cruise conditions
airDensity = 0.9 # kg/m^3
velocity = 30 # m/s
cruiseC_l = 0.3

#EDF properties
staticThrustAirDesnity = 1.2
inletDiam = 90 # mm
maxMotorDiam = 40 #mm
fanSweptArea = math.pi/4 *(inletDiam**2 - maxMotorDiam**2)
staticThrust = 40 #N
efflux = math.sqrt( staticThrust / (staticThrustAirDesnity*fanSweptArea))

