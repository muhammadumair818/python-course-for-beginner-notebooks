"""
===== FILE HANDLING: EXCEPTION HANDLING =====
"""

# === TRY-EXCEPT ===
print("=== TRY-EXCEPT ===")

try:
    result = 10 / 2
    print(f"Result: {result}")
except ZeroDivisionError:
    print("Cannot divide by zero!")

print()

# === TRY-EXCEPT WITH FILE ===
print("=== FILE NOT FOUND EXCEPTION ===")

try:
    with open("nonexistent.txt", 'r') as file:
        content = file.read()
except FileNotFoundError:
    print("File not found!")

print()

# === MULTIPLE EXCEPT BLOCKS ===
print("=== MULTIPLE EXCEPT BLOCKS ===")

def process_number(value):
    try:
        num = int(value)
        result = 100 / num
        return result
    except ValueError:
        print(f"'{value}' is not a valid number")
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    except Exception as e:
        print(f"Unexpected error: {e}")

print(f"process_number('10'): {process_number('10')}")
print(f"process_number('abc'): {process_number('abc')}")
print(f"process_number('0'): {process_number('0')}")

print()

# === TRY-EXCEPT-ELSE ===
print("=== TRY-EXCEPT-ELSE ===")

try:
    num = int("25")
except ValueError:
    print("Invalid number")
else:
    print(f"Successfully converted: {num}")

print()

# === TRY-EXCEPT-FINALLY ===
print("=== TRY-EXCEPT-FINALLY ===")

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"File '{filename}' not found")
    finally:
        print("File operation complete")

read_file("nonexistent.txt")

print()

# === RAISE EXCEPTION ===
print("=== RAISE EXCEPTION ===")

def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age > 150:
        raise ValueError("Age is too high")
    return age

try:
    validate_age(25)
    print("Valid age")
except ValueError as e:
    print(f"Error: {e}")

print()

# === COMMON EXCEPTIONS ===
print("=== COMMON EXCEPTIONS ===")

# IndexError
try:
    lst = [1, 2, 3]
    print(lst[10])
except IndexError:
    print("Index out of range")

# KeyError
try:
    d = {"a": 1}
    print(d["b"])
except KeyError:
    print("Key not found")

# TypeError
try:
    result = "hello" + 5
except TypeError:
    print("Type error: cannot concatenate string and int")

print()

# === PRACTICAL EXAMPLE ===
print("=== PRACTICAL: SAFE INPUT ===")

def get_positive_number(prompt):
    while True:
        try:
            num = float(input(prompt))
            if num < 0:
                print("Please enter a positive number")
                continue
            return num
        except ValueError:
            print("Invalid input. Please enter a number.")

# Simulated input
number = 42
print(f"User input: {number}")
print(f"Processing: {number}")
