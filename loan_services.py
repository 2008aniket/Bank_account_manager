import time


def handle_loan(accounts, loans):
    print("1. Add Loan  2. View Loan")
    try:
        choice = int(input("Enter Your Choice Index :- "))
    except ValueError:
        print("Invalid Input")
        return

    if choice == 1:
        try:
            account_number = int(input("Enter Your Account Number :- "))
            if account_number in accounts:
                loan_type = input("Enter The Type Of Your Loan :- ")
                loan_amount = int(input("Enter The Amount Of Your Loan :- "))
                rate_of_interest = float(
                    input(
                        "Enter Annual Rate Of Interest (in Percentage) :- "
                    )
                )
                loan_duration = int(
                    input("Enter Duration Of Loan In Months :- ")
                )

                total_interest = (loan_amount * rate_of_interest) / 100
                total_payable = loan_amount + total_interest
                emi_val = round(total_payable / loan_duration, 2)

                loans.append(
                    {
                        "Account_Number": account_number,
                        "Type": loan_type,
                        "EMI": emi_val,
                        "Amount": loan_amount,
                        "Loan_Duration": loan_duration,
                        "ID": account_number,
                        "Remaining": total_payable,
                    }
                )
                print(f"Loan Approved! Monthly EMI Is :- {emi_val}")
            else:
                print("Account Number NOT Found")
        except ValueError:
            print("Invalid numerical inputs provided.")
    elif choice == 2:
        try:
            account_number = int(input("Enter Your Account Number :- "))
            found = False
            for l in loans:
                if l["Account_Number"] == account_number:
                    print(
                        f"Loan ID: {l['ID']} | EMI: {l['EMI']} | Remaining Payable: {l['Remaining']}"
                    )
                    found = True
            if not found:
                print("Record Of Loan NOT Found")
        except ValueError:
            print("Invalid Account Number.")


def handle_emi(accounts, loans, emi_history):
    print("1. Pay EMI  2. EMI History  3. Remaining And Interest")
    try:
        choice = int(input("Enter Your Choice Index Number :- "))
    except ValueError:
        print("Invalid Choice")
        return

    if choice == 1:
        try:
            loan_id = int(input("Enter Your Loan ID :- "))
            found = False
            for l in loans:
                if l["ID"] == loan_id:
                    amount = int(input("Enter Amount To Pay :- "))
                    l["Remaining"] -= amount
                    emi_history.append(
                        [loan_id, amount, time.strftime("%d-%m-%Y")]
                    )
                    print(
                        f"Amount Paid. Remaining Loan Balance: {l['Remaining']}"
                    )
                    found = True
                    break
            if not found:
                print("Your Loan ID NOT Found")
        except ValueError:
            print("Invalid inputs.")

    elif choice == 2:
        try:
            loan_id = int(input("Enter Your Loan ID :- "))
            found = False
            for e in emi_history:
                if e[0] == loan_id:
                    print(e)
                    found = True
            if not found:
                print("No EMI History Found")
        except ValueError:
            print("Invalid Loan ID")

    elif choice == 3:
        try:
            account_number = int(input("Enter Your Account Number :- "))
            if account_number in accounts:
                for l in loans:
                    if l["Account_Number"] == account_number:
                        total_payable = l["EMI"] * l["Loan_Duration"]
                        interest = total_payable - l["Amount"]
                        print(
                            f"Loan ID: {l['ID']} | Remaining: {l['Remaining']} | Total Calculated Interest: {interest}"
                        )
            else:
                print("Your Account NOT Found")
        except ValueError:
            print("Invalid Account Number.")
