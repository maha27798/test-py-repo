# operator overloading
'''class Addition:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return self.a + self.b + other.a + other.b
obj1 = Addition(1, 2)
obj2 = Addition(3, 4)
result = obj1 +  obj2  # invokes obj1.__add__(obj2)
print("Addition:", result) 

 # method overloading using default arguments
class MathOperations:
    def multiply(self, a, b=1, c=1):
        return a * b * c
math = MathOperations()
print("Multiply 2 numbers:", math.multiply(2, 3))        
print("Multiply 3 numbers:", math.multiply(2, 3, 4)) '''

# let create a class circle with radius attribute and methods to calculate area and perimeter
'''class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius
    def perimeter(self):
        return 2 * 3.14 * self.radius
    
c1 = Circle(5)
print("Area:", c1.area())
print("Perimeter:", c1.perimeter())'''

# create a class Employee with attributes role, salary and department. Include a method to display employee details,
# create engineer class that inherits from Employee and adds attributes: age and name;
'''class Employee:
    def __init__(self, role, salary ,department):
        self.role = role
        self.salary = salary
        self.dep = department
    def show_details(self):
        print("Role:", self.role)
        print("Salary:", self.salary)
        print("Dep:", self.dep)
class Engineer(Employee):
    def __init__(self, role, salary, department, age=None, name=None):
        super().__init__(role, salary, department)
        self.age = age
        self.name = name
    def show_details(self):
        super().show_details()
        print("Name:", self.name)
        print("Age:", self.age)
e1 = Employee("Developer", 60000, "IT")
e1.show_details()
e2 = Employee("Manager", 80000, "HR")
e2.show_details()
eng1 = Engineer("Software Engineer", 70000, "IT", 30, "Maha")
eng1.show_details()'''

 #create a clas called orders which stores items and its prices,use dunder function__get__() to convey that:
 #  order1>order2 if price of order1 > order2
'''class Orders:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self, other):
        return self.price > other.price
order1 = Orders("Laptop", 1000)
order2 = Orders("Tablet", 500)
if order1 > order2:
    print(f"{order1.item} is more expensive than {order2.item}")
else:
    print(f"{order2.item} is more expensive than {order1.item}")'''
