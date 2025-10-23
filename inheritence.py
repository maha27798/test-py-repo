class Parent:
    def func1(self):
        print("This is from the Parent class")

class Child(Parent):
    def func2(self):
        print("This is from the Child class")

obj = Child()
obj.func1()  # Inherited from Parent
obj.func2()  # From Child
#TYPES OF INHERITENCE
#1. Single Inheritence
'''class Animal:
    def speak(self):
        print("Animal speaks")
class Dog(Animal):
    def bark(self):
        print("Dog barks")
dog = Dog()
dog.speak()  # Inherited from Animal'''
#2. Multi-level Inheritence
'''class Animal:
    def speak(self):
        print("Animal speaks")
class Dog(Animal):
    def bark(self):
        print("Dog barks")
class Puppy(Dog):
    def weep(self):
        print("Puppy weeps")
puppy = Puppy()
puppy.speak()  # Inherited from Animal'''
#3. Multiple Inheritence
'''class Father:
    def skills(self):
        print("Gardening, Programming")
class Mother:
    def skills(self):
        print("Cooking, Art")
class Child(Father, Mother):
    def skills(self):
        Father.skills(self)
        Mother.skills(self)
        print("Sports")
c = Child()
c.skills()  # Inherited from both Father and Mother'''
#4. Hierarchical Inheritence
'''class Parent:
    def func1(self):
        print("This is from the Parent class")
class Child1(Parent):
    def func2(self):
        print("This is from Child1 class")
class Child2(Parent):
    def func3(self):
        print("This is from Child2 class")
obj1 = Child1()

obj1.func1()  # Inherited from Parent
obj1.func2()  # From Child1
obj2 = Child2()
obj2.func1()  # Inherited from Parent
obj2.func3()  # From Child2'''
#5. Hybrid Inheritence 
'''class School:
    def func1(self):
        print("This is from the School class")
class Student(School):
    def func2(self):
        print("This is from the Student class")
class Teacher(School):
    def func3(self):
        print("This is from the Teacher class")
class TA(Student, Teacher):
    def func4(self):
        print("This is from the TA class")
obj = TA()
obj.func1()  # Inherited from School
obj.func2()  # Inherited from Student
obj.func3()  # Inherited from Teacher
obj.func4()  # From TA'''
#SUPER() FUNCTION
'''class Parent:
    def show(self):
        print("Parent class method")
class Child(Parent):
    def show(self):
        super().show()  # Call Parent's show()
        print("Child class method")
obj = Child()
obj.show()'''


# staticmethod
# classmethod
# instance method
# property decorator
# getter and setter methods