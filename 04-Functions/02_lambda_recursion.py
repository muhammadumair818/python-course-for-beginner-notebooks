"""
===== FUNCTIONS: LAMBDA AND RECURSION =====

Lambda functions are small anonymous functions.
Recursion is when a function calls itself.
"""

# === LAMBDA FUNCTIONS ===
print("=== LAMBDA FUNCTIONS ===")

# Regular function
def multiply_regular(x, y):
    return x * y

# Lambda function (one-liner)
multiply_lambda = lambda x, y: x * y

print(f"Regular: {multiply_regular(3, 4)}")
print(f"Lambda: {multiply_lambda(3, 4)}")

print()

# === LAMBDA WITH MAP ===
print("=== LAMBDA WITH MAP ===")

numbers = [1, 2, 3, 4, 5]

# Double each number
doubled = list(map(lambda x: x * 2, numbers))
print(f"Original: {numbers}")
print(f"Doubled: {doubled}")

# Square each number
squared = list(map(lambda x: x ** 2, numbers))
print(f"Squared: {squared}")

print()

# === LAMBDA WITH FILTER ===
print("=== LAMBDA WITH FILTER ===")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filter even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"All: {numbers}")
print(f"Evens: {evens}")

# Filter numbers > 5
greater_than_5 = list(filter(lambda x: x > 5, numbers))
print(f"Greater than 5: {greater_than_5}")

print()

# === LAMBDA WITH SORT ===
print("=== LAMBDA WITH SORT ===")

students = [
    ("Umair", 85),
    ("Fatima", 90),
    ("Hassan", 78)
]

# Sort by grade
sorted_students = sorted(students, key=lambda x: x[1])
print(f"Sorted by grade:")
for name, grade in sorted_students:
    print(f"  {name}: {grade}")

print()

# === RECURSION ===
print("=== RECURSION ===")

# Factorial using recursion
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(f"5! = {factorial(5)}")
print(f"3! = {factorial(3)}")

print()

# === RECURSION: COUNT DOWN ===
print("=== RECURSION: COUNT DOWN ===")

def countdown(n):
    if n == 0:
        return
    print(n, end=" ")
    countdown(n - 1)

countdown(5)
print()

print()

# === RECURSION: SUM OF NUMBERS ===
print("=== RECURSION: SUM OF NUMBERS ===")

def sum_up_to(n):
    if n == 0:
        return 0
    return n + sum_up_to(n - 1)

print(f"Sum 1+2+3+4+5 = {sum_up_to(5)}")
print(f"Sum 1+2+...+10 = {sum_up_to(10)}")

print()

# === RECURSION: FIBONACCI ===
print("=== RECURSION: FIBONACCI ===")

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print("Fibonacci sequence:")
for i in range(8):
    print(fibonacci(i), end=" ")
print()

print()

# === RECURSION: POWER ===
print("=== RECURSION: POWER ===")

def power(base, exp):
    if exp == 0:
        return 1
    return base * power(base, exp - 1)

print(f"2^3 = {power(2, 3)}")
print(f"3^4 = {power(3, 4)}")

print()

# === WHEN TO USE RECURSION ===
print("=== WHEN TO USE RECURSION ===")

# Good: Tree traversal, factorial, fibonacci
# Bad: Simple loops (use iteration instead)

# List recursion
def print_list(lst, index=0):
    if index == len(lst):
        return
    print(lst[index], end=" ")
    print_list(lst, index + 1)

print("Printing list recursively:")
print_list([10, 20, 30, 40, 50])
print()

print()

# === LAMBDA PRACTICAL EXAMPLES ===
print("=== LAMBDA PRACTICAL EXAMPLES ===")

# Sort dictionary by value
scores = {"Umair": 85, "Fatima": 90, "Hassan": 78}
sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
print("Scores (sorted):")
for name, score in sorted_scores:
    print(f"  {name}: {score}")

print()

# Transform and filter
numbers = [1, 2, 3, 4, 5, 6]
result = list(map(lambda x: x * 2, filter(lambda x: x > 2, numbers)))
print(f"Numbers > 2, doubled: {result}")
