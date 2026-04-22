class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
        self.history = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.history.append(f"Deposited: {amount}")
            print(f"Deposited: {amount} | New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            self.history.append(f"Withdrawn: {amount}")
            print(f"Withdrawn: {amount} | New balance: {self.balance}")

    def check_balance(self):
        print(f"Current balance: {self.balance}")

    def show_history(self):
        print("\nTransaction History:")
        for h in self.history:
            print("-", h)


# Simple menu system (THIS makes it a real project)
account = BankAccount(100)

while True:
    print("\n===== BANK SYSTEM =====")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Transaction History")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        amount = float(input("Enter deposit amount: "))
        account.deposit(amount)

    elif choice == "2":
        amount = float(input("Enter withdrawal amount: "))
        account.withdraw(amount)

    elif choice == "3":
        account.check_balance()

    elif choice == "4":
        account.show_history()

    elif choice == "5":
        print("Thank you for using the bank system.")
        break

    else:
        print("Invalid choice, try again.")