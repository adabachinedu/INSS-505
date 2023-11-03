""" In this problem, I will use my understanding of loop to list only a few items in a list.
    This is called the break statement.
    Problem statement:
    In a system made up of integers, exit the loop when it detects a float.
     = (10, 6, 4, 3, 2, 1.5, 1, 0, 0.5)                                   """
# In solving the problem above, we will apply the loop() ie "for" statement
system = (10, 6, 4, 3, 2, 1.5, 1, 0, 0.5)
for outlier in system:
    if outlier == 1.5:
        break
    print(outlier, end="")

""" The loop() is an iteration but in this problem, we applied a if statement.
    The if statement is a conditional that triggers action when a particular point is reached.
    The break statement acted on he if function to create a halt  
    In the print, we apply the end() to print the output horizontally                """
