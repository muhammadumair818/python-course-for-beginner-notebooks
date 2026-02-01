"""
===== MODULES & LIBRARIES: MATH & RANDOM =====
"""

# === MATH MODULE ===
print("=== MATH MODULE ===")

import math

# Constants
print(f"Pi: {math.pi}")
print(f"E: {math.e}")

# Rounding
print(f"ceil(4.3): {math.ceil(4.3)}")
print(f"floor(4.7): {math.floor(4.7)}")

# Power and square root
print(f"pow(2, 3): {math.pow(2, 3)}")
print(f"sqrt(16): {math.sqrt(16)}")

# Trigonometry
print(f"sin(pi/2): {math.sin(math.pi / 2)}")
print(f"cos(0): {math.cos(0)}")

# Logarithm
print(f"log(100): {math.log10(100)}")

print()

# === RANDOM MODULE ===
print("=== RANDOM MODULE ===")

import random

# Random float 0-1
print(f"random(): {random.random():.3f}")

# Random integer in range
print(f"randint(1, 10): {random.randint(1, 10)}")
print(f"randint(1, 10): {random.randint(1, 10)}")

# Random choice from list
colors = ["red", "green", "blue", "yellow"]
print(f"choice(colors): {random.choice(colors)}")

# Shuffle
cards = [1, 2, 3, 4, 5]
random.shuffle(cards)
print(f"Shuffled: {cards}")

# Sample (random items without replacement)
sample = random.sample(range(1, 11), 3)
print(f"Sample from 1-10: {sample}")

print()

# === DATETIME MODULE ===
print("=== DATETIME MODULE ===")

from datetime import datetime, timedelta

# Current date and time
now = datetime.now()
print(f"Now: {now}")
print(f"Year: {now.year}, Month: {now.month}, Day: {now.day}")

# Format date
print(f"Formatted: {now.strftime('%Y-%m-%d %H:%M:%S')}")

# Date arithmetic
tomorrow = now + timedelta(days=1)
print(f"Tomorrow: {tomorrow.strftime('%Y-%m-%d')}")

# Calculate days between
date1 = datetime(2024, 1, 1)
date2 = datetime(2024, 12, 31)
difference = date2 - date1
print(f"Days in 2024: {difference.days}")

print()

# === PRACTICAL EXAMPLE: SIMPLE GAME ===
print("=== PRACTICAL: GUESS THE NUMBER ===")

target = random.randint(1, 10)
guess = 5  # Simulating user input

if guess == target:
    print(f"Correct! The number was {target}")
elif guess < target:
    print(f"Too low! The number was {target}")
else:
    print(f"Too high! The number was {target}")

print()

# === PRACTICAL EXAMPLE: ROLL DICE ===
print("=== PRACTICAL: ROLL DICE ===")

def roll_dice(num_dice=1):
    rolls = [random.randint(1, 6) for _ in range(num_dice)]
    return rolls

print(f"Roll 1 die: {roll_dice(1)}")
print(f"Roll 2 dice: {roll_dice(2)}")
print(f"Roll 3 dice: {roll_dice(3)}")

print()

# === CALCULATING STATISTICS ===
print("=== STATISTICS ===")

import statistics

grades = [85, 90, 78, 92, 88, 95]

print(f"Grades: {grades}")
print(f"Mean: {statistics.mean(grades):.2f}")
print(f"Median: {statistics.median(grades):.2f}")
print(f"Stdev: {statistics.stdev(grades):.2f}")
