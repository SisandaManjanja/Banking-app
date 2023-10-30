# Define the file names for bank data and transaction log
bank_data_file = "Bank Data.txt"
transaction_log_file = "Transaction Log.txt"

# Function to create bank data file if it doesn't exist
def create_bank_data_file():
    try:
        with open(bank_data_file, "x") as file:
            file.write("0.0")
    except FileExistsError:
        pass  # The file already exists, no need to create it

# Function to create transaction log file if it doesn't exist
def create_transaction_log_file():
    try:
        with open(transaction_log_file, "x"):
            pass  # Create an empty file
    except FileExistsError:
        pass  # The file already exists, no need to create it

# Function to get the current balance
def get_balance():
    create_bank_data_file()  # Ensure the file exists
    try:
        with open(bank_data_file, "r") as file:
            balance = file.read()
            if not balance:
                balance = "0.0"
            return float(balance)
    except FileNotFoundError:
        return 0.0

# Function to make a deposit
def make_deposit():
    amount = input("How much would you like to deposit? R")
    try:
        amount = float(amount)
        if amount <= 0:
            raise ValueError
    except ValueError:
        print("Invalid input. Please provide a valid positive number for the deposit.")
        return

    balance = get_balance()
    balance += amount

    with open(bank_data_file, "w") as file:
        file.write(str(balance))

    with open(transaction_log_file, "a") as file:
        file.write(f"Deposit: +R{amount}\n")

    print(f"Current Balance: R{balance}")

# Function to make a withdrawal
def make_withdrawal():
    amount = input("How much would you like to withdraw? R")
    try:
        amount = float(amount)
        if amount <= 0:
            raise ValueError
    except ValueError:
        print("Invalid input. Please provide a valid positive number for the withdrawal.")
        return

    balance = get_balance()
    if amount > balance:
        print("Insufficient funds for the withdrawal.")
        return

    balance -= amount

    with open(bank_data_file, "w") as file:
        file.write(str(balance))

    with open(transaction_log_file, "a") as file:
        file.write(f"Withdrawal: -R{amount}\n")

    print(f"Current Balance: R{balance}")

# Main program
create_bank_data_file()  # Ensure the file exists
create_transaction_log_file()  # Ensure the file exists

while True:
    print("Would you like to make a transaction? (Yes or No)")
    user_choice = input().strip().lower()

    if user_choice != "yes":
        break

    print("Would you like to make a deposit or withdrawal? (Deposit or Withdrawal)")
    transaction_type = input().strip().lower()

    if transaction_type == "deposit":
        print(f"Current Balance: R{get_balance()}")
        make_deposit()
    elif transaction_type == "withdrawal":
        print(f"Current Balance: R{get_balance()}")
        make_withdrawal()
    else:
        print("You provided an invalid input. Please choose 'Deposit' or 'Withdrawal'.")

print("Thank you for using the banking application.")