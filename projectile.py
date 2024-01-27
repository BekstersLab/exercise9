from math import pi, tan, cos


# Practice with complex maths


# gravity = pow(9.81, 2)
# initial_vorticity = 44
# theta = 80 * (pi/80)
# distance = 0.5
# height = 1

y = 1 + 0.5*tan(80*(pi/180)) - pow(9.81, 2) / 2*pow(44*cos(80*(pi/180)), 2)
print(y)
