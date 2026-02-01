"""
===== FUNCTIONS: EXERCISES =====

Practice with functions, lambda, and recursion.
"""

print("=" * 50)
print("FUNCTIONS EXERCISES")
print("=" * 50)
print()

# ===== EXERCISE 1: Simple Function =====
print("EXERCISE 1: Calculate Circle Area")
print("-" * 40)

def circle_area(radius):
    return 3.14159 * (radius ** 2)

r = 5
area = circle_area(r)
print(f"Circle with radius {r}: Area = {area:.2f}")

print()

# ===== EXERCISE 2: Function with Multiple Parameters =====
print("EXERCISE 2: Calculate Total Price")
print("-" * 40)

def calculate_total(price, quantity, tax_rate=0.1):
    subtotal = price * quantity
    tax = subtotal * tax_rate
    return subtotal + tax

total = calculate_total(100, 3)
print(f"Price: $100, Quantity: 3")
print(f"Total (with 10% tax): ${total:.2f}")

total_custom = calculate_total(50, 2, 0.08)
print(f"Price: $50, Quantity: 2, Tax: 8%")
print(f"Total: ${total_custom:.2f}")

print()

# ===== EXERCISE 3: Return Multiple Values =====
print("EXERCISE 3: Get Min and Max")
print("-" * 40)

def min_max(numbers):
    return min(numbers), max(numbers)

nums = [5, 10, 3, 20, 8]
minimum, maximum = min_max(nums)
print(f"Numbers: {nums}")
print(f"Min: {minimum}, Max: {maximum}")

print()

# ===== EXERCISE 4: Validation Function =====
print("EXERCISE 4: Validate Age")
print("-" * 40)

def is_adult(age):
    return age >= 18

ages = [15, 25, 18, 12, 35]
for age in ages:
    status = "Adult" if is_adult(age) else "Minor"
    print(f"Age {age}: {status}")

print()

# ===== EXERCISE 5: *args Practice =====
print("EXERCISE 5: Average of Numbers")
print("-" * 40)

def average(*numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)

print(f"average(10, 20, 30) = {average(10, 20, 30):.2f}")
print(f"average(5, 15) = {average(5, 15):.2f}")
print(f"average(1, 2, 3, 4, 5) = {average(1, 2, 3, 4, 5):.2f}")

print()

# ===== EXERCISE 6: Lambda Function =====
print("EXERCISE 6: Lambda for Sorting")
print("-" * 40)

products = [
    ("Laptop", 1200),
    ("Mouse", 25),
    ("Keyboard", 100)
]

sorted_by_price = sorted(products, key=lambda x: x[1])
print("Products sorted by price:")
for name, price in sorted_by_price:
    print(f"  {name}: ${price}")

print()

# ===== EXERCISE 7: Map with Lambda =====
print("EXERCISE 7: Convert Temperatures")
print("-" * 40)

celsius = [0, 10, 20, 30, 100]
fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))

print("Celsius -> Fahrenheit:")
for c, f in zip(celsius, fahrenheit):
    print(f"  {c}°C = {f:.1f}°F")

print()

# ===== EXERCISE 8: Filter with Lambda =====
print("EXERCISE 8: Filter Expensive Products")
print("-" * 40)

products = [
    ("Apple", 1),
    ("Laptop", 1200),
    ("Mouse", 25),
    ("Monitor", 300),
    ("Pen", 2)
]

expensive = list(filter(lambda x: x[1] > 100, products))
print("Products over $100:")
for name, price in expensive:
    print(f"  {name}: ${price}")

print()

# ===== EXERCISE 9: Simple Recursion =====
print("EXERCISE 9: Sum 1 to N")
print("-" * 40)

def sum_to_n(n):
    if n == 0:
        return 0
    return n + sum_to_n(n - 1)

for n in [5, 10, 15]:
    print(f"Sum 1 to {n}: {sum_to_n(n)}")

print()

# ===== EXERCISE 10: Factorial =====
print("EXERCISE 10: Factorial")
print("-" * 40)

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

for n in [3, 5, 6]:
    print(f"{n}! = {factorial(n)}")

print()

print("=" * 50)
print("WELL DONE!")
print("=" * 50)
