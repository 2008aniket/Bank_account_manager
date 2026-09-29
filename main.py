import account_management as am
import banking_operations as bo
import loan_services as ls

# Shared Data Structures
Accounts = {}
Transactions = []
Loans = []
EMI_History = []
ATM_Storage = []


def main():
    while True:
        print("\n=== Bank Management System ===")
        print("1. Create / View Account")
        print("2. Update / Delete Account")
        print("3. Check Balance")
        print("4. Deposit / Withdrawal")
        print("5. Transaction History")
        print("6. Loan Section")
        print("7. EMI Services")
        print("8. ATM Section")
        print("9. Exit")

        try:
            choice = int(input("Enter Your Choice Index :- "))
            if choice == 1:
                am.create_view(Accounts)
            elif choice == 2:
                am.update_delete(Accounts)
            elif choice == 3:
                am.check_balance(Accounts)
            elif choice == 4:
                bo.deposit_withdraw(Accounts, Transactions)
            elif choice == 5:
                am.history(Accounts, Transactions)
            elif choice == 6:
                ls.handle_loan(Accounts, Loans)
            elif choice == 7:
                ls.handle_emi(Accounts, Loans, EMI_History)
            elif choice == 8:
                bo.atm_service(Accounts, Transactions, ATM_Storage)
            elif choice == 9:
                print("THANK YOU FOR USING OUR SERVICES")
                break
            else:
                print("Your Chosen Choice Index Is Wrong")
        except ValueError:
            print("Please enter a valid numeric choice from the menu.")


if __name__ == "__main__":
    main()
