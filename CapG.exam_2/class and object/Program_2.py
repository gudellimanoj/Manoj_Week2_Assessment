# Design a `BankAccount` class with `deposit()` and `withdraw()` methods. Implement logic to prevent overdraft.

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrawn: {amount}")
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.balance

    def display(self):
        print(f"Balance: {self.balance}")

obj = BankAccount(1000)
obj.display()
obj.deposit(500)
obj.display()
obj.withdraw(200)
obj.display()
obj.withdraw(2000)
obj.display()


