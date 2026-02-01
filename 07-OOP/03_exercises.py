"""
===== OOP: EXERCISES =====
"""

print("=" * 50)
print("OOP EXERCISES")
print("=" * 50)
print()

# ===== EXERCISE 1: Rectangle Class =====
print("EXERCISE 1: Rectangle Class")
print("-" * 40)

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
    
    def info(self):
        return f"Rectangle {self.width}x{self.height}"

rect = Rectangle(10, 5)
print(rect.info())
print(f"Area: {rect.area()}")
print(f"Perimeter: {rect.perimeter()}")

print()

# ===== EXERCISE 2: Temperature Class =====
print("EXERCISE 2: Temperature Converter")
print("-" * 40)

class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius
    
    def to_fahrenheit(self):
        return (self.celsius * 9/5) + 32
    
    def to_kelvin(self):
        return self.celsius + 273.15

temp = Temperature(25)
print(f"Celsius: {temp.celsius}°C")
print(f"Fahrenheit: {temp.to_fahrenheit():.2f}°F")
print(f"Kelvin: {temp.to_kelvin():.2f}K")

print()

# ===== EXERCISE 3: Employee Class =====
print("EXERCISE 3: Employee Class")
print("-" * 40)

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def give_raise(self, amount):
        self.salary += amount
    
    def info(self):
        return f"{self.name}: ${self.salary}"

emp = Employee("Usman", 50000)
print(emp.info())

emp.give_raise(5000)
print(f"After raise: {emp.info()}")

print()

# ===== EXERCISE 4: Inheritance =====
print("EXERCISE 4: Animal Inheritance")
print("-" * 40)

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def info(self):
        return f"{self.name}, age {self.age}"

class Dog(Animal):
    def bark(self):
        return f"{self.name} barks: Woof!"

dog = Dog("Buddy", 3)
print(dog.info())
print(dog.bark())

print()

# ===== EXERCISE 5: Bank Account Class =====
print("EXERCISE 5: Bank Account")
print("-" * 40)

class BankAccount:
    def __init__(self, holder, balance=0):
        self.holder = holder
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds")
    
    def get_balance(self):
        return self.balance

account = BankAccount("Umair", 1000)
account.deposit(500)
account.withdraw(200)
print(f"{account.holder}: ${account.get_balance()}")

print()

print("=" * 50)
print("WELL DONE!")
print("=" * 50)
