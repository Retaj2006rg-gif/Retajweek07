
# =========================
# Lab7 - Question 1
# =========================

try:
    number1 = float(input('Enter first number: '))
    number2 = float(input('Enter second number: '))
    result = number1 / number2
except ZeroDivisionError:
    print('division by zero')
except ValueError:
    print('text entered')
else:
    print('The result:', result)



# =========================
# Lab7 - Question 2
# =========================

class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age

pe = Person('Retaj', 21)
pe._age = 22
print('name:', pe.name, 'age:', pe._age)



# =========================
# Lab7 - Question 3
# =========================

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def add_bonus(self, amount):
        self.salary = self.salary + amount

    def display_info(self):
        print("Manager Name:", self.name)
        print("Total Salary:", self.salary)

my_manager = Manager("Retaj", 990)
my_manager.add_bonus(720)
my_manager.display_info()



# =========================
# Lab7 - Question 4
# =========================

class Student:
    def __init__(self):
        self.name = input("Enter student name: ")
        try:
            self.age = int(input("Enter student age: "))
            if self.age < 0:
                print("Error: Age cannot be negative!")
                self.age = None
        except ValueError:
            print("Please enter a valid number for age")
            self.age = None

    def display(self):
        if self.age is not None:
            print("Student Name:", self.name)
            print("Student Age:", self.age)

my_student = Student()
my_student.display()