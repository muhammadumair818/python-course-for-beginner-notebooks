"""
===== DATA STRUCTURES: TUPLES =====

A tuple is an ordered collection of items.
- Immutable (cannot be changed after creation)
- Faster than lists
- Can be used as dictionary keys
"""

# === CREATING TUPLES ===
print("=== CREATING TUPLES ===")

# Empty tuple
empty = ()
print(f"Empty tuple: {empty}")

# Tuple with items
colors = ("red", "green", "blue")
print(f"Colors: {colors}")

# Tuple with single item (note the comma!)
single = (42,)
print(f"Single item tuple: {single}")

# Using tuple() constructor
numbers = tuple(range(1, 6))
print(f"Using tuple(): {numbers}")

print()

# === ACCESSING ITEMS ===
print("=== ACCESSING ITEMS ===")

colors = ("red", "green", "blue", "yellow")
print(f"Tuple: {colors}")
print(f"First: {colors[0]}")
print(f"Last: {colors[-1]}")

print()

# === SLICING ===
print("=== SLICING ===")

numbers = (1, 2, 3, 4, 5)
print(f"Tuple: {numbers}")
print(f"[1:3]: {numbers[1:3]}")
print(f"[:2]: {numbers[:2]}")
print(f"[2:]: {numbers[2:]}")

print()

# === IMMUTABILITY ===
print("=== IMMUTABILITY (Cannot Change) ===")

point = (10, 20)
print(f"Original: {point}")

# This would cause an error:
# point[0] = 15  # TypeError: 'tuple' object does not support item assignment

print("Tuples cannot be modified (immutable)")

print()

# === LENGTH, INDEX, COUNT ===
print("=== LENGTH, INDEX, COUNT ===")

numbers = (1, 2, 2, 3, 2, 4, 5)
print(f"Tuple: {numbers}")
print(f"Length: {len(numbers)}")
print(f"Index of 3: {numbers.index(3)}")
print(f"Count of 2: {numbers.count(2)}")

print()

# === LOOPING THROUGH TUPLES ===
print("=== LOOPING ===")

coordinates = [(0, 0), (1, 2), (3, 4)]

for x, y in coordinates:
    print(f"Point: ({x}, {y})")

print()

# === TUPLE PACKING & UNPACKING ===
print("=== TUPLE UNPACKING ===")

# Packing
info = ("Umair", 25, "Engineer")
print(f"Packed: {info}")

# Unpacking
name, age, job = info
print(f"Name: {name}, Age: {age}, Job: {job}")

# Swapping values
a, b = 1, 2
print(f"Before swap: a={a}, b={b}")
a, b = b, a
print(f"After swap: a={a}, b={b}")

print()

# === TUPLE OPERATIONS ===
print("=== TUPLE OPERATIONS ===")

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

# Combine
combined = tuple1 + tuple2
print(f"Combined: {combined}")

# Repeat
repeated = (1, 2) * 3
print(f"Repeated: {repeated}")

print()

# === WHEN TO USE TUPLES ===
print("=== WHEN TO USE TUPLES ===")

# 1. As dictionary keys
locations = {
    (0, 0): "origin",
    (1, 1): "diagonal",
    (5, 3): "point"
}
print(f"Locations: {locations}")

# 2. Returning multiple values from function
def get_person():
    return ("Umair", 25)

name, age = get_person()
print(f"Person: {name}, {age}")

# 3. Data that shouldn't change
rgb = (255, 128, 0)  # Orange
print(f"RGB color: {rgb}")

print()

# === PRACTICAL EXAMPLES ===
print("=== PRACTICAL EXAMPLES ===")

# Coordinates
points = [(0, 0), (1, 2), (3, 4), (5, 6)]
print(f"Points: {points}")

for x, y in points:
    distance = (x**2 + y**2) ** 0.5
    print(f"Point ({x}, {y}): distance = {distance:.2f}")

print()

# Nested tuples
student = ("Umair", (85, 90, 95))
name, scores = student
print(f"Student: {name}")
print(f"Scores: {scores}")
print(f"Average: {sum(scores) / len(scores):.2f}")
