"""
===== PYTHON BASICS: VARIABLES =====

A variable is a named container that stores a value.
Python variables don't need to be declared with a type - Python figures it out!

Variable Naming Rules:
- Must start with a letter or underscore
- Can contain letters, numbers, and underscores
- Python is case-sensitive (name != Name)
- Avoid Python keywords (if, for, while, etc.)
- Use descriptive names (good: age, first_name; bad: x, y1)
"""

# === CREATING VARIABLES ===
name = "Umair"  # String variable
age = 25        # Integer variable
height = 5.6    # Float variable (decimal)
is_student = True  # Boolean variable (True/False)

# Print the variables
print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is Student:", is_student)
print()

# === CHECKING VARIABLE TYPE ===
print("=== Variable Types ===")
print(f"Type of name: {type(name)}")
print(f"Type of age: {type(age)}")
print(f"Type of height: {type(height)}")
print(f"Type of is_student: {type(is_student)}")
print()

# === CHANGING VARIABLE VALUES ===
print("=== Changing Values ===")
print(f"Original age: {age}")
age = 26  # Update the age
print(f"Updated age: {age}")
print()

# === MULTIPLE ASSIGNMENT ===
print("=== Multiple Assignment ===")
x, y, z = 10, 20, 30
print(f"x = {x}, y = {y}, z = {z}")
print()

# === VARIABLE NAMING CONVENTIONS ===
print("=== Good Variable Names ===")
first_name = "Fatima"  # Snake case: preferred in Python
lastName = "Smith"  # Camel case: less common in Python
AGE_LIMIT = 18  # UPPERCASE: for constants (values that shouldn't change)

print(f"First name: {first_name}")
print(f"Last name: {lastName}")
print(f"Age limit: {AGE_LIMIT}")
print()

# === DYNAMIC TYPING ===
print("=== Dynamic Typing (Python feature) ===")
value = "Hello"  # String
print(f"value = {value}, type = {type(value)}")

value = 42  # Same variable, now an integer
print(f"value = {value}, type = {type(value)}")

value = 3.14  # Same variable, now a float
print(f"value = {value}, type = {type(value)}")
print()

# === PRACTICE EXERCISES ===
print("=== Practice Exercises ===")
# Exercise 1: Create variables for a person
print("\nExercise 1: Person Information")
person_name = "Usman"
person_age = 30
person_city = "Karachi"
person_email = "usman@email.com"

print(f"Name: {person_name}")
print(f"Age: {person_age}")
print(f"City: {person_city}")
print(f"Email: {person_email}")

# Exercise 2: Update values
print("\nExercise 2: Update Birthday")
print(f"Age before birthday: {person_age}")
person_age = person_age + 1
print(f"Age after birthday: {person_age}")

# Exercise 3: Check types
print("\nExercise 3: Variable Types")
value1 = 100
value2 = "100"
value3 = 100.0

print(f"{value1} is of type: {type(value1)}")
print(f"{value2} is of type: {type(value2)}")
print(f"{value3} is of type: {type(value3)}")
print("Notice: '100' (string) and 100 (integer) are different!")
