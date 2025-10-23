#class in Python
'''class Student:
    name = "Maha Fatima"
    
    s1 = Student()
print(s1.name)'''
#class in Python with __init__ method
'''
 # default constructor
def __init__(self):
     pass'''
# 2:parameterized constructor
'''class Student:
 # parameterized constructor
 def __init__(self, name="Maha Fatima", age=20):
        self.name = name
        self.age = age

s1 = Student()
print(s1.name)
print(s1.age)
'''
#ATTRIBUTES AND METHODS
# object.attribute
# class.attribute

# method()
# def hello():
#     print("Hello, World!")
# hello()
#3:parameterized constructor with multiple attributes
'''
 parameterized constructor
 def __init__(self, name="Maha Fatima", mark1=220, mark2=230, mark3=210,avg=0):
        self.name = name
        self.mark1 = mark1
        self.mark2 = mark2
        self.mark3 = mark3
        avg = (mark1 + mark2 + mark3) / 3
        self.avg = avg
s1 = Student()
print(s1.name)
print(s1.mark1)
print(s1.mark2)
print(s1.mark3)
print(s1.avg)'''

# STATIC METHODS(NO SELF PARAMETER)....work at class level not at object level
# class Student:
#     @staticmethod #decorator
#     def college():
#         print("ABC College of Engineering")

# ABSTRACTION (hide unnecessary information)
'''
class Car:
    def __init__(self):
        self.brk = False
        self.acc = False
        self.clutch= False

    def start(self):
         self.brk = True
         self.acc = True
         print("Car start")
Car1 = Car()
Car1.start()
'''
#encapsulation (store data and function together in a single unit(OBJECT))

'''class Account:
    def __init__(self, balance=0 , account_number="1234567890"):
     self.account_number = account_number
     self.balance = balance

    def debit(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Debited: {amount}")
        else:
            print("Insufficient balance")
    def credit(self, amount):
        self.balance += amount
        print(f"Credited: {amount}")
        def get_balance(self):
            return self.balance
acc1 = Account(1000)
acc1.debit(500)
acc1.credit(200)
print(f"Current Balance: {acc1.balance}")'''

#del keyword to delete object
class Account:
    def __init__(self, balance=0 , account_number="1234567890"):
     self.account_number = account_number
     self.balance = balance

    def debit(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Debited: {amount}")
        else:
            print("Insufficient balance")
    def credit(self, amount):
        self.balance += amount
        print(f"Credited: {amount}")
        def get_balance(self):
            return self.balance
acc1 = Account(1000)
acc1.debit(500)
acc1.credit(200)
del acc1
print("Account deleted")
print(f"Current Balance: balance")  # This will raise an error since acc1 is deleted