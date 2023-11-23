for zero in range(0,10):
    print(zero, end="")
for one in range(1,10):
    print(one, end="")
for another in range(10, 1, -1):
    print(another)
for x in range(1,10,2):
    print(x, end="")
# step 5
radius = "r"
r = float(input("\nthe radius of the circumference of a circle. the radius is:\n "))
# step 6
import math
pi = input(math.pi)
# step 7:
areaOfcircle = (math.pi * r**2)
print(areaOfcircle)
# step 8
length = int(input("The length of a rectangle is:\n"))
# step 9
width = int(input("The width of a rectangle is:\n"))
# step 10
area = (length*width)
print(area)
#step11
"""Modification to step 7 and step 10 to apply the if and else statements. 
    The conditions will be fulfilled base on the input collected from the 
    user."""
if areaOfcircle>=0:
    print("areaOfcircle:", areaOfcircle)
elif area>=0:
    print("area:", area)
else:
    print("'Error!'\n Cannot print area, parameters less than zero")