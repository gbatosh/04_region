class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit of {amount} accepted. New balance is {self.balance}.")
        else:
            print("invalid deposit amount. deposit amount must be positive.")
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"withdrawal of {amount} accepted. new balance is {self.balance}.")
        else:
            print("invalid withdrawal amount. withdrawal amount must be less than or equal to the balance.")
account = BankAccount("gbatyrbek")
account.deposit(100)
account.deposit(50)
account.withdraw(30)
account.withdraw(200) 
account.deposit(-10)
