"""
===== DATA STRUCTURES: EXERCISES =====

Practice with lists, tuples, sets, and dictionaries.
"""

print("=" * 50)
print("DATA STRUCTURES EXERCISES")
print("=" * 50)
print()

# ===== EXERCISE 1: List Operations =====
print("EXERCISE 1: List Operations")
print("-" * 40)

numbers = [10, 20, 30, 40, 50]
print(f"Original list: {numbers}")
print(f"First element: {numbers[0]}")
print(f"Last element: {numbers[-1]}")
print(f"Length: {len(numbers)}")
print(f"Sum: {sum(numbers)}")
print(f"Average: {sum(numbers) / len(numbers)}")

print()

# ===== EXERCISE 2: List Modification =====
print("EXERCISE 2: List Modification")
print("-" * 40)

fruits = ["apple", "banana", "orange"]
print(f"Original: {fruits}")

fruits.append("mango")
print(f"After append: {fruits}")

fruits.insert(1, "grape")
print(f"After insert: {fruits}")

fruits.remove("banana")
print(f"After remove: {fruits}")

print()

# ===== EXERCISE 3: List Slicing =====
print("EXERCISE 3: List Slicing")
print("-" * 40)

numbers = list(range(0, 10))
print(f"Numbers: {numbers}")
print(f"First 3: {numbers[:3]}")
print(f"Last 3: {numbers[-3:]}")
print(f"Every 2nd: {numbers[::2]}")
print(f"Reversed: {numbers[::-1]}")

print()

# ===== EXERCISE 4: Tuple Unpacking =====
print("EXERCISE 4: Tuple Unpacking")
print("-" * 40)

person = ("Umair", 25, "Engineer")
name, age, job = person
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Job: {job}")

print()

# ===== EXERCISE 5: Set Operations =====
print("EXERCISE 5: Set Operations")
print("-" * 40)

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print(f"Set 1: {set1}")
print(f"Set 2: {set2}")
print(f"Union: {set1 | set2}")
print(f"Intersection: {set1 & set2}")
print(f"Difference: {set1 - set2}")

print()

# ===== EXERCISE 6: Remove Duplicates =====
print("EXERCISE 6: Remove Duplicates")
print("-" * 40)

items = [1, 2, 2, 3, 3, 3, 4, 5, 5]
unique = list(set(items))
print(f"With duplicates: {items}")
print(f"Unique items: {sorted(unique)}")

print()

# ===== EXERCISE 7: Dictionary Access =====
print("EXERCISE 7: Dictionary Access")
print("-" * 40)

student = {
    "name": "Usman",
    "age": 20,
    "gpa": 3.8,
    "major": "Computer Science"
}

print(f"Dictionary: {student}")
print(f"Name: {student['name']}")
print(f"GPA: {student['gpa']}")
print(f"Major: {student['major']}")

print()

# ===== EXERCISE 8: Dictionary Modification =====
print("EXERCISE 8: Dictionary Modification")
print("-" * 40)

person = {"name": "Umair", "age": 25}
print(f"Original: {person}")

person["city"] = "New York"
print(f"Added city: {person}")

person["age"] = 26
print(f"Updated age: {person}")

del person["city"]
print(f"Deleted city: {person}")

print()

# ===== EXERCISE 9: Grade Book =====
print("EXERCISE 9: Grade Book")
print("-" * 40)

grades = {
    "Umair": 90,
    "Fatima": 85,
    "Hassan": 95,
    "Ayesha": 88
}

print(f"Grades: {grades}")
print(f"Average: {sum(grades.values()) / len(grades):.2f}")
print(f"Highest: {max(grades.values())}")
print(f"Lowest: {min(grades.values())}")

for name, grade in grades.items():
    if grade >= 90:
        status = "Excellent"
    elif grade >= 80:
        status = "Good"
    else:
        status = "Needs improvement"
    print(f"  {name}: {grade} ({status})")

print()

# ===== EXERCISE 10: Word Frequency =====
print("EXERCISE 10: Word Frequency")
print("-" * 40)

text = "python python java python javascript java c"
words = text.split()

word_freq = {}
for word in words:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1

print(f"Text: {text}")
print(f"Word frequencies:")
for word, count in sorted(word_freq.items()):
    print(f"  {word}: {count}")

print()

print("=" * 50)
print("GREAT JOB!")
print("=" * 50)
