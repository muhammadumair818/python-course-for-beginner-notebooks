"""
===== PYTHON BASICS: INPUT/OUTPUT =====

Input: Getting data from the user using input()
Output: Displaying data to the user using print()

Tips:
- input() always returns a string
- Use int() or float() to convert user input to numbers
- Use f-strings or .format() for formatted output
"""

# === BASIC OUTPUT WITH PRINT ===
print("=== BASIC OUTPUT WITH PRINT ===")
print("Hello, World!")
print("Python is awesome!")
print("Line 1")
print("Line 2")
print("Line 3")
print()

# === MULTIPLE VALUES IN PRINT ===
print("=== MULTIPLE VALUES IN PRINT ===")
name = "Umair"
age = 25
city = "Karachi"

print(name, age, city)  # Separated by spaces
print(name, age, city, sep=", ")  # Custom separator
print("Name:", name, "Age:", age, "City:", city)
print()

# === F-STRINGS (Modern Python) ===
print("=== F-STRINGS (Formatted Strings) ===")
name = "Fatima"
age = 30
score = 95.5

print(f"My name is {name}")
print(f"I am {age} years old")
print(f"My score is {score}")
print(f"Name: {name}, Age: {age}, Score: {score}")

# F-string with expressions
print(f"Next year I will be {age + 1}")
print(f"My score * 2 = {score * 2}")

print()

# === .format() METHOD ===
print("=== .format() METHOD ===")
print("Hello, {}!".format(name))
print("{} is {} years old".format(name, age))
print("Name: {}, Age: {}, Score: {}".format(name, age, score))

# With positions
print("{0} loves {1}".format("Umair", "Python"))
print("{1} is loved by {0}".format("Umair", "Python"))

print()

# === BASIC INPUT ===
print("=== BASIC INPUT ===")
print("Example: input() always returns a STRING")

# Example input (user would type their answer)
# user_input = input("Enter your name: ")
# print(f"Hello, {user_input}!")

# For demonstration, we'll show what happens:
name = "Usman"  # Pretend user entered this
print(f"User entered: {name} (type: {type(name)})")

print()

# === CONVERTING INPUT TO NUMBERS ===
print("=== CONVERTING INPUT TO NUMBERS ===")

# When user enters "25", it's a string "25"
age_str = "25"  # Simulating user input
print(f"Input received: '{age_str}' (type: {type(age_str)})")

# Convert to integer
age_int = int(age_str)
print(f"Converted to int: {age_int} (type: {type(age_int)})")

# Convert to float
age_float = float(age_str)
print(f"Converted to float: {age_float} (type: {type(age_float)})")

print()

# === PRACTICAL INPUT/OUTPUT EXAMPLE ===
print("=== PRACTICAL EXAMPLE: Calculator ===")
print("(This demonstrates the flow)\n")

# Simulate user input
num1_str = "10"
num2_str = "5"

print(f"Enter first number: {num1_str}")
print(f"Enter second number: {num2_str}")

# Convert to numbers
num1 = float(num1_str)
num2 = float(num2_str)

# Calculate
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2

# Display results
print("\n--- Results ---")
print(f"{num1} + {num2} = {addition}")
print(f"{num1} - {num2} = {subtraction}")
print(f"{num1} * {num2} = {multiplication}")
print(f"{num1} / {num2} = {division}")

print()

# === FORMATTING OUTPUT ===
print("=== FORMATTING OUTPUT ===")

price = 19.99
quantity = 3
total = price * quantity

# Basic output
print(f"Price: {price}")

# Rounded to 2 decimal places
print(f"Price: {price:.2f}")

# Right-aligned with width 10
print(f"Price: {price:>10}")

# Show percentage
percentage = 0.85
print(f"Completion: {percentage:.1%}")

print()

# === SKIP NEWLINES ===
print("=== SKIP NEWLINES ===")
print("Part 1", end="")  # Don't add newline
print(" Part 2", end="")
print(" Part 3")

print()
print()

# === MULTIPLE LINES WITH END PARAMETER ===
print("=== CUSTOM SEPARATOR ===")
print("Apple", "Banana", "Cherry", sep=" | ")
print(1, 2, 3, 4, 5, sep="-")

print()

# === ESCAPE SEQUENCES ===
print("=== ESCAPE SEQUENCES ===")
print("Line 1\nLine 2\nLine 3")  # \n = newline
print("Tab\tSeparated\tValues")  # \t = tab
print("This is a \"quote\"")  # \" = quote
print("Backslash: \\")  # \\ = backslash

print()

# === SUMMARY ===
print("=== SUMMARY ===")
print("1. print() displays output")
print("2. input() gets user input (as string)")
print("3. Convert with int() or float()")
print("4. Use f-strings for easy formatting")
print("5. Remember: user input is always a string!")
