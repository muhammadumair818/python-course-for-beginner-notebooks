"""
===== DATA STRUCTURES: LISTS =====

A list is an ordered collection of items.
- Mutable (can be changed)
- Can contain different types
- Access by index (position)
"""

# === CREATING LISTS ===
print("=== CREATING LISTS ===")

# Empty list
empty_list = []
print(f"Empty list: {empty_list}")

# List with items
fruits = ["apple", "banana", "orange", "mango"]
print(f"Fruits: {fruits}")

# Mixed types
mixed = [1, "hello", 3.14, True, None]
print(f"Mixed types: {mixed}")

# Using list() constructor
numbers = list(range(1, 6))
print(f"Using list(): {numbers}")

print()

# === INDEXING (ACCESSING ITEMS) ===
print("=== INDEXING ===")

fruits = ["apple", "banana", "orange", "mango"]
print(f"List: {fruits}")
print(f"Index 0 (first): {fruits[0]}")
print(f"Index 1: {fruits[1]}")
print(f"Index -1 (last): {fruits[-1]}")
print(f"Index -2 (second last): {fruits[-2]}")

print()

# === SLICING ===
print("=== SLICING ===")

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"List: {numbers}")
print(f"[2:5]: {numbers[2:5]}")  # Index 2, 3, 4
print(f"[:3]: {numbers[:3]}")    # From start to 2
print(f"[6:]: {numbers[6:]}")    # From 6 to end
print(f"[::2]: {numbers[::2]}")  # Every 2nd
print(f"[::-1]: {numbers[::-1]}")  # Reversed

print()

# === LENGTH ===
print("=== LENGTH ===")

fruits = ["apple", "banana", "orange"]
print(f"Fruits: {fruits}")
print(f"Length: {len(fruits)}")

print()

# === MODIFYING LISTS ===
print("=== MODIFYING LISTS ===")

# Add item (append)
fruits = ["apple", "banana"]
print(f"Original: {fruits}")
fruits.append("orange")
print(f"After append: {fruits}")

# Insert at position
fruits.insert(1, "mango")
print(f"After insert(1, 'mango'): {fruits}")

# Remove item
fruits.remove("mango")
print(f"After remove('mango'): {fruits}")

# Pop (remove by index)
removed = fruits.pop()  # Removes last
print(f"Popped item: {removed}")
print(f"After pop(): {fruits}")

# Clear
numbers = [1, 2, 3, 4, 5]
print(f"Before clear: {numbers}")
numbers.clear()
print(f"After clear: {numbers}")

print()

# === CHANGING ITEMS ===
print("=== CHANGING ITEMS ===")

fruits = ["apple", "banana", "orange"]
print(f"Original: {fruits}")

fruits[0] = "mango"
print(f"After fruits[0] = 'mango': {fruits}")

fruits[1:3] = ["grape", "kiwi"]
print(f"After fruits[1:3] = ['grape', 'kiwi']: {fruits}")

print()

# === SEARCHING ===
print("=== SEARCHING ===")

fruits = ["apple", "banana", "orange", "banana"]

# Check if item exists
print(f"'apple' in fruits: {'apple' in fruits}")
print(f"'grape' in fruits: {'grape' in fruits}")

# Find index
index = fruits.index("banana")
print(f"Index of 'banana': {index}")

# Count occurrences
count = fruits.count("banana")
print(f"Count of 'banana': {count}")

print()

# === SORTING ===
print("=== SORTING ===")

numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"Original: {numbers}")

# Sort in place (changes original)
numbers.sort()
print(f"After sort(): {numbers}")

# Sort in reverse
numbers.sort(reverse=True)
print(f"Reverse sort: {numbers}")

# Sort strings
words = ["zebra", "apple", "mango"]
words.sort()
print(f"Sorted words: {words}")

print()

# === COPYING LISTS ===
print("=== COPYING LISTS ===")

original = [1, 2, 3]
copy_list = original.copy()
copy_list[0] = 99

print(f"Original: {original}")
print(f"Copy (modified): {copy_list}")

print()

# === LIST OPERATIONS ===
print("=== LIST OPERATIONS ===")

list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Combine lists
combined = list1 + list2
print(f"Combined: {combined}")

# Repeat
repeated = [1, 2] * 3
print(f"Repeated: {repeated}")

# Extend (add items from another list)
list1.extend(list2)
print(f"After extend: {list1}")

print()

# === LOOPING THROUGH LISTS ===
print("=== LOOPING THROUGH LISTS ===")

fruits = ["apple", "banana", "orange"]

print("For loop:")
for fruit in fruits:
    print(f"  {fruit}")

print("\nWith enumerate:")
for index, fruit in enumerate(fruits):
    print(f"  {index}: {fruit}")

print()

# === LIST COMPREHENSION ===
print("=== LIST COMPREHENSION ===")

numbers = [1, 2, 3, 4, 5]
squared = [x**2 for x in numbers]
print(f"Squared: {squared}")

evens = [x for x in numbers if x % 2 == 0]
print(f"Evens: {evens}")

print()

# === PRACTICAL EXAMPLES ===
print("=== PRACTICAL EXAMPLES ===")

# Grade list
grades = [85, 92, 78, 95, 88]
average = sum(grades) / len(grades)
highest = max(grades)
lowest = min(grades)

print(f"Grades: {grades}")
print(f"Average: {average:.2f}")
print(f"Highest: {highest}")
print(f"Lowest: {lowest}")

print()

# Student list
students = ["Umair", "Fatima", "Hassan"]
print(f"Students: {students}")
print(f"First student: {students[0]}")
print(f"Last student: {students[-1]}")
