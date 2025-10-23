'''class Student:
    def __init__(self, name, age):
        self.name = name          # public attribute
        self.__age = age          # private attribute

    def show_info(self):
        print("Name:", self.name)
        print("Age:", self.__age)

# Create object
s = Student("Maha", 20)
s.show_info()

# Try to access directly
print(s.name)       
print(s.__age)'''
class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def __show_balance(self):     # private method
        print("Balance:", self.__balance)

    def access_balance(self):     # public method
        print("Accessing private method...")
        self.__show_balance()

# Create object
acc = Account("Maha", 5000)

acc.access_balance()  # ✅ Works
acc.__show_balance()  # ❌ Error
