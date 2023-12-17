# The Start-up page of the ATM in Idle Mode will Read as Follows:

print("Welcome to Group1 Bank PLC\n"

      "Insert Card")

# Standard Requirement for an ATM system Authentication Before the Menu is Displayed:

# Number of PIN tries set after which, card is confiscated
attempts = 3

# PIN stored in system database to be called upon for authentication
pin = 1234

# Account balance of INSS-505
balance = 10000

# Variables
# user_pin = 0
# user_withdrawal = 0
# user_exit = 0
#
while attempts > 0:
    user_pin = int(input("Enter Your Four Digit PIN:\n"))

# User is prompted to enter PIN, after 3 tries, the card is confiscated
    if user_pin != pin:
        attempts -= 1
        print("Invalid PIN,Please Enter a valid PIN!\n"
               "You have", attempts, "Tries left")

# If the correct PIN is inputted then user can access the menu of the system
    else:
        access_menu = input(" Select Transaction: D-deposit(cash or check),W-withdrawal:   \n")

# For Deposit, the Code is as follows:
        if access_menu == "D":
            user_deposit = int(input("Enter amount to deposit:   $"))
            balance += user_deposit
            print("You have successfully deposited $",user_deposit, "to your account\n")
            print("total balance is:", balance)

# Alternatively, a User can initiate a Withdrawal Request.
# Withdrawal could fail if the requested withdrawal amount is greater than the account balance.
        elif access_menu == "W":
            user_withdrawal = int(input("Enter the amount to withdraw:   $"))
            if user_withdrawal > balance:
                print("Invalid amount, please enter a valid amount")
            else:
                balance -= user_withdrawal
                print("You have successfully withdrawn $", user_withdrawal)
        print("total balance is:","$",balance)

# After a withdrawal or deposit transaction is completed, th system prompts the user to go again or exit.
        user_exit = input("Do you want to perform another transaction? Continue : Yes, Exit : No:   ")
        if user_exit == "Yes":
            continue
        else:
            print("please remove card, thank you!")
            break
"""The system is designed to break the loop if anything other than a yes is inputted.
    This will be considered as human error"""