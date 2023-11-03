"""The area of a rectangle is the area total surrounding of the rectangle.
    It is calculated as the length multiplied by the with i.e area=L*B."""

# The variable for the length is defined below and I have applied the int() to convert the data from a str to int.
length = int(input("The length of a rectangle is longest path of the shape. In this calculation,\n the length is:"))

# The variable for the width is defined below and I have applied the int() to convert the data from a str to int.
width = int(input("The width of a rectangle is shortest path of the shape. In this calculation,\n the width is:"))

# The variable for the length is defined below. The variables were earlier converted. The int() will not be needed.
area = (length*width)
# End of problem
print("The area of the rectangle is", area, "square meters", end="")
