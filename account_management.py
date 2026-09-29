import datetime
import time


def create_view(accounts):
    print("1. Create Account  2. View Account")
    try:
        c = int(input("Enter Your Choice Index Number :- "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    if c == 1:
        try:
            account_number = int(input("Enter Your Account Number :- "))
            if account_number in accounts:
                print("Account Number Already Exists")
            else:
                name = input("Enter Your Name :- ")
                phone_number = int(input("Enter Your Phone Number :- "))
                balance = int(input("Enter Opening Bank Balance :- "))
                accounts[account_number] = {
                    "Name": name,
                    "Balance": balance,
                    "Phone Number": phone_number,
                }
                print("Your Account Has Been Created Successfully")
        except ValueError:
            print("Invalid numerical input. Account creation failed.")
    elif c == 2:
        while True:
            try:
                account_number = int(
                    input("Enter Your Account Number To View Your Account :- ")
                )
                if account_number in accounts:
                    print(accounts[account_number])
                    break
                else:
                    print("Account Number NOT Found, Try Again")
            except ValueError:
                print("Please enter a valid numeric Account Number.")
    else:
        print("Wrong Index Number")


def update_delete(accounts):
    print("1. Update  2. Delete")
    try:
        c = int(input("Enter Your Choice Index Number :- "))
        account_number = int(input("Enter Your Account Number :- "))
    except ValueError:
        print("Invalid input type.")
        return

    if account_number not in accounts:
        print("Your Account Number Not Found")
        return

    if c == 1:
        new_phone = input("Enter New Phone Number :- ")
        accounts[account_number]["Phone Number"] = new_phone
        print("Your Account Has Been Updated")
    elif c == 2:
        del accounts[account_number]
        print("Account Deleted")
    else:
        print("Your Chosen Index Number Is Wrong")


def check_balance(accounts):
    while True:
        try:
            account_number = int(input("Enter Your Account Number :- "))
            if account_number in accounts:
                print(
                    "Your Account Balance Is :-",
                    accounts[account_number]["Balance"],
                )
                break
            else:
                print("Your Account Number NOT Found, Try Again")
        except ValueError:
            print("Please enter a valid numeric Account Number.")


def history(accounts, transactions):
    try:
        account_number = int(input("Enter Your Account Number :- "))
        if account_number in accounts:
            print("Transaction History :- ")
            found = False
            for t in transactions:
                if t[0] == account_number:
                    print(t)
                    found = True
            if not found:
                print("No transactions found for this account.")
        else:
            print("Your Account NOT Found")
    except ValueError:
        print("Invalid Account Number input.")
