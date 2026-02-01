"""
===== PYTHON BASICS: EXERCISES =====

Practice problems to solidify your understanding of Python basics.
Work through these exercises and try to solve them on your own!
"""

print("=" * 50)
print("BASIC PYTHON EXERCISES")
print("=" * 50)
print()

# ===== EXERCISE 1: Temperature Converter =====
print("EXERCISE 1: Temperature Converter")
print("-" * 40)
print("Convert Fahrenheit to Celsius")

# Formula: C = (F - 32) * 5/9
fahrenheit = 98.6
celsius = (fahrenheit - 32) * 5/9

print(f"Input: {fahrenheit}°F")
print(f"Output: {celsius:.2f}°C")
print()

# ===== EXERCISE 2: Personal Information =====
print("EXERCISE 2: Personal Information")
print("-" * 40)
print("Create a profile and display it nicely")

name = "Umair Khan"
age = 28
height = 5.6  # feet
weight = 130  # pounds
city = "San Francisco"
occupation = "Software Engineer"

print(f"{'Name:':<20} {name}")
print(f"{'Age:':<20} {age}")
print(f"{'Height:':<20} {height} ft")
print(f"{'Weight:':<20} {weight} lbs")
print(f"{'City:':<20} {city}")
print(f"{'Occupation:':<20} {occupation}")
print()

# ===== EXERCISE 3: Simple Calculator =====
print("EXERCISE 3: Simple Calculator")
print("-" * 40)
print("Perform arithmetic operations")

num1 = 15
num2 = 7

print(f"Number 1: {num1}")
print(f"Number 2: {num2}")
print()
print(f"Addition: {num1} + {num2} = {num1 + num2}")
print(f"Subtraction: {num1} - {num2} = {num1 - num2}")
print(f"Multiplication: {num1} * {num2} = {num1 * num2}")
print(f"Division: {num1} / {num2} = {num1 / num2:.2f}")
print(f"Floor Division: {num1} // {num2} = {num1 // num2}")
print(f"Modulo: {num1} % {num2} = {num1 % num2}")
print(f"Exponent: {num1} ** {num2} = {num1 ** num2}")
print()

# ===== EXERCISE 4: String Manipulation =====
print("EXERCISE 4: String Manipulation")
print("-" * 40)
print("Work with strings")

sentence = "Python is an amazing programming language"

print(f"Original: {sentence}")
print(f"Length: {len(sentence)} characters")
print(f"Uppercase: {sentence.upper()}")
print(f"Lowercase: {sentence.lower()}")
print(f"Capitalized: {sentence.capitalize()}")
print(f"Title case: {sentence.title()}")
print()

# Word operations
words = sentence.split()
print(f"Words: {words}")
print(f"Number of words: {len(words)}")
print(f"First word: {words[0]}")
print(f"Last word: {words[-1]}")
print()

# ===== EXERCISE 5: Replace and Search =====
print("EXERCISE 5: Replace and Search")
print("-" * 40)

text = "I love Python. Python is fun. I code in Python."
print(f"Original: {text}")

# Find
position = text.find("Python")
print(f"First 'Python' at position: {position}")

# Count
count = text.count("Python")
print(f"Count of 'Python': {count}")

# Replace
new_text = text.replace("Python", "JavaScript")
print(f"Replaced: {new_text}")
print()

# ===== EXERCISE 6: Data Type Conversion =====
print("EXERCISE 6: Data Type Conversion")
print("-" * 40)

# String to number
age_str = "25"
age_int = int(age_str)
print(f"'{age_str}' (string) → {age_int} (integer)")

price_str = "19.99"
price_float = float(price_str)
print(f"'{price_str}' (string) → {price_float} (float)")

# Number to string
number = 42
number_str = str(number)
print(f"{number} (integer) → '{number_str}' (string)")

# String concatenation vs number addition
str1 = "5"
str2 = "3"
print(f"\nString addition: '{str1}' + '{str2}' = '{str1 + str2}'")

num1 = int(str1)
num2 = int(str2)
print(f"Number addition: {num1} + {num2} = {num1 + num2}")
print()

# ===== EXERCISE 7: Logical Operations =====
print("EXERCISE 7: Logical Operations")
print("-" * 40)

age = 25
has_license = True
has_insurance = True

can_drive = age >= 18 and has_license and has_insurance
print(f"Age: {age}")
print(f"Has license: {has_license}")
print(f"Has insurance: {has_insurance}")
print(f"Can drive: {can_drive}")
print()

# Discount eligibility
is_student = True
is_senior = False
is_member = True

eligible = (is_student or is_senior) and is_member
print(f"Is student: {is_student}")
print(f"Is senior: {is_senior}")
print(f"Is member: {is_member}")
print(f"Eligible for discount: {eligible}")
print()

# ===== EXERCISE 8: Invoice Calculation =====
print("EXERCISE 8: Invoice Calculation")
print("-" * 40)

item1_name = "Laptop"
item1_price = 1200.00
item1_quantity = 1

item2_name = "Mouse"
item2_price = 25.50
item2_quantity = 2

item3_name = "USB Cable"
item3_price = 10.00
item3_quantity = 3

subtotal1 = item1_price * item1_quantity
subtotal2 = item2_price * item2_quantity
subtotal3 = item3_price * item3_quantity

subtotal = subtotal1 + subtotal2 + subtotal3
tax_rate = 0.08
tax = subtotal * tax_rate
total = subtotal + tax

print(f"{item1_name:<15} ${item1_price:>10.2f} x {item1_quantity:>2} = ${subtotal1:>10.2f}")
print(f"{item2_name:<15} ${item2_price:>10.2f} x {item2_quantity:>2} = ${subtotal2:>10.2f}")
print(f"{item3_name:<15} ${item3_price:>10.2f} x {item3_quantity:>2} = ${subtotal3:>10.2f}")
print("-" * 50)
print(f"{'Subtotal:':<30} ${subtotal:>10.2f}")
print(f"{'Tax (8%):':<30} ${tax:>10.2f}")
print(f"{'Total:':<30} ${total:>10.2f}")
print()

# ===== EXERCISE 9: String Slicing =====
print("EXERCISE 9: String Slicing")
print("-" * 40)

code = "Python3.11.2"
print(f"Full string: {code}")
print(f"First 6 chars: {code[0:6]}")
print(f"Last 5 chars: {code[-5:]}")
print(f"Reversed: {code[::-1]}")
print(f"Every 2nd char: {code[::2]}")
print()

# ===== EXERCISE 10: Age in Different Measurements =====
print("EXERCISE 10: Age in Different Measurements")
print("-" * 40)

age_years = 25

age_months = age_years * 12
age_weeks = age_years * 52
age_days = age_years * 365

print(f"Age: {age_years} years")
print(f"     {age_months} months")
print(f"     {age_weeks} weeks")
print(f"     {age_days} days")
print()

print("=" * 50)
print("CONTINUE PRACTICING!")
print("=" * 50)
