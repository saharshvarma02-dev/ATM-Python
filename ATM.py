import sqlite3
conn = sqlite3.connect('bank.db')
cursor = conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS accounts(
    name TEXT,
    account_number TEXT PRIMARY KEY,
    pin TEXT,
    balance REAL
)""")
conn.commit()

def create_account(name, account_number, pin):
    cursor.execute("SELECT * FROM accounts WHERE account_number = ?", (account_number,))
    if cursor.fetchone():
        print("Account already exists.")
        return
    cursor.execute("INSERT INTO accounts VALUES (?, ?, ?, ?)", (name, account_number, pin, 0))
    conn.commit()
    print("Account created successfully.")

class BankAccount:
    def __init__(self, name, account_number, balance = 0):
        self.name = name
        self.account_number = account_number
        self.balance = balance
    # Deposit
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount.")
    # Withdraw
    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
    # Check Balance
    def check_balance(self):
        print(f"Current balance: ${self.balance}")

name = input("Enter account holder's name: ")
acc_no = input("Enter account number: ")
account = BankAccount(name, acc_no)
while True:
    print("\n---Banking menu---")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        name = input("Name: ")
        acc_no = input("Account number: ")
        pin = input("Set PIN: ")
        create_account(name, acc_no, pin)
    elif choice == '2':
        amount = float(input("Enter amount to deposit: "))
        account.deposit(amount)
    elif choice == '3':
        amount = float(input("Enter amount to withdraw: "))
        account.withdraw(amount)
    elif choice == '4':
        account.check_balance()
    elif choice == '5':
        print("Thank you for using our services.")
        break
    else:
        print("Invalid choice. Please try again.")