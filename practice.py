# class Car:
#     def __init__(self, brand, model, year):   # Constructor
#         self.brand = brand
#         self.model = model
#         self.year = year

#     def display_info(self):                   # function
#         print(f"Car: {self.brand} {self.model} {self.year}")

# car1 = Car("Toyota", "Corolla", 2020)         # Object creation
# car2 = Car("Tesla", "Model S", 2024)

# car1.display_info()
# car2.display_info()


# # Q2. Create a class Employee that: Takes name and salary as input.Has a method bonus() that adds 10% bonus to salary.Displays the final salary.

# class Employee:
#      def __init__(self, name="maha", salary="1000"):
#          self.name = name
#          self.salary = salary
#      def bonus(self):
#         self.salary += self.salary*0.10
#      def display(self):
#          print(f"Car: {self.name} {self.salary}")
         
# E1=Employee("maha", 1000)
# E1.display()
# E1.bonus()

# # Write a program with two classes: Person (parent) and Student (child).Use inheritance to make 
# # Student inherit from Person.Add methods to display both personal and academic info.
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def display_person(self):
#         print(f"Name: {self.name}, Age: {self.age}")

# class Student(Person):    # Inherits from Person
#     def __init__(self, name, age, roll_no, course):
#         super().__init__(name, age)
#         self.roll_no = roll_no
#         self.course = course

#     def display_student(self):
#         self.display_person()
#         print(f"Roll No: {self.roll_no}, Course: {self.course}")

# stu1 = Student("Maha", 20, 101, "Software Engineering")
# stu1.display_student()


# ✳️ Q4. Create a class Account that: Has a private attribute __balance.Allows deposit, withdraw, 
# and balance check using methods only.Prevents direct access to __balance.


class Account:
    def __init__(self, balance, account_number):
        self.__balance = balance
        self.acc_no = account_number

    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited {amount}. New balance: {self.__balance}")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance: {self.__balance}")
        else:
            print("Insufficient funds!")

    def check(self):
        print(f"Current balance: {self.__balance}")

acc1 = Account(1000, 121)

acc1.deposit(500)
acc1.withdraw(200)
acc1.check()



             

         

# ✳️ Q5. Create a program that shows polymorphism using classes Bird and Fish.

# Both should have a method move() — birds “fly”, fish “swim”.

# ✳️ Q6. Create a Rectangle class that:

# Has attributes length and width

# Has methods area() and perimeter()

# Creates multiple rectangles and prints results.

# ✳️ Q7. Create a class variable that counts how many objects have been created from the class.

# Example Output:

# Total Students Created: 3

# ✳️ Q8. Create a Library system:

# Books are stored as objects.

# Each book has title, author, and availability status.

# Methods: borrow(), return_book(), and show_info()

# ✳️ Q9. Create a class Temperature that:

# Converts Celsius to Fahrenheit and vice versa using methods.

# ✳️ Q10. Create a class BankAccount with:

# Owner’s name and balance.

# Methods: deposit(), withdraw(), display_balance().

# Prevent negative balance and handle invalid inputs.

         