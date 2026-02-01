"""
===== CONTROL FLOW: EXERCISES =====

Practice problems to solidify your understanding of control flow.
"""

print("=" * 50)
print("CONTROL FLOW EXERCISES")
print("=" * 50)
print()

# ===== EXERCISE 1: Simple Calculator =====
print("EXERCISE 1: Simple Calculator")
print("-" * 40)

num1 = 20
num2 = 5
operation = "+"

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    result = num1 / num2
elif operation == "%":
    result = num1 % num2
else:
    result = "Invalid operation"

print(f"{num1} {operation} {num2} = {result}")
print()

# ===== EXERCISE 2: Grades =====
print("EXERCISE 2: Grade Assignment")
print("-" * 40)

score = 88

if score >= 90:
    grade = "A"
    feedback = "Excellent!"
elif score >= 80:
    grade = "B"
    feedback = "Good job!"
elif score >= 70:
    grade = "C"
    feedback = "Satisfactory"
elif score >= 60:
    grade = "D"
    feedback = "Passing"
else:
    grade = "F"
    feedback = "Failed"

print(f"Score: {score}")
print(f"Grade: {grade}")
print(f"Feedback: {feedback}")
print()

# ===== EXERCISE 3: Number Range Check =====
print("EXERCISE 3: Number in Range")
print("-" * 40)

number = 42

if 1 <= number <= 10:
    range_type = "1-10"
elif 11 <= number <= 20:
    range_type = "11-20"
elif 21 <= number <= 30:
    range_type = "21-30"
elif 31 <= number <= 50:
    range_type = "31-50"
else:
    range_type = "Above 50"

print(f"Number: {number}")
print(f"Range: {range_type}")
print()

# ===== EXERCISE 4: Number Classification =====
print("EXERCISE 4: Number Classification")
print("-" * 40)

nums = [15, 28, 33, 44, 50]

print("Classifying numbers:")
for num in nums:
    if num % 2 == 0:
        parity = "Even"
    else:
        parity = "Odd"
    
    if num < 20:
        size = "Small"
    elif num < 40:
        size = "Medium"
    else:
        size = "Large"
    
    print(f"{num}: {parity}, {size}")

print()

# ===== EXERCISE 5: Sum with Loop =====
print("EXERCISE 5: Sum List Elements")
print("-" * 40)

numbers = [10, 20, 30, 40, 50]
total = 0

for num in numbers:
    total += num

print(f"Numbers: {numbers}")
print(f"Sum: {total}")
print(f"Average: {total / len(numbers):.2f}")
print()

# ===== EXERCISE 6: Count Elements =====
print("EXERCISE 6: Count Elements")
print("-" * 40)

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

evens = 0
odds = 0

for num in data:
    if num % 2 == 0:
        evens += 1
    else:
        odds += 1

print(f"Data: {data}")
print(f"Even count: {evens}")
print(f"Odd count: {odds}")
print()

# ===== EXERCISE 7: Search in List =====
print("EXERCISE 7: Search in List")
print("-" * 40)

fruits = ["apple", "banana", "orange", "mango", "grape"]
search = "mango"

found = False
for fruit in fruits:
    if fruit == search:
        found = True
        break

if found:
    print(f"'{search}' found in list!")
else:
    print(f"'{search}' not found!")

print()

# ===== EXERCISE 8: Filter List =====
print("EXERCISE 8: Filter Even Numbers")
print("-" * 40)

numbers = list(range(1, 21))

# Using loop
evens = []
for num in numbers:
    if num % 2 == 0:
        evens.append(num)

print(f"All numbers: {numbers}")
print(f"Even numbers: {evens}")

# Using list comprehension
evens_comp = [num for num in numbers if num % 2 == 0]
print(f"Even (comprehension): {evens_comp}")

print()

# ===== EXERCISE 9: Transform List =====
print("EXERCISE 9: Double All Numbers")
print("-" * 40)

numbers = [1, 2, 3, 4, 5]

# Using loop
doubled = []
for num in numbers:
    doubled.append(num * 2)

print(f"Original: {numbers}")
print(f"Doubled: {doubled}")

# Using list comprehension
doubled_comp = [num * 2 for num in numbers]
print(f"Doubled (comprehension): {doubled_comp}")

print()

# ===== EXERCISE 10: Multiplication Table =====
print("EXERCISE 10: 7x Multiplication Table")
print("-" * 40)

multiplier = 7

for i in range(1, 11):
    result = multiplier * i
    print(f"{multiplier} × {i:2d} = {result:3d}")

print()

# ===== EXERCISE 11: Pattern =====
print("EXERCISE 11: Star Pattern")
print("-" * 40)

rows = 5
print("Increasing pattern:")
for i in range(1, rows + 1):
    print("*" * i)

print()

print("Decreasing pattern:")
for i in range(rows, 0, -1):
    print("*" * i)

print()

# ===== EXERCISE 12: Nested Loop =====
print("EXERCISE 12: 3x3 Times Table")
print("-" * 40)

for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i*j:2d}", end=" ")
    print()

print()

# ===== EXERCISE 13: Skip and Process =====
print("EXERCISE 13: Skip Negatives")
print("-" * 40)

data = [5, -3, 8, -1, 10, -2, 7]

print("Processing positive numbers only:")
for value in data:
    if value < 0:
        continue
    print(f"Processing: {value}")

print()

# ===== EXERCISE 14: Stop Condition =====
print("EXERCISE 14: Find Target Number")
print("-" * 40)

numbers = [2, 4, 6, 8, 10, 12, 14]
target = 10

print(f"Searching for {target} in {numbers}")
for num in numbers:
    if num == target:
        print(f"Found {target}!")
        break
    print(f"Checking {num}...")

print()

# ===== EXERCISE 15: List Comprehension Practice =====
print("EXERCISE 15: List Comprehension Practice")
print("-" * 40)

# Numbers from 1-10 squared
squares = [i**2 for i in range(1, 11)]
print(f"Squares of 1-10: {squares}")

# Numbers from 1-20 divisible by 3
divisible_3 = [i for i in range(1, 21) if i % 3 == 0]
print(f"Divisible by 3 (1-20): {divisible_3}")

# Length of each word
words = ["Python", "is", "awesome"]
lengths = [len(word) for word in words]
print(f"Words: {words}")
print(f"Lengths: {lengths}")

print()
print("=" * 50)
print("GREAT JOB! CONTINUE PRACTICING!")
print("=" * 50)
