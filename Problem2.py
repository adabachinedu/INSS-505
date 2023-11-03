#To find the area of a circle, we would import the math function with the statement below:
import math

# The radius of a circle in this problem will be denoted as "r"
radius = "r"
r = float(input("the radius of the circumference of a circle. the radius is:\n "))
# In line 5, the float() was added to convert the string to an integer inorder to apply mathematical functions.

# pi will be inputted by python given that math.pi is a builtin function
pi = input(math.pi)

# Apply the formular to calculate the area of a circle
area = (math.pi * r**2)
print(area)
# End of problem

