"""
===== FUNCTIONS: BASICS =====

A function is a reusable block of code that performs a specific task.

Syntax:
def function_name(parameters):
    # Code block
    return result
"""

# === SIMPLE FUNCTION ===
print("=== SIMPLE FUNCTION ===")

def greet():
    print("Hello, World!")

greet()  # Call the function
greet()

print()

# === FUNCTION WITH PARAMETERS ===
print("=== FUNCTION WITH PARAMETERS ===")

def greet_person(name):
    print(f"Hello, {name}!")

greet_person("Umair")
greet_person("Fatima")
greet_person("Hassan")

print()

# === FUNCTION WITH MULTIPLE PARAMETERS ===
print("=== FUNCTION WITH MULTIPLE PARAMETERS ===")

def add(a, b):
    result = a + b
    return result

sum1 = add(10, 20)
sum2 = add(5, 3)

print(f"10 + 20 = {sum1}")
print(f"5 + 3 = {sum2}")

print()

# === RETURN VALUES ===
print("=== RETURN VALUES ===")

def multiply(x, y):
    return x * y

result = multiply(4, 5)
print(f"4 * 5 = {result}")

# Without return
def no_return():
    print("This function doesn't return anything")
    # Returns None implicitly

value = no_return()
print(f"Value: {value}")

print()

# === FUNCTION WITH DEFAULT PARAMETERS ===
print("=== DEFAULT PARAMETERS ===")

def greet_with_title(name, title="Mr."):
    print(f"Hello, {title} {name}!")

greet_with_title("Smith")  # Uses default title
greet_with_title("Khan", "Ms.")  # Custom title

print()

# === MULTIPLE RETURN VALUES ===
print("=== MULTIPLE RETURN VALUES ===")

def get_person_info():
    return "Umair", 25, "Engineer"

name, age, job = get_person_info()
print(f"Name: {name}, Age: {age}, Job: {job}")

# Return as tuple
result = get_person_info()
print(f"Result: {result}")

print()

# === KEYWORD ARGUMENTS ===
print("=== KEYWORD ARGUMENTS ===")

def create_profile(name, age, city):
    print(f"Name: {name}, Age: {age}, City: {city}")

# Positional arguments
create_profile("Umair", 25, "Karachi")

# Keyword arguments
create_profile(city="Lahore", name="Fatima", age=30)

print()

# === VARIABLE NUMBER OF ARGUMENTS (*args) ===
print("=== VARIABLE ARGUMENTS (*args) ===")

def sum_numbers(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print(f"sum_numbers(1, 2, 3) = {sum_numbers(1, 2, 3)}")
print(f"sum_numbers(10, 20) = {sum_numbers(10, 20)}")
print(f"sum_numbers(1, 2, 3, 4, 5) = {sum_numbers(1, 2, 3, 4, 5)}")

print()

# === VARIABLE KEYWORD ARGUMENTS (**kwargs) ===
print("=== VARIABLE KEYWORD ARGUMENTS (**kwargs) ===")

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"  {key}: {value}")

print("Person info:")
print_info(name="Umair", age=25, city="Karachi")

print("\nCar info:")
print_info(brand="Toyota", model="Camry", year=2022)

print()

# === PRACTICAL EXAMPLES ===
print("=== PRACTICAL EXAMPLES ===")

# Calculate rectangle area
def rectangle_area(length, width):
    return length * width

area = rectangle_area(10, 5)
print(f"Rectangle area (10 x 5): {area}")

# Convert temperature
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

print(f"0°C = {celsius_to_fahrenheit(0)}°F")
print(f"100°C = {celsius_to_fahrenheit(100)}°F")

# Check if number is even
def is_even(num):
    return num % 2 == 0

print(f"Is 10 even? {is_even(10)}")
print(f"Is 7 even? {is_even(7)}")

print()

# === DOCSTRINGS ===
print("=== DOCSTRINGS ===")

def divide(a, b):
    """
    Divide a by b.
    
    Args:
        a: Numerator
        b: Denominator
    
    Returns:
        Result of division
    """
    if b == 0:
        return "Cannot divide by zero"
    return a / b

print(divide.__doc__)
print(f"10 / 2 = {divide(10, 2)}")
