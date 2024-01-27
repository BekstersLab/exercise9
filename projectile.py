from math import pi, tan, cos


# Practice with complex maths

# gravity = pow(9.81, 2)
# initial_vorticity = 44
# theta = 80 * (pi/80)
# distance = 0.5
# height = 1
# x = pi

y = 1 + 0.5*tan(80*(pi/180)) - pow(9.81, 2) / 2*pow(44*cos(80*(pi/180)), 2)
print(y)


# TO DO: Method and Modules
# Practice with complex maths

# import the math module to be able to use pi, tan (tangent) and cos (cosine) in calculation
import math
# print math.pi to check pi is working - shows 3.141592653589793
print(f"pi = {math.pi}")

# declare the variables as per the instructions given above:
# declaring the height of the barrel (y0) as 1 meter
y0 = 1

# declaring the horizontal distance travelled (x) as 0.5 meters
x = 0.5

# theta = deg * (pi/180) from instructions =
# theta = 80 * (3.141592653589793 / 180)
theta = 80 * (math.pi / 180)
# printing the value of theta determined by the above calculation
print(f"theta = {theta}")

# declaring the acceleration due to gravity (g) as 9.81 m/s
g = 9.81

# declaring the initial velocity (v0) as 44 m/s
v0 = 44

# the equation written in python (I hope this is correct!)
y = y0 + x * math.tan(theta) - ((g * x**2) / (2 * (v0 * math.cos(theta)))**2)
# math.tan() function returns the tangent of value passed as argument
# math.cos() function returns the cosine of value passed as argument

# print the answer
print(f"y = {y}")

# round y to 2 decimal places otherwise it prints to 16 decimal places
y_rounded2 = round(y, 2)

# print y rounded to 2dp, which is the outcome of the calculation
print(f"the height of the projectile is {y_rounded2} meters")

# //////// ORIGINAL QUESTION ////////

'''
The height of a projectile (y) from a gun (ignoring air resistance) is given as:

where:
g : acceleration due to gravity: 9.81 m/s squared
v0: the initial velocity m/s
0: (theta) elevation angle in radians
x: the horizontal distance travelled
y0: height of the barrel (m)

Write a python program to answer the following question:
At a barrel height of 1m, after a horizontal distance of 0.5m, an elevation of 80 degrees,
and an initial velocity of 44 m/s, what is the height of the projectile?

To convert degrees (deg) to radians use:

theta = deg * (pi/180)

You will need to import some math methods:

from math import pi, tan, cos

BEK NOTE: not sure how to include the image of equation. I think I have correctly written out in code below

'''


