"""
===== OOP: CLASSES AND OBJECTS =====

A class is a blueprint for creating objects.
An object is an instance of a class.
"""

# === SIMPLE CLASS ===
print("=== SIMPLE CLASS ===")

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def bark(self):
        print(f"{self.name} says: Woof!")
    
    def get_info(self):
        return f"{self.name} is {self.age} years old"

# Create objects
dog1 = Dog("Sharjeel", 3)
dog2 = Dog("Amir", 5)

print(dog1.get_info())
print(dog2.get_info())

dog1.bark()
dog2.bark()

print()

# === CLASS ATTRIBUTES ===
print("=== CLASS ATTRIBUTES ===")

class Car:
    # Class attribute (shared by all instances)
    wheels = 4
    
    def __init__(self, brand, model):
        # Instance attributes (unique to each object)
        self.brand = brand
        self.model = model
    
    def info(self):
        return f"{self.brand} {self.model} has {Car.wheels} wheels"

car1 = Car("Toyota", "Camry")
car2 = Car("Honda", "Civic")

print(car1.info())
print(car2.info())
print(f"All cars have {Car.wheels} wheels")

print()

# === MODIFY ATTRIBUTES ===
print("=== MODIFY ATTRIBUTES ===")

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def birthday(self):
        self.age += 1
        print(f"Happy birthday, {self.name}!")

person = Person("Umair", 25)
print(f"{person.name} is {person.age} years old")

person.birthday()
print(f"{person.name} is now {person.age} years old")

print()

# === METHODS ===
print("=== METHODS ===")

class Calculator:
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        if b == 0:
            return "Cannot divide by zero"
        return a / b

calc = Calculator()
print(f"10 + 5 = {calc.add(10, 5)}")
print(f"10 - 5 = {calc.subtract(10, 5)}")
print(f"10 * 5 = {calc.multiply(10, 5)}")
print(f"10 / 5 = {calc.divide(10, 5)}")

print()

# === SPECIAL METHODS ===
print("=== SPECIAL METHODS ===")

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    # String representation
    def __str__(self):
        return f"'{self.title}' by {self.author}"
    
    # Length
    def __len__(self):
        return len(self.title)

book = Book("Python Guide", "Usman Khan")
print(str(book))
print(f"Title length: {len(book)}")

print()

# === PRACTICAL EXAMPLE: STUDENT CLASS ===
print("=== PRACTICAL: STUDENT CLASS ===")

class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = []
    
    def add_grade(self, grade):
        self.grades.append(grade)
    
    def get_average(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)
    
    def get_info(self):
        avg = self.get_average()
        return f"{self.name} (ID: {self.student_id}) - Average: {avg:.2f}"

student = Student("Umair", "STU001")
student.add_grade(85)
student.add_grade(90)
student.add_grade(88)

print(student.get_info())

print()

# === PRACTICAL EXAMPLE: BANK ACCOUNT ===
print("=== PRACTICAL: BANK ACCOUNT ===")

class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Deposit amount must be positive")
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
    
    def get_balance(self):
        return self.balance

account = BankAccount("Usman", 1000)
account.deposit(500)
account.withdraw(200)
print(f"Final balance: ${account.get_balance()}")
