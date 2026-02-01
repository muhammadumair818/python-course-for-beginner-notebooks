"""
===== MODULES & LIBRARIES: PANDAS & NUMPY INTRODUCTION =====
"""

import pandas as pd
import numpy as np

# === NUMPY ARRAYS ===
print("=== NUMPY ARRAYS ===")

# Create array from list
arr1 = np.array([1, 2, 3, 4, 5])
print(f"Array: {arr1}")
print(f"Shape: {arr1.shape}")
print(f"Data type: {arr1.dtype}")

# Array operations
print(f"Sum: {arr1.sum()}")
print(f"Mean: {arr1.mean()}")
print(f"Max: {arr1.max()}")

print()

# === 2D ARRAYS ===
print("=== 2D ARRAYS ===")

matrix = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])

print(f"Matrix:\n{matrix}")
print(f"Shape: {matrix.shape}")
print(f"Element [1, 2]: {matrix[1, 2]}")

print()

# === PANDAS SERIES ===
print("=== PANDAS SERIES ===")

# Create Series (1D labeled array)
ages = pd.Series([25, 30, 35, 40], index=["Umair", "Fatima", "Hassan", "Ayesha"])
print(f"Ages:\n{ages}")
print(f"Umair's age: {ages['Umair']}")

print()

# === PANDAS DATAFRAME ===
print("=== PANDAS DATAFRAME ===")

# Create DataFrame (2D labeled table)
data = {
    "Name": ["Umair", "Fatima", "Hassan"],
    "Age": [25, 30, 35],
    "Salary": [50000, 60000, 70000]
}

df = pd.DataFrame(data)
print("DataFrame:")
print(df)

print()

# === ACCESSING DATA ===
print("=== ACCESSING DATAFRAME DATA ===")

print(f"Names: {df['Name'].tolist()}")
print(f"First row:\n{df.iloc[0]}")
print(f"Age of Umair: {df.loc[0, 'Age']}")

print()

# === DATAFRAME OPERATIONS ===
print("=== DATAFRAME OPERATIONS ===")

print(f"Shape: {df.shape}")
print(f"Columns: {df.columns.tolist()}")
print(f"Info:\n{df.info()}")
print(f"\nStatistics:\n{df.describe()}")

print()

# === FILTERING ===
print("=== FILTERING DATA ===")

high_earners = df[df['Salary'] > 55000]
print("High earners (> $55000):")
print(high_earners)

print()

# === PRACTICAL EXAMPLE ===
print("=== PRACTICAL: STUDENT GRADES ===")

grades_data = {
    "Student": ["Umair", "Fatima", "Hassan", "Ayesha"],
    "Math": [85, 90, 78, 92],
    "Science": [88, 85, 92, 88],
    "English": [92, 88, 85, 90]
}

grades_df = pd.DataFrame(grades_data)
grades_df["Average"] = grades_df[["Math", "Science", "English"]].mean(axis=1)

print(grades_df)
