"""
===== OOP: INHERITANCE =====

Inheritance allows one class to inherit from another.
"""

# === SIMPLE INHERITANCE ===
print("=== SIMPLE INHERITANCE ===")

class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return f"{self.name} makes a sound"

class Dog(Animal):
    def speak(self):
        return f"{self.name} says: Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says: Meow!"

dog = Dog("Buddy")
cat = Cat("Whiskers")

print(dog.speak())
print(cat.speak())

print()

# === SUPER() FUNCTION ===
print("=== SUPER() FUNCTION ===")

class Vehicle:
    def __init__(self, brand):
        self.brand = brand
    
    def info(self):
        return f"Brand: {self.brand}"

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model
    
    def info(self):
        parent_info = super().info()
        return f"{parent_info}, Model: {self.model}"

car = Car("Toyota", "Camry")
print(car.info())

print()

# === MULTIPLE LEVELS OF INHERITANCE ===
print("=== MULTIPLE LEVELS OF INHERITANCE ===")

class Living:
    def __init__(self, name):
        self.name = name

class Animal(Living):
    def speak(self):
        return f"{self.name} makes sound"

class Dog(Animal):
    def speak(self):
        return f"{self.name} barks"

dog = Dog("Max")
print(dog.speak())

print()

# === PRACTICAL EXAMPLE: SHAPES ===
print("=== PRACTICAL: SHAPES ===")

import math

class Shape:
    def __init__(self, color):
        self.color = color
    
    def area(self):
        return "Area not defined"
    
    def info(self):
        return f"{self.__class__.__name__} ({self.color})"

class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius
    
    def area(self):
        return math.pi * (self.radius ** 2)

rect = Rectangle("red", 10, 5)
circle = Circle("blue", 3)

print(f"{rect.info()}: Area = {rect.area():.2f}")
print(f"{circle.info()}: Area = {circle.area():.2f}")

print()

# === ISINSTANCE() ===
print("=== ISINSTANCE() ===")

print(f"Is rect a Shape? {isinstance(rect, Shape)}")
print(f"Is rect a Rectangle? {isinstance(rect, Rectangle)}")
print(f"Is circle a Circle? {isinstance(circle, Circle)}")
print(f"Is circle a Shape? {isinstance(circle, Shape)}")

print()

# === POLYMORPHISM ===
print("=== POLYMORPHISM ===")

shapes = [rect, circle]

print("Area of all shapes:")
for shape in shapes:
    print(f"  {shape.info()}: {shape.area():.2f}")
