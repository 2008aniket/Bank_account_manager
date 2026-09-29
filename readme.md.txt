# Vityarthi — Bank Management System

A Python-based Bank Management System developed as a college project for VIT Bhopal University. This console-driven application provides end-to-end management of bank account operations, financial transactions, loan processing, EMI calculations, and simulated ATM services.

# ================================================================================
FEATURES

* Account Management: Create new accounts, view account details, update registered phone numbers, and delete existing accounts.


* Banking Operations: Deposit cash, withdraw funds, and perform real-time account balance checks.


* Transaction Tracking: Log all account deposits, withdrawals, and ATM usage with timestamps and view transaction history.


* Loan Services: Apply for loans with automatic EMI calculations based on interest rate and loan tenure, view loan statuses, and calculate remaining payable amounts.


* EMI Management: Pay monthly loan EMIs and track payment history.


* ATM Service Simulation: Simulate card-based ATM withdrawals with automatic balance deduction and transaction records.



# ================================================================================
PROJECT STRUCTURE

├── main.py                 # Core application menu loop and state initialization
├── account_management.py   # Account creation, updating, deletion, balance check, & history
├── banking_operations.py   # Cash deposit/withdrawal and ATM simulation routines
└── loan_services.py        # Loan creation, EMI calculations, payments, and history

# ================================================================================
REQUIREMENTS

* Python 3.x (No external third-party libraries required; uses built-in Python modules like datetime and time).



# ================================================================================
USAGE / HOW TO RUN

1. Clone or download this repository to your local computer.
2. Open your terminal or command prompt and navigate to the directory containing the project files:
cd path/to/vityarthi-project
3. Run the main script:
python main.py
4. Follow the interactive menu prompts on the terminal screen.



# ================================================================================
MENU NAVIGATION

Upon execution, the terminal displays the following options:

1. Create / View Account: Open a new bank account or view existing details using an account number.


2. Update / Delete Account: Modify the contact phone number or close an account.


3. Check Balance: Query available account balance.


4. Deposit / Withdrawal: Perform standard bank transactions.


5. Transaction History: Output all recorded financial movements for a given account.


6. Loan Section: Apply for loans or view current loan agreements.


7. EMI Services: Pay installments, view repayment history, and check total interest costs.


8. ATM Section: Simulate ATM cash withdrawal using card and PIN inputs.


9. Exit: Terminate the program execution safely.