"""
===== CONTROL FLOW: IF/ELIF/ELSE STATEMENTS =====

Conditional statements allow you to execute code based on conditions.
If a condition is True, the code runs. If False, it doesn't.

Structure:
if condition:
    # Code runs if condition is True
elif condition:
    # Code runs if previous conditions were False and this is True
else:
    # Code runs if all conditions were False
"""

# === SIMPLE IF STATEMENT ===
print("=== SIMPLE IF STATEMENT ===")

age = 20

if age >= 18:
    print("You are an adult")
    print("You can vote")

print()

# === IF-ELSE STATEMENT ===
print("=== IF-ELSE STATEMENT ===")

age = 15

if age >= 18:
    print("You can vote")
else:
    print("You are too young to vote")

print()

# === IF-ELIF-ELSE STATEMENT ===
print("=== IF-ELIF-ELSE STATEMENT ===")

score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Score: {score}")
print(f"Grade: {grade}")

print()

# === NESTED IF STATEMENTS ===
print("=== NESTED IF STATEMENTS ===")

age = 25
has_license = True
has_insurance = True

if age >= 18:
    print("Age requirement met")
    if has_license:
        print("License requirement met")
        if has_insurance:
            print("You can drive!")
        else:
            print("You need insurance")
    else:
        print("You need a license")
else:
    print("Too young to drive")

print()

# === MULTIPLE CONDITIONS WITH LOGICAL OPERATORS ===
print("=== MULTIPLE CONDITIONS ===")

# Using AND
age = 25
has_license = True

if age >= 18 and has_license:
    print("You can drive (using AND)")

print()

# Using OR
day = "Saturday"

if day == "Saturday" or day == "Sunday":
    print("It's the weekend!")

print()

# Using NOT
is_raining = False

if not is_raining:
    print("Go outside!")

print()

# === PRACTICAL EXAMPLE: TEMPERATURE CHECK ===
print("=== PRACTICAL EXAMPLE: Temperature =====")

temperature = 75

if temperature < 32:
    status = "Freezing"
elif temperature < 50:
    status = "Cold"
elif temperature < 70:
    status = "Cool"
elif temperature < 85:
    status = "Warm"
else:
    status = "Hot"

print(f"Temperature: {temperature}°F")
print(f"Status: {status}")

print()

# === PRACTICAL EXAMPLE: DISCOUNT CALCULATION ===
print("=== PRACTICAL EXAMPLE: Discount Calculation ===")

purchase_amount = 150
customer_type = "VIP"

if customer_type == "VIP":
    discount = 0.20  # 20% discount
elif customer_type == "Regular":
    discount = 0.10  # 10% discount
else:
    discount = 0.0  # No discount

discount_amount = purchase_amount * discount
final_price = purchase_amount - discount_amount

print(f"Purchase amount: ${purchase_amount}")
print(f"Customer type: {customer_type}")
print(f"Discount: {discount * 100}%")
print(f"Discount amount: ${discount_amount}")
print(f"Final price: ${final_price}")

print()

# === PRACTICAL EXAMPLE: GRADE FEEDBACK ===
print("=== PRACTICAL EXAMPLE: Grade Feedback ===")

score = 78

if score >= 90:
    print("Excellent work! Keep it up!")
elif score >= 80:
    print("Good job! You're doing well.")
elif score >= 70:
    print("You passed. Could be better though.")
elif score >= 60:
    print("You barely passed. Study harder!")
else:
    print("Failed. See your instructor.")

print()

# === TERNARY OPERATOR (Single-line IF-ELSE) ===
print("=== TERNARY OPERATOR ===")

age = 25
status = "Adult" if age >= 18 else "Minor"
print(f"Age: {age} -> Status: {status}")

age = 15
status = "Adult" if age >= 18 else "Minor"
print(f"Age: {age} -> Status: {status}")

print()

# === COMPARING DIFFERENT DATA TYPES ===
print("=== COMPARING VALUES ===")

# String comparison
name = "Umair"

if name == "Umair":
    print("Name is Umair")

if name != "Fatima":
    print("Name is not Bob")

if name.lower() == "umair":
    print("Name is umair (case-insensitive)")

print()

# Numeric comparison
value = 50

if 0 < value < 100:
    print(f"{value} is between 0 and 100")

print()

# === TRUTHY AND FALSY VALUES ===
print("=== TRUTHY AND FALSY VALUES ===")

# Falsy values: 0, "", [], {}, None, False
# Truthy values: Everything else

if 0:
    print("0 is truthy")
else:
    print("0 is falsy")

if "":
    print("Empty string is truthy")
else:
    print("Empty string is falsy")

if []:
    print("Empty list is truthy")
else:
    print("Empty list is falsy")

if "Hello":
    print("Non-empty string is truthy")

print()

# === CHECKING MULTIPLE VALUES ===
print("=== CHECKING MULTIPLE VALUES ===")

user_role = "admin"

if user_role in ["admin", "moderator"]:
    print("You have special privileges")
else:
    print("Regular user")

print()

# === PRACTICE ===
print("=== PRACTICE: Age Categories ===")

age = 35

if age < 13:
    category = "Child"
elif age < 20:
    category = "Teenager"
elif age < 65:
    category = "Adult"
else:
    category = "Senior"

print(f"Age {age}: {category}")
