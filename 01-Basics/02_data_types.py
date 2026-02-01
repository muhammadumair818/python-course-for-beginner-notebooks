"""
===== PYTHON BASICS: DATA TYPES =====

Python has several fundamental data types:
1. int - Integer (whole numbers): 5, -10, 0
2. float - Float (decimal numbers): 3.14, -2.5
3. str - String (text): "Hello", 'World'
4. bool - Boolean (True/False)
5. None - Represents absence of value
"""

# === INTEGERS ===
print("=== INTEGERS ===")
age = 25
score = -100
temperature = 0

print(f"age: {age} (type: {type(age)})")
print(f"score: {score}")
print(f"temperature: {temperature}")
print()

# === FLOATS ===
print("=== FLOATS ===")
price = 19.99
pi = 3.14159
weight = 72.5

print(f"price: {price} (type: {type(price)})")
print(f"pi: {pi}")
print(f"weight: {weight}")
print()

# === STRINGS ===
print("=== STRINGS ===")
# Strings can use single or double quotes
message1 = "Hello, World!"
message2 = 'Python is fun'
message3 = """This is a
multi-line
string"""

print(f"message1: {message1}")
print(f"message2: {message2}")
print(f"message3:\n{message3}")
print()

# String concatenation (joining strings)
first_name = "Usman"
last_name = "Khan"
full_name = first_name + " " + last_name
print(f"Full name: {full_name}")
print()

# === BOOLEANS ===
print("=== BOOLEANS ===")
is_adult = True
is_student = False
has_license = True

print(f"is_adult: {is_adult} (type: {type(is_adult)})")
print(f"is_student: {is_student}")
print(f"has_license: {has_license}")
print()

# === NONE TYPE ===
print("=== NONE TYPE ===")
empty_value = None
result = None

print(f"empty_value: {empty_value} (type: {type(empty_value)})")
print(f"result: {result}")
print()

# === TYPE CONVERSION ===
print("=== TYPE CONVERSION ===")

# Convert string to integer
string_number = "42"
int_number = int(string_number)
print(f"String '{string_number}' converted to int: {int_number}")

# Convert integer to string
number = 100
string_from_number = str(number)
print(f"Integer {number} converted to string: '{string_from_number}'")

# Convert to float
int_val = 10
float_val = float(int_val)
print(f"Integer {int_val} converted to float: {float_val}")

# Convert to boolean
print(f"int(0) as boolean: {bool(0)}")  # False
print(f"int(1) as boolean: {bool(1)}")  # True
print(f"Empty string as boolean: {bool('')}")  # False
print(f"Non-empty string as boolean: {bool('hello')}")  # True
print()

# === COMMON MISTAKES ===
print("=== Common Mistakes ===")

# Mistake 1: String vs Number
user_input = "123"
print(f"'123' + '456' = '{user_input + '456'}'")  # String concatenation
number = int(user_input)
print(f"123 + 456 = {number + 456}")  # Arithmetic

print()

# === PRACTICAL EXAMPLE ===
print("=== Practical Example: Store User Data ===")
username = "umair_wonder"
user_age = 28
user_balance = 150.75
is_premium = True
verification_date = None

print(f"Username: {username} ({type(username).__name__})")
print(f"Age: {user_age} ({type(user_age).__name__})")
print(f"Balance: ${user_balance} ({type(user_balance).__name__})")
print(f"Premium Member: {is_premium} ({type(is_premium).__name__})")
print(f"Verification Date: {verification_date} ({type(verification_date).__name__})")
