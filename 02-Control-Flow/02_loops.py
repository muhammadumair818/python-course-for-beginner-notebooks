"""
===== CONTROL FLOW: FOR AND WHILE LOOPS =====

Loops allow you to repeat code multiple times.

FOR loop: Use when you know how many times to repeat
WHILE loop: Use when you don't know how many times (repeat until condition is False)
"""

# === SIMPLE FOR LOOP ===
print("=== SIMPLE FOR LOOP ===")

# Loop through range of numbers
for i in range(5):
    print(f"Iteration {i}")

print()

# === FOR LOOP WITH RANGE ===
print("=== FOR LOOP WITH RANGE ===")

# range(start, stop, step)
print("range(0, 5):")
for num in range(0, 5):
    print(num, end=" ")
print()

print("\nrange(1, 6):")
for num in range(1, 6):
    print(num, end=" ")
print()

print("\nrange(0, 10, 2):  # Every 2nd number")
for num in range(0, 10, 2):
    print(num, end=" ")
print()

print("\nrange(10, 0, -1):  # Countdown")
for num in range(10, 0, -1):
    print(num, end=" ")
print()

print()

# === FOR LOOP WITH LIST ===
print("=== FOR LOOP WITH LIST ===")

fruits = ["apple", "banana", "orange", "mango"]

for fruit in fruits:
    print(f"I like {fruit}")

print()

# === FOR LOOP WITH ENUMERATE ===
print("=== FOR LOOP WITH ENUMERATE (Get Index and Value) ===")

fruits = ["apple", "banana", "orange"]

for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")

print()

# === SUM AND TOTAL ===
print("=== SUM AND TOTAL ===")

numbers = [10, 20, 30, 40, 50]
total = 0

for num in numbers:
    total += num

print(f"Numbers: {numbers}")
print(f"Total: {total}")
print(f"Average: {total / len(numbers)}")

print()

# === FOR LOOP WITH MULTIPLICATION TABLE ===
print("=== MULTIPLICATION TABLE ===")

number = 7

for i in range(1, 11):
    print(f"{number} × {i} = {number * i}")

print()

# === WHILE LOOP ===
print("=== WHILE LOOP ===")

print("Count down from 5:")
count = 5
while count > 0:
    print(count, end=" ")
    count -= 1
print("Blastoff!")

print()

# === WHILE LOOP: UNKNOWN ITERATIONS ===
print("=== WHILE LOOP: Guess the Number ===")

target = 7
guess = 0

while guess != target:
    guess += 1
    print(f"Guess {guess}...", end=" ")
    if guess < target:
        print("Too low")
    elif guess > target:
        print("Too high")

print(f"Correct! The number is {target}")

print()

# === WHILE LOOP: USER INPUT ===
print("=== WHILE LOOP: Sum Until Quit ===")
print("(Simulated with list)")

values = [10, 20, 30, 0]  # 0 means quit
total = 0
index = 0

while index < len(values):
    value = values[index]
    if value == 0:
        break  # Exit the loop
    total += value
    print(f"Added {value}, total: {total}")
    index += 1

print(f"Final total: {total}")

print()

# === NESTED LOOPS ===
print("=== NESTED LOOPS (Loop within a Loop) ===")

print("Times table:")
for row in range(1, 4):
    for col in range(1, 4):
        print(f"{row}×{col}={row*col}", end=" | ")
    print()

print()

# === PATTERN WITH NESTED LOOPS ===
print("=== PATTERN WITH NESTED LOOPS ===")

rows = 5
for i in range(1, rows + 1):
    for j in range(i):
        print("*", end="")
    print()

print()

# === BREAK STATEMENT ===
print("=== BREAK STATEMENT (Exit Loop) ===")

for i in range(10):
    if i == 5:
        print(f"Found 5, breaking...")
        break
    print(i, end=" ")

print()
print()

# === CONTINUE STATEMENT ===
print("=== CONTINUE STATEMENT (Skip to Next) ===")

print("Numbers without even numbers:")
for i in range(1, 11):
    if i % 2 == 0:  # If even
        continue  # Skip to next iteration
    print(i, end=" ")

print()
print()

# === FOR-ELSE LOOP ===
print("=== FOR-ELSE (Run When Loop Completes) ===")

print("Searching for 5:")
for num in [1, 2, 3, 4]:
    if num == 5:
        print("Found!")
        break
else:
    print("5 not found in the list")

print()

print("Searching for 4:")
for num in [1, 2, 3, 4]:
    if num == 4:
        print("Found!")
        break
else:
    print("4 not found in the list")

print()

# === WHILE-ELSE LOOP ===
print("=== WHILE-ELSE ===")

count = 0
while count < 3:
    print(f"Count: {count}")
    count += 1
else:
    print("Loop completed!")

print()

# === PRACTICAL EXAMPLE: CALCULATE FACTORIAL ===
print("=== PRACTICAL EXAMPLE: Factorial ===")

number = 5
factorial = 1

for i in range(1, number + 1):
    factorial *= i

print(f"{number}! = {factorial}")

print()

# === PRACTICAL EXAMPLE: GENERATE FIBONACCI ===
print("=== PRACTICAL EXAMPLE: Fibonacci Sequence ===")

count = 8
a, b = 0, 1

print(f"First {count} Fibonacci numbers:")
for _ in range(count):
    print(a, end=" ")
    a, b = b, a + b

print()
print()

# === PRACTICAL EXAMPLE: FIND PRIME NUMBERS ===
print("=== PRACTICAL EXAMPLE: Prime Numbers ===")

print("Prime numbers from 1 to 20:")
for num in range(1, 21):
    is_prime = True
    for divisor in range(2, num):
        if num % divisor == 0:
            is_prime = False
            break
    if is_prime and num > 1:
        print(num, end=" ")

print()
