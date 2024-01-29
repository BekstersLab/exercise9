# Practice with complex maths
# from statement finds and compiles math module, allowing it to import the pi, tan and cos functions
from math import pi, tan, cos
# import math - do not use as will need to input math.pi, math.tan, math.cos (bek original import method)

# Write a python program to answer the following question:
# At a barrel height of 1m, after a horizontal distance of 0.5m,
# an elevation of 80 degrees and an initial velocity of 44 m/s, what is the height of the projectile?

# print pi to check pi is working - shows 3.141592653589793
# print(f"pi = {math.pi}")
# f-string used to interpolate and format strings
# interpolation - process substituting values of variables into placeholders in a string
# f-string = formatting sting literals = provides a way to embed expressions inside string literals
print(f"pi = {pi}")

# declare the variables as per the instructions given above:
# declaring the height of the barrel (y0) as 1 meter
y0 = 1

# declaring the horizontal distance travelled (x) as 0.5 meters
x = 0.5

# theta = deg * (pi/180) from instructions =
# theta = 80 * (3.141592653589793 / 180)
# theta = 80 * (math.pi / 180)
theta = 80 * (pi / 180)
# printing the value of theta determined by the above calculation
print(f"theta = {theta}")

# declaring the acceleration due to gravity (g) as 9.81 m/s
g = 9.81

# declaring the initial velocity (v0) as 44 m/s
v0 = 44

# version 1 - WRONG Gives answer of y = 3.8251381553649444 (CLOSE)
# the equation written in python (I hope this is correct!) Original version using import math
# y = y0 + x * math.tan(theta) - ((g * x**2) / (2 * (v0 * math.cos(theta)))**2)

# updated version using 'from math import pi, tan, cos' - leticia's import method!
# y = y0 + x * tan(theta) - ((g * x**2) / (2 * (v0 * cos(theta)))**2)

# tan() function returns the tangent of value passed as argument
# cos() function returns the cosine of value passed as argument

# version 2 - WRONG! Gives answer of y = 3.732608888714104
# y = y0 + x * tan(theta) - ((g * x)**2 / (2 * (v0 * cos(theta)))**2)

# Apparently this is the correct answer and I got to it knowing the answer should be 3.81.
# I wouldn't have known to write the equation out like this from the given diagram! I am not good at maths!!!
# version 3
y = y0 + x * tan(theta) - ((g * x**2) / (2 * v0**2 * cos(theta)**2))

# print the answer
print(f"y = {y}")

# round y to 2 decimal places otherwise it prints to 16 decimal places
y_rounded2 = round(y, 2)

# print y rounded to 2dp, which is the outcome of the calculation
print(f"{y_rounded2} meters is the height of a projectile at a horizontal distance of 0.5 meters, given a starting height of 1 meter, an elevation of 80 degrees and an initial velocity of 44 meters per second")

# ---------- Leticia code -------------

# hard coded the values - to make of my code and thinking steps 
y = 1 + 0.5*tan(80*(pi/180)) - pow(9.81, 2) / 2*pow(44*cos(80*(pi/180)), 2)

print(y)

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

'''


