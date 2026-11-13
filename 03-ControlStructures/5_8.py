###
# ATM (cash machine) simulator
#
from validators import read_int
balance = 1000  # Initial balance
pin = '1111'

while True:
    print()
    print("ATM Menu:")
    print("1. Check balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    print("5. Check PIN")
    print("6. Change PIN")

    choice = input("Choose an option (1-6): ")
    print()

    if choice == '1':
        print(f"Your current balance is: €{balance}")
    elif choice == '2':
        amount = float(input("Enter the amount to deposit: "))
        balance += amount
        print(f"€{amount} has been deposited. New balance: €{balance}")
    elif choice == '3':
        amount = float(input("Enter the amount to withdraw: "))
        if amount <= balance:
            balance -= amount
            print(f"€{amount} has been withdrawn. New balance: €{balance}")
        else:
            print("Insufficient balance.")
    elif choice == '4':
        print("Exiting... Thank you for using the ATM!")
        break
    elif choice == '5':
        entered_pin = input("Enter your PIN: ")
        if entered_pin == pin:
            print("PIN is correct.")
        else:
            print("Incorrect PIN.")
    elif choice == '6':
        current_pin = read_int("Enter your current PIN: ", 0, 9999)
        if current_pin == pin:
            new_pin = read_int("Enter your new 4-digit PIN: ", 0, 9999)
            if len(new_pin) == 4 and new_pin.isdigit():
                confirm_pin = read_int("Confirm your new PIN: ", 0, 9999)
                if confirm_pin == new_pin:
                    pin = new_pin
                    print("Your PIN has been changed successfully.")
                else:
                    print("PINs do not match.")
            else:
                print("Invalid PIN. It must contain exactly 4 digits.")
        else:
            print("Incorrect current PIN. PIN was not changed.")
    else:
        print("Invalid option. Please try again.")