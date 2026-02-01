"""
===== PYTHON BASICS: STRING OPERATIONS =====

Strings are sequences of characters. Python provides many methods to work with strings.
"""

# === STRING BASICS ===
print("=== STRING BASICS ===")
text = "Hello, Python!"

print(f"String: {text}")
print(f"Length: {len(text)}")
print()

# === INDEXING (Getting individual characters) ===
print("=== INDEXING ===")
word = "Python"
print(f"String: {word}")
print(f"Index 0 (first char): {word[0]}")
print(f"Index 1: {word[1]}")
print(f"Index 5 (last char): {word[5]}")
print(f"Index -1 (last char from end): {word[-1]}")
print(f"Index -2 (second from end): {word[-2]}")
print()

# === SLICING (Getting substrings) ===
print("=== SLICING ===")
sentence = "Python Programming"

print(f"Full string: {sentence}")
print(f"sentence[0:6]: {sentence[0:6]}")  # Characters 0-5
print(f"sentence[7:18]: {sentence[7:18]}")  # Characters 7-17
print(f"sentence[:6]: {sentence[:6]}")  # From start to 5
print(f"sentence[7:]: {sentence[7:]}")  # From 7 to end
print(f"sentence[::2]: {sentence[::2]}")  # Every 2nd character
print(f"sentence[::-1]: {sentence[::-1]}")  # Reverse the string
print()

# === STRING METHODS ===
print("=== STRING METHODS ===")

text = "Python Programming"

# Length
print(f"Length: {len(text)}")

# Uppercase and lowercase
print(f"Uppercase: {text.upper()}")
print(f"Lowercase: {text.lower()}")

# Capitalize and title
print(f"Capitalize: {text.capitalize()}")
print(f"Title: {text.title()}")

# Strip (remove whitespace)
text_with_spaces = "  Hello, World!  "
print(f"Original: '{text_with_spaces}'")
print(f"Strip: '{text_with_spaces.strip()}'")
print(f"Left strip: '{text_with_spaces.lstrip()}'")
print(f"Right strip: '{text_with_spaces.rstrip()}'")
print()

# === SEARCHING ===
print("=== SEARCHING IN STRINGS ===")

text = "The quick brown fox jumps"

# Find position
print(f"Text: {text}")
print(f"Position of 'brown': {text.find('brown')}")
print(f"Position of 'fox': {text.find('fox')}")
print(f"Position of 'dog' (not found): {text.find('dog')}")

# Check if substring exists
print(f"'quick' in text: {'quick' in text}")
print(f"'slow' in text: {'slow' in text}")

# Count occurrences
text2 = "apple apple apple banana"
print(f"Count of 'apple': {text2.count('apple')}")
print()

# === REPLACING ===
print("=== REPLACING ===")

text = "I love Python and I love coding"
new_text = text.replace("love", "enjoy")
print(f"Original: {text}")
print(f"Replaced: {new_text}")

# Replace only first occurrence
new_text2 = text.replace("love", "enjoy", 1)
print(f"Replace first only: {new_text2}")
print()

# === SPLITTING AND JOINING ===
print("=== SPLITTING AND JOINING ===")

# Split (string to list)
sentence = "Apple Banana Cherry Date"
words = sentence.split()
print(f"Original: {sentence}")
print(f"Split by space: {words}")

# Split by custom separator
csv_data = "Name,Age,City"
fields = csv_data.split(",")
print(f"CSV: {csv_data}")
print(f"Split by comma: {fields}")

# Join (list to string)
items = ["Apple", "Banana", "Cherry"]
joined = " | ".join(items)
print(f"Items: {items}")
print(f"Joined with ' | ': {joined}")
print()

# === STRING CONCATENATION ===
print("=== STRING CONCATENATION ===")

first_name = "Usman"
last_name = "Khan"

# Method 1: +
full_name1 = first_name + " " + last_name
print(f"Method 1 (+): {full_name1}")

# Method 2: f-string
full_name2 = f"{first_name} {last_name}"
print(f"Method 2 (f-string): {full_name2}")

# Method 3: .format()
full_name3 = "{} {}".format(first_name, last_name)
print(f"Method 3 (.format()): {full_name3}")
print()

# === STRING REPETITION ===
print("=== STRING REPETITION ===")

print("Ha" * 3)  # Ha Ha Ha
print("*" * 10)  # **********
print("-" * 20)
print()

# === CHECKING STRING PROPERTIES ===
print("=== CHECKING STRING PROPERTIES ===")

# Check if all characters are...
text = "Hello123"
print(f"Text: {text}")
print(f"isalpha() (all letters): {text.isalpha()}")
print(f"isdigit() (all digits): {text.isdigit()}")
print(f"isalnum() (all alphanumeric): {text.isalnum()}")
print(f"isspace(): {text.isspace()}")

# Check for uppercase/lowercase
text2 = "HelloWorld"
print(f"\nText: {text2}")
print(f"isupper(): {text2.isupper()}")
print(f"islower(): {text2.islower()}")
print()

# === PRACTICAL EXAMPLE ===
print("=== PRACTICAL EXAMPLE: Processing User Input ===")

email = "  USMAN.KHAN@EXAMPLE.COM  "
print(f"Original email: '{email}'")

# Clean and normalize
cleaned_email = email.strip().lower()
print(f"Cleaned email: '{cleaned_email}'")

# Extract username
username = cleaned_email.split("@")[0]
print(f"Username: {username}")

# Extract domain
domain = cleaned_email.split("@")[1]
print(f"Domain: {domain}")
