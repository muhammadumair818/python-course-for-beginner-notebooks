"""
===== PYTHON BASICS: OPERATORS =====

Operators are symbols that perform operations on variables and values.
Types:
1. Arithmetic Operators: +, -, *, /, //, %, **
2. Comparison Operators: ==, !=, <, >, <=, >=
3. Logical Operators: and, or, not
4. Assignment Operators: =, +=, -=, *=, etc.
"""

# === ARITHMETIC OPERATORS ===
print("=== ARITHMETIC OPERATORS ===")
a = 10
b = 3

# Addition
print(f"{a} + {b} = {a + b}")

# Subtraction
print(f"{a} - {b} = {a - b}")

# Multiplication
print(f"{a} * {b} = {a * b}")

# Division (returns float)
print(f"{a} / {b} = {a / b}")

# Floor Division (returns integer)
print(f"{a} // {b} = {a // b}")

# Modulo (remainder)
print(f"{a} % {b} = {a % b}")

# Exponentiation (power)
print(f"{a} ** {b} = {a ** b}")

print()

# === COMPARISON OPERATORS ===
print("=== COMPARISON OPERATORS ===")
x = 15
y = 8

# Equal to
print(f"{x} == {y}: {x == y}")

# Not equal to
print(f"{x} != {y}: {x != y}")

# Greater than
print(f"{x} > {y}: {x > y}")

# Less than
print(f"{x} < {y}: {x < y}")

# Greater than or equal
print(f"{x} >= {y}: {x >= y}")

# Less than or equal
print(f"{x} <= {y}: {x <= y}")

print()

# === LOGICAL OPERATORS ===
print("=== LOGICAL OPERATORS ===")

# AND operator (both must be True)
print(f"True and True: {True and True}")
print(f"True and False: {True and False}")
print(f"False and False: {False and False}")

print()

# OR operator (at least one must be True)
print(f"True or False: {True or False}")
print(f"False or False: {False or False}")
print(f"True or True: {True or True}")

print()

# NOT operator (reverses the value)
print(f"not True: {not True}")
print(f"not False: {not False}")

print()

# === PRACTICAL LOGICAL OPERATORS ===
print("=== Practical Logical Operators ===")
age = 25
has_license = True
has_insurance = True

# Can drive?
can_drive = age >= 18 and has_license and has_insurance
print(f"Can drive? {can_drive}")

# Is eligible for student discount?
is_student = False
is_low_income = True
eligible_for_discount = (is_student or is_low_income) and age < 65
print(f"Eligible for discount? {eligible_for_discount}")

print()

# === ASSIGNMENT OPERATORS ===
print("=== ASSIGNMENT OPERATORS ===")

# Simple assignment
count = 10
print(f"count = {count}")

# Add and assign (+=)
count += 5
print(f"count += 5: {count}")

# Subtract and assign (-=)
count -= 3
print(f"count -= 3: {count}")

# Multiply and assign (*=)
count *= 2
print(f"count *= 2: {count}")

# Divide and assign (/=)
count /= 4
print(f"count /= 4: {count}")

print()

# === OPERATOR PRECEDENCE ===
print("=== OPERATOR PRECEDENCE ===")
print("Python follows mathematical order of operations (PEMDAS)")
result1 = 10 + 5 * 2
result2 = (10 + 5) * 2

print(f"10 + 5 * 2 = {result1}")  # Multiplication first
print(f"(10 + 5) * 2 = {result2}")  # Parentheses first

print()

# === STRING OPERATORS ===
print("=== STRING OPERATORS ===")

# String concatenation with +
greeting = "Hello" + " " + "World"
print(f"Concatenation: {greeting}")

# String repetition with *
repeat_str = "ha" * 3
print(f"Repetition: {repeat_str}")

print()

# === PRACTICAL EXAMPLES ===
print("=== Practical Examples ===")

# Calculate discount price
original_price = 100
discount_percent = 20
discount_amount = original_price * (discount_percent / 100)
final_price = original_price - discount_amount
print(f"Original price: ${original_price}")
print(f"Discount: {discount_percent}%")
print(f"Final price: ${final_price}")

print()

# Check age group
age = 25
is_teenager = age >= 13 and age < 20
is_adult = age >= 18
is_senior = age >= 65

print(f"Age: {age}")
print(f"Is teenager: {is_teenager}")
print(f"Is adult: {is_adult}")
print(f"Is senior: {is_senior}")
