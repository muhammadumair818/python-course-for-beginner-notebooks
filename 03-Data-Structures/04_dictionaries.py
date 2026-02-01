"""
===== DATA STRUCTURES: DICTIONARIES =====

A dictionary is an unordered collection of key-value pairs.
- Keys are unique
- Access by key (not index)
- Mutable
"""

# === CREATING DICTIONARIES ===
print("=== CREATING DICTIONARIES ===")

# Empty dictionary
empty = {}
print(f"Empty: {empty}")

# Dictionary with items
person = {
    "name": "Umair",
    "age": 25,
    "city": "Karachi"
}
print(f"Person: {person}")

# Using dict() constructor
info = dict(name="Fatima", age=30, email="fatima@example.com")
print(f"Info: {info}")

print()

# === ACCESSING VALUES ===
print("=== ACCESSING VALUES ===")

person = {"name": "Umair", "age": 25, "city": "Karachi"}
print(f"Dictionary: {person}")
print(f"Name: {person['name']}")
print(f"Age: {person['age']}")

# Using get() (safer)
email = person.get("email")
print(f"Email: {email}")

# Using get() with default
email = person.get("email", "Not provided")
print(f"Email (with default): {email}")

print()

# === MODIFYING DICTIONARIES ===
print("=== MODIFYING DICTIONARIES ===")

person = {"name": "Umair", "age": 25}
print(f"Original: {person}")

# Add item
person["city"] = "Karachi"
print(f"After adding city: {person}")

# Modify item
person["age"] = 26
print(f"After updating age: {person}")

# Remove item
del person["city"]
print(f"After deleting city: {person}")

# Pop (remove and get value)
age = person.pop("age")
print(f"Popped age: {age}")
print(f"After pop: {person}")

# Clear
temp = {"x": 1, "y": 2}
temp.clear()
print(f"After clear: {temp}")

print()

# === DICTIONARY METHODS ===
print("=== DICTIONARY METHODS ===")

student = {
    "name": "Usman",
    "age": 20,
    "grade": "A"
}

print(f"Dictionary: {student}")
print(f"Keys: {student.keys()}")
print(f"Values: {student.values()}")
print(f"Items: {student.items()}")

print()

# === CHECKING KEYS ===
print("=== CHECKING KEYS ===")

person = {"name": "Umair", "age": 25}
print(f"Dictionary: {person}")
print(f"'name' in person: {'name' in person}")
print(f"'city' in person: {'city' in person}")

print()

# === LOOPING THROUGH DICTIONARIES ===
print("=== LOOPING ===")

person = {"name": "Umair", "age": 25, "city": "Karachi"}

print("Loop keys:")
for key in person:
    print(f"  {key}")

print("\nLoop key-value pairs:")
for key, value in person.items():
    print(f"  {key}: {value}")

print("\nLoop values:")
for value in person.values():
    print(f"  {value}")

print()

# === NESTED DICTIONARIES ===
print("=== NESTED DICTIONARIES ===")

company = {
    "name": "TechCorp",
    "employees": {
        "umair": {"role": "Engineer", "salary": 100000},
        "fatima": {"role": "Manager", "salary": 120000}
    }
}

print(f"Company: {company['name']}")
print(f"Umair's role: {company['employees']['umair']['role']}")
print(f"Fatima's salary: ${company['employees']['fatima']['salary']}")

print()

# === PRACTICAL EXAMPLES ===
print("=== PRACTICAL EXAMPLES ===")

# Student grades
grades = {
    "Umair": 85,
    "Fatima": 92,
    "Hassan": 78,
    "Ayesha": 95
}

print(f"Grades: {grades}")
print(f"Average: {sum(grades.values()) / len(grades):.2f}")
print(f"Highest: {max(grades.values())}")

print()

# Phone book
contacts = {
    "Umair": "555-1234",
    "Fatima": "555-5678",
    "Hassan": "555-9999"
}

search = "Umair"
if search in contacts:
    print(f"{search}'s phone: {contacts[search]}")

print()

# Word count
sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(f"Word frequencies:")
for word, count in word_count.items():
    print(f"  {word}: {count}")
