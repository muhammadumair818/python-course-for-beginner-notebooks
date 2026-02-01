"""
===== CONTROL FLOW: LIST COMPREHENSION =====

List comprehension is a concise way to create lists.
Syntax: [expression for item in iterable if condition]

It's more efficient and readable than writing loops.
"""

# === SIMPLE LIST COMPREHENSION ===
print("=== SIMPLE LIST COMPREHENSION ===")

# Traditional way with loop
numbers_loop = []
for i in range(1, 6):
    numbers_loop.append(i)
print(f"Using loop: {numbers_loop}")

# Using list comprehension
numbers_comp = [i for i in range(1, 6)]
print(f"Using comprehension: {numbers_comp}")

print()

# === TRANSFORMATION ===
print("=== TRANSFORMATION ===")

# Double each number
numbers = [1, 2, 3, 4, 5]
doubled = [num * 2 for num in numbers]
print(f"Original: {numbers}")
print(f"Doubled: {doubled}")

print()

# Square each number
squared = [num ** 2 for num in numbers]
print(f"Squared: {squared}")

print()

# === FILTERING ===
print("=== FILTERING (WITH CONDITION) ===")

# Get only even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [num for num in numbers if num % 2 == 0]
print(f"Original: {numbers}")
print(f"Even only: {evens}")

print()

# Get numbers greater than 5
greater_than_5 = [num for num in numbers if num > 5]
print(f"Greater than 5: {greater_than_5}")

print()

# === TRANSFORMATION WITH FILTERING ===
print("=== TRANSFORMATION WITH FILTERING ===")

# Double only even numbers
doubled_evens = [num * 2 for num in numbers if num % 2 == 0]
print(f"Numbers: {numbers}")
print(f"Doubled evens: {doubled_evens}")

print()

# === STRING OPERATIONS ===
print("=== STRING OPERATIONS ===")

# Convert to uppercase
words = ["hello", "world", "python"]
uppercase = [word.upper() for word in words]
print(f"Original: {words}")
print(f"Uppercase: {uppercase}")

print()

# Get length of each word
lengths = [len(word) for word in words]
print(f"Word lengths: {lengths}")

print()

# === RANGE WITH COMPREHENSION ===
print("=== RANGE WITH COMPREHENSION ===")

# Multiples of 3
multiples_of_3 = [i for i in range(1, 21) if i % 3 == 0]
print(f"Multiples of 3 (1-20): {multiples_of_3}")

print()

# Even numbers from 1 to 20
evens = [i for i in range(1, 21) if i % 2 == 0]
print(f"Even numbers (1-20): {evens}")

print()

# === NESTED LIST COMPREHENSION ===
print("=== NESTED LIST COMPREHENSION ===")

# 2x3 multiplication table (flattened)
mult_table = [i * j for i in range(1, 3) for j in range(1, 4)]
print(f"Multiplication table (flattened): {mult_table}")

# Create 2D grid
grid = [[i + j for j in range(3)] for i in range(3)]
print(f"2D Grid:")
for row in grid:
    print(row)

print()

# === DICTIONARY FROM LIST ===
print("=== CREATE DICTIONARY FROM LIST ===")

numbers = [1, 2, 3, 4, 5]

# Create dict with number as key and square as value
squares_dict = {num: num**2 for num in numbers}
print(f"Squares dict: {squares_dict}")

print()

# === CONVERT STRING TO LIST OF CHARACTERS ===
print("=== STRING TO CHARACTER LIST ===")

word = "Python"
chars = [char for char in word]
print(f"Word: {word}")
print(f"Characters: {chars}")

print()

# Uppercase characters only
uppercase_chars = [char for char in word if char.isupper()]
print(f"Uppercase: {uppercase_chars}")

print()

# === COMMON OPERATIONS ===
print("=== COMMON OPERATIONS ===")

# Remove duplicates (convert to set, then list)
numbers_with_duplicates = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
unique = list(set(numbers_with_duplicates))
print(f"With duplicates: {numbers_with_duplicates}")
print(f"Unique (using set): {sorted(unique)}")

# Cleaner with list comprehension trick
numbers = [1, 2, 3, 4, 5]
incremented = [x + 1 for x in numbers]
print(f"\nOriginal: {numbers}")
print(f"Incremented: {incremented}")

print()

# === PRACTICAL EXAMPLES ===
print("=== PRACTICAL EXAMPLES ===")

# Extract emails
users = [
    {"name": "Umair", "email": "umair@example.com"},
    {"name": "Fatima", "email": "fatima@example.com"},
    {"name": "Hassan", "email": "hassan@example.com"}
]

emails = [user["email"] for user in users]
print(f"Emails: {emails}")

print()

# Get names in uppercase
names = ["umair", "fatima", "hassan"]
uppercase_names = [name.upper() for name in names]
print(f"Names uppercase: {uppercase_names}")

print()

# Convert prices to integers (remove $ and convert)
prices_str = ["$10", "$20", "$30"]
prices = [int(price[1:]) for price in prices_str]
print(f"Price strings: {prices_str}")
print(f"Price integers: {prices}")

print()

# === PERFORMANCE COMPARISON ===
print("=== PERFORMANCE COMPARISON ===")

# List comprehension is usually faster and more readable
large_list = [i for i in range(100) if i % 2 == 0]
print(f"First 10 even numbers: {large_list[:10]}")
print(f"Total count: {len(large_list)}")

print()

# === CONDITIONAL EXPRESSION IN LIST ===
print("=== CONDITIONAL EXPRESSION IN LIST ===")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Multiply by 2 if even, otherwise multiply by 3
result = [num * 2 if num % 2 == 0 else num * 3 for num in numbers]
print(f"Original: {numbers}")
print(f"Transformed: {result}")
