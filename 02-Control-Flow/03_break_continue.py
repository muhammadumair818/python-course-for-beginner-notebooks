"""
===== CONTROL FLOW: BREAK AND CONTINUE =====

BREAK: Exit/stop the loop immediately
CONTINUE: Skip the rest of current iteration, move to next
"""

# === BREAK STATEMENT ===
print("=== BREAK STATEMENT ===")
print("Stop when we find 5:")

for num in range(1, 11):
    if num == 5:
        print(f"Found {num}! Stopping...")
        break
    print(num, end=" ")

print()
print()

# === BREAK IN WHILE LOOP ===
print("=== BREAK IN WHILE LOOP ===")

password = ""
attempts = 0

while attempts < 3:
    password = "secret"  # Simulating input
    if password == "secret":
        print("Password correct! Access granted.")
        break
    else:
        attempts += 1
        print(f"Wrong password. Attempt {attempts}/3")

if attempts == 3:
    print("Too many failed attempts. Access denied.")

print()

# === CONTINUE STATEMENT ===
print("=== CONTINUE STATEMENT ===")
print("Print only odd numbers:")

for num in range(1, 11):
    if num % 2 == 0:  # If even
        continue  # Skip to next iteration
    print(num, end=" ")

print()
print()

# === CONTINUE: SKIP INVALID ===
print("=== CONTINUE: Skip Invalid Data ===")

data = [10, -5, 20, 0, 15, -3, 25]

print("Positive numbers only:")
for value in data:
    if value <= 0:
        continue  # Skip non-positive
    print(value, end=" ")

print()
print()

# === SKIP UNWANTED ITEMS ===
print("=== SKIP UNWANTED ITEMS ===")

fruits = ["apple", "banana", "grape", "orange", "kiwi"]
unwanted = ["grape"]

print("Fruits without grapes:")
for fruit in fruits:
    if fruit in unwanted:
        continue
    print(fruit, end=" ")

print()
print()

# === BREAK AND CONTINUE TOGETHER ===
print("=== BREAK AND CONTINUE TOGETHER ===")

print("Process numbers 1-10 (skip 3 and 7, stop at 9):")

for num in range(1, 11):
    if num in [3, 7]:
        print(f"(Skip {num})", end=" ")
        continue
    if num == 9:
        print(f"{num}", end=" ")
        print("(Stopping)")
        break
    print(num, end=" ")

print()
print()

# === NESTED LOOPS WITH BREAK ===
print("=== NESTED LOOPS WITH BREAK ===")

print("Find 5 in 2D grid:")

grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

found = False
for row in range(len(grid)):
    for col in range(len(grid[row])):
        if grid[row][col] == 5:
            print(f"Found 5 at position ({row}, {col})")
            found = True
            break
    if found:
        break

print()

# === PRACTICAL EXAMPLE: SEARCH ===
print("=== PRACTICAL EXAMPLE: Search ===")

items = ["car", "bike", "truck", "plane", "bus"]
search_item = "truck"

print(f"Searching for '{search_item}'...")
for i, item in enumerate(items):
    if item == search_item:
        print(f"Found at index {i}!")
        break
else:
    print("Not found!")

print()

# === PRACTICAL EXAMPLE: VALIDATION ===
print("=== PRACTICAL EXAMPLE: Validate Email ===")

email = "user@example.com"
invalid_chars = ['!', '#', '$', '%']

print(f"Email: {email}")
print("Checking for invalid characters...")

is_valid = True
for char in email:
    if char in invalid_chars:
        print(f"Invalid character found: {char}")
        is_valid = False
        break

if is_valid:
    print("Email is valid!")

print()

# === PRACTICAL EXAMPLE: STOP ON ERROR ===
print("=== PRACTICAL EXAMPLE: Stop on Error ===")

numbers = [10, 20, 0, 30, 40]

print("Divide 100 by each number:")
for num in numbers:
    if num == 0:
        print("Cannot divide by zero! Stopping.")
        break
    result = 100 / num
    print(f"100 / {num} = {result}")

print()

# === FOR-ELSE WITH BREAK ===
print("=== FOR-ELSE WITH BREAK ===")

# The else block runs ONLY if loop completes without break

print("Search for 5:")
for num in [1, 2, 3, 4]:
    if num == 5:
        print("Found!")
        break
else:
    print("Not found (else block ran)")

print()

print("Search for 4:")
for num in [1, 2, 3, 4]:
    if num == 4:
        print("Found!")
        break
else:
    print("Not found (else block ran)")

print()

# === PRACTICAL EXAMPLE: PROCESS UNTIL CONDITION ===
print("=== PRACTICAL EXAMPLE: Process Until Condition ===")

print("Process items until we hit a special marker:")

items = ["apple", "banana", "cherry", "STOP", "date", "elderberry"]

for item in items:
    if item == "STOP":
        print("Stop marker found! Halting process.")
        break
    print(f"Processing: {item}")

print()

# === SKIP AND PROCESS ===
print("=== SKIP AND PROCESS ===")

print("Process items (skip negatives):")

transactions = [100, -50, 200, -30, 150, 0, -20]

for amount in transactions:
    if amount < 0:
        print(f"Skipping invalid amount: {amount}")
        continue
    if amount == 0:
        print("Zero balance detected!")
        break
    print(f"Processing transaction: ${amount}")
