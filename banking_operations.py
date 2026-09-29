import datetime
import time


def deposit_withdraw(accounts, transactions):
    while True:
        try:
            account_number = int(input("Enter Your Account Number :- "))
            if account_number in accounts:
                print("1. Deposit  2. Withdraw")
                choice = int(input("Enter Your Choice Index Number :- "))
                amount = int(input("Enter The Amount Of Money :- "))

                if choice == 1:
                    accounts[account_number]["Balance"] += amount
                    transactions.append(
                        [
                            account_number,
                            "Deposit",
                            amount,
                            time.strftime("%d-%m-%Y"),
                        ]
                    )
                    print(
                        "Amount Deposited. Current Account Balance:",
                        accounts[account_number]["Balance"],
                    )
                elif choice == 2:
                    if accounts[account_number]["Balance"] >= amount:
                        accounts[account_number]["Balance"] -= amount
                        transactions.append(
                            [
                                account_number,
                                "Withdraw",
                                amount,
                                str(datetime.date.today()),
                            ]
                        )
                        print(
                            "Withdrawal Successful. Current Account Balance:",
                            accounts[account_number]["Balance"],
                        )
                    else:
                        print("NOT Enough Balance In Your Account")
                else:
                    print("Invalid Choice")
                break
            else:
                print("Your Account NOT Found")
                break
        except ValueError:
            print("Invalid entry. Please use numerical digits.")
            break


def atm_service(accounts, transactions, atm_storage):
    try:
        account_number = int(input("Enter Account Number :- "))
        if account_number in accounts:
            card = input("Enter Your Card Number :- ")
            pin = input("Enter Your PIN :- ")
            amount = int(input("Enter ATM Withdrawal Amount :- "))

            if accounts[account_number]["Balance"] >= amount:
                accounts[account_number]["Balance"] -= amount
                atm_storage.append(
                    [
                        account_number,
                        card,
                        "ATM Withdraw",
                        amount,
                        str(datetime.date.today()),
                    ]
                )
                transactions.append(
                    [
                        account_number,
                        "ATM Withdrawal",
                        amount,
                        str(datetime.date.today()),
                    ]
                )
                print(
                    "ATM Withdrawal Successful! Current Balance:",
                    accounts[account_number]["Balance"],
                )
            else:
                print("Low Balance In Account")
        else:
            print("Account Number Not Found")
    except ValueError:
        print("Invalid numeric values entered.")
