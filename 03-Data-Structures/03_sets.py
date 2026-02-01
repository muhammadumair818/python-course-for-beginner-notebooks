"""
===== DATA STRUCTURES: SETS =====

A set is an unordered collection of unique items.
- No duplicates
- Unordered (no indexing)
- Mutable (can add/remove items)
"""

# === CREATING SETS ===
print("=== CREATING SETS ===")

# Using curly braces
numbers = {1, 2, 3, 4, 5}
print(f"Numbers: {numbers}")

# With duplicates (automatically removes them)
colors = {"red", "blue", "red", "green"}
print(f"Colors: {colors}")

# Empty set (not {} - that's a dict!)
empty = set()
print(f"Empty set: {empty}")

# Using set() constructor
from_list = set([1, 2, 2, 3, 3, 3])
print(f"From list: {from_list}")

print()

# === LENGTH AND MEMBERSHIP ===
print("=== LENGTH AND MEMBERSHIP ===")

fruits = {"apple", "banana", "orange"}
print(f"Fruits: {fruits}")
print(f"Length: {len(fruits)}")
print(f"'apple' in fruits: {'apple' in fruits}")
print(f"'grape' in fruits: {'grape' in fruits}")

print()

# === ADDING AND REMOVING ===
print("=== ADDING AND REMOVING ===")

colors = {"red", "blue"}
print(f"Original: {colors}")

# Add single item
colors.add("green")
print(f"After add: {colors}")

# Try to add duplicate (no error, just ignored)
colors.add("red")
print(f"After add duplicate: {colors}")

# Remove (error if not found)
colors.remove("blue")
print(f"After remove: {colors}")

# Discard (no error if not found)
colors.discard("yellow")
print(f"After discard: {colors}")

# Pop (remove random item)
colors = {"red", "green", "blue"}
item = colors.pop()
print(f"Popped {item}: {colors}")

print()

# === SET OPERATIONS ===
print("=== SET OPERATIONS ===")

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(f"Set 1: {set1}")
print(f"Set 2: {set2}")

# Union (all items from both)
union = set1 | set2
print(f"Union (|): {union}")

# Intersection (common items)
intersection = set1 & set2
print(f"Intersection (&): {intersection}")

# Difference (in set1 but not set2)
difference = set1 - set2
print(f"Difference (-): {difference}")

# Symmetric difference (in either but not both)
sym_diff = set1 ^ set2
print(f"Symmetric Difference (^): {sym_diff}")

print()

# === PRACTICAL EXAMPLES ===
print("=== PRACTICAL EXAMPLES ===")

# Remove duplicates from list
numbers_with_dupes = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
unique = set(numbers_with_dupes)
print(f"With duplicates: {numbers_with_dupes}")
print(f"Unique items: {sorted(list(unique))}")

print()

# Find common friends
umair_friends = {"Fatima", "Hassan", "Bilal"}
fatima_friends = {"Hassan", "Zara", "Bilal"}

common = umair_friends & fatima_friends
print(f"Umair's friends: {umair_friends}")
print(f"Fatima's friends: {fatima_friends}")
print(f"Common friends: {common}")

print()

# Check if subset/superset
vowels = {"a", "e", "i", "o", "u"}
letters = {"a", "b", "c", "e"}

print(f"Vowels: {vowels}")
print(f"Letters: {letters}")
print(f"Is vowels superset of letters? {vowels.issuperset(letters)}")
print(f"Is letters subset of vowels? {letters.issubset(vowels)}")
