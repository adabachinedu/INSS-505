numbers = int(input("Enter numbers:"))
for numbers in range(1, numbers):
    if numbers % 5 == 0 and numbers % 3 == 0:
        print(numbers, "Tic Tac")
    if numbers % 3 == 0:
        print(numbers, "Tic")
    if numbers % 5 == 0:
        print(numbers, "Tac")

#  step6
"""In applying the while loop, we count from 1 and 15.
    lower boundary is set at 1 and upper boundary at 16"""
i = 1
while i < 16:
  print(i)
  i = i + 1
else:
    print("Finish")

# Step7
a = int(input("Enter numbers:"))
a = 1
while a < 16:
    a = a + 1
    if a % 5 == 0 and a % 3 == 0:
        print(a, "Tic Tac")
    elif (a % 3 == 0):
        print(a, "Tic")
    elif a % 5 == 0:
        print(a, "Tac")

# Step 8
# Using the random function
import random
# Apply the function to print numbers
print(random.randint(1,189))

# Step9
# Creating value to store input
user_value = 0
limit = 0
# Using the while loop
while user_value >= 0 and limit < 5:
    user_value = int(input("Enter value: \n"))
    if user_value <= 0:
        print("Error! Enter value greater than zero")
        limit += 1
#In the elif, I am constraining user to entr value between 1-10 so they are guided.
    elif user_value >= 0 and user_value <= 10:
        print("Welcome")
        break
# Then the if and elif conditions are not met uopn trail, print the else result
    else:
        print("Invalid")
        limit += 1
# After 5 tries, the user is constrained
    if limit == 5:
        print("Tries exceeded. Account deactivated!")

# Step 10
"""Once the value is above zero use random int generator to generate int value;
if the random value and your value entered matches print out perfect match,
if not print both numbers don’t match.
You are required to use if condition statement."""

import random
user_value = int(input("Enter value: \n"))
main = random.randint(1, user_value)
limit = 0
while True:
    limit += 1
    mynumber = int(input("first guess: \n"))
    if mynumber == main:
        print ("perfect")
        break
    elif mynumber != main:
        print("both numbers do not match")
        limit += 1
    else:
        print("error")
        limit += 1
    if limit == 5:
        print("exit!")



