"""
===== FILE HANDLING: CSV AND JSON =====
"""

import csv
import json
import os

# === WRITE CSV FILE ===
print("=== WRITE CSV FILE ===")

students = [
    ["Name", "Age", "Grade"],
    ["Umair", "20", "A"],
    ["Fatima", "21", "B"],
    ["Hassan", "19", "A"]
]

filename_csv = "students.csv"

with open(filename_csv, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(students)

print(f"CSV file created: {filename_csv}")

print()

# === READ CSV FILE ===
print("=== READ CSV FILE ===")

with open(filename_csv, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

print()

# === WRITE JSON FILE ===
print("=== WRITE JSON FILE ===")

data = {
    "students": [
        {"name": "Umair", "age": 20, "grade": "A"},
        {"name": "Fatima", "age": 21, "grade": "B"},
        {"name": "Hassan", "age": 19, "grade": "A"}
    ],
    "school": "Tech High"
}

filename_json = "students.json"

with open(filename_json, 'w') as file:
    json.dump(data, file, indent=4)

print(f"JSON file created: {filename_json}")

print()

# === READ JSON FILE ===
print("=== READ JSON FILE ===")

with open(filename_json, 'r') as file:
    loaded_data = json.load(file)
    print(json.dumps(loaded_data, indent=2))

print()

# === USING DICTIONARIES WITH CSV ===
print("=== DICTIONARIES WITH CSV ===")

students_dict = [
    {"Name": "Umair", "Age": 20, "Grade": "A"},
    {"Name": "Fatima", "Age": 21, "Grade": "B"}
]

filename_csv2 = "students_dict.csv"

with open(filename_csv2, 'w', newline='') as file:
    fieldnames = ["Name", "Age", "Grade"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(students_dict)

print(f"CSV with dicts created: {filename_csv2}")

# Read it back
print("Reading back:")
with open(filename_csv2, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)

print()

# === CLEAN UP ===
os.remove(filename_csv)
os.remove(filename_json)
os.remove(filename_csv2)

print("Files cleaned up!")
