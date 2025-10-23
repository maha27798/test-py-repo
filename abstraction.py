class BankAccount:
    def __init__(self, balance):
        self.__balance = balance   # hidden (private)

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance
account = BankAccount(1000)
account.deposit(500)
print("Balance:", account.get_balance())  # Access via method