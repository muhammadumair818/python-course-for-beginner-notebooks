"""
===== FILE HANDLING: READ & WRITE FILES =====
"""

# === WRITING TO FILES ===
print("=== WRITING TO FILES ===")

# Write mode ('w')
filename = "sample.txt"

content = """Hello, World!
This is a sample file.
Python is awesome!
"""

with open(filename, 'w') as file:
    file.write(content)

print(f"File '{filename}' created!")

print()

# === READING FILES ===
print("=== READING FILES ===")

# Read entire file
with open(filename, 'r') as file:
    text = file.read()
    print(text)

print()

# === READING LINE BY LINE ===
print("=== READING LINES ===")

with open(filename, 'r') as file:
    for line in file:
        print(f"Line: {line.strip()}")

print()

# === APPEND MODE ===
print("=== APPEND MODE ===")

new_content = "\nAppended line!"

with open(filename, 'a') as file:
    file.write(new_content)

print("Content appended!")

# Read to verify
with open(filename, 'r') as file:
    print(file.read())

print()

# === CHECK IF FILE EXISTS ===
print("=== CHECK IF FILE EXISTS ===")

import os

if os.path.exists(filename):
    print(f"File '{filename}' exists!")
    file_size = os.path.getsize(filename)
    print(f"File size: {file_size} bytes")

print()

# === DELETE FILE ===
print("=== DELETE FILE ===")

# Uncomment to delete:
# os.remove(filename)
# print(f"File '{filename}' deleted!")

print()

# === WRITE MULTIPLE LINES ===
print("=== WRITE MULTIPLE LINES ===")

lines = ["Line 1", "Line 2", "Line 3"]

with open("lines.txt", 'w') as file:
    for line in lines:
        file.write(line + "\n")

with open("lines.txt", 'r') as file:
    content = file.read()
    print(content)

print()

# === READ ALL LINES AS LIST ===
print("=== READLINES ===")

with open("lines.txt", 'r') as file:
    all_lines = file.readlines()
    print(f"Lines: {all_lines}")

# Clean up
import os
os.remove("sample.txt")
os.remove("lines.txt")
