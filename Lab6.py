limit = 0
while True:
    e_value = int(input("Enter value: \n"))

    if e_value <= 0:
        print("Error! Enter a value greater than zero")
    else:
        print("Welcome")
        break

if e_value % 2 == 0:
    print("Number is Even")
elif e_value % 2 != 0:
    print("Number is Odd")

for i in range(2, int(e_value ** 0.5) + 1):
    if (e_value % i) == 1:
        print("Number is prime")
        limit += 1
        break
    else:
        print("Number is Non-Prime")