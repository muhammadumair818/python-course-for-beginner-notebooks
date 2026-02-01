# 02-Control-Flow: Conditional Statements & Loops

Learn to control the flow of your programs with conditional logic and loops.

## Topics Covered

### 1. **If/Elif/Else** (`01_if_elif_else.py`)
Make decisions in your code based on conditions.
- Simple if statements
- if-else logic
- if-elif-else chains
- Nested conditionals
- Logical operators (and, or, not)
- Ternary operator (single-line if-else)

**Key Concepts:**
- Conditions evaluate to True or False
- Use elif for multiple conditions
- Logical operators combine conditions
- Indentation matters!

**Run:** `python 01_if_elif_else.py`

---

### 2. **Loops** (`02_loops.py`)
Repeat code multiple times efficiently.
- FOR loops with range()
- FOR loops with lists
- enumerate() for index + value
- WHILE loops
- Loop-else (runs when loop completes)
- Nested loops

**Key Concepts:**
- FOR loops iterate a known number of times
- WHILE loops continue until condition is false
- range() generates sequences
- Nested loops process 2D structures

**Run:** `python 02_loops.py`

---

### 3. **Break & Continue** (`03_break_continue.py`)
Control loop execution with break and continue.
- BREAK: Exit loop immediately
- CONTINUE: Skip to next iteration
- Usage in nested loops
- for-else with break

**Key Concepts:**
- break stops loop execution
- continue skips current iteration
- Useful for searching and filtering
- for-else runs when loop completes normally

**Run:** `python 03_break_continue.py`

---

### 4. **List Comprehension** (`04_list_comprehension.py`)
Create and transform lists concisely.
- Simple list comprehension
- Transformations (square, double, etc.)
- Filtering with conditions
- Nested comprehensions
- Dictionary comprehensions

**Key Concepts:**
- Concise syntax for creating lists
- More readable and efficient than loops
- Can include conditions
- Works with any iterable

**Run:** `python 04_list_comprehension.py`

---

### 5. **Exercises** (`05_exercises.py`)
Practice problems combining all control flow concepts.
- Simple calculator
- Grade assignment
- Number classification
- Counting and summing
- Searching and filtering
- Pattern generation
- List transformations

**Run:** `python 05_exercises.py`

---

## How to Use This Folder

1. Start with `01_if_elif_else.py`
2. Study conditional logic
3. Move to `02_loops.py` and understand iteration
4. Learn break/continue with `03_break_continue.py`
5. Master list comprehension with `04_list_comprehension.py`
6. Practice with `05_exercises.py`

## Common Control Flow Patterns

### Pattern 1: Checking Multiple Conditions
```python
age = 25
has_license = True

if age >= 18 and has_license:
    print("Can drive")
```

### Pattern 2: Finding in a List
```python
fruits = ["apple", "banana", "orange"]
search = "banana"

for fruit in fruits:
    if fruit == search:
        print("Found!")
        break
```

### Pattern 3: Filtering
```python
numbers = [1, 2, 3, 4, 5]
evens = [num for num in numbers if num % 2 == 0]
```

### Pattern 4: Transforming
```python
numbers = [1, 2, 3, 4, 5]
squared = [num ** 2 for num in numbers]
```

## Sample Output

### Running If/Elif/Else:
```
=== IF-ELIF-ELSE STATEMENT ===
Score: 85
Grade: B
```

### Running Loops:
```
=== MULTIPLICATION TABLE ===
7 × 1 = 7
7 × 2 = 14
7 × 3 = 21
...
7 × 10 = 70
```

### Running List Comprehension:
```
Original: [1, 2, 3, 4, 5]
Doubled: [2, 4, 6, 8, 10]
Even only: [2, 4]
```

## Common Mistakes to Avoid

1. ❌ **Forgetting colons after if/for/while:**
   ```python
   if age > 18
       print("Adult")  # ERROR
   if age > 18:
       print("Adult")  # CORRECT
   ```

2. ❌ **Wrong indentation:**
   ```python
   if age > 18:
   print("Adult")  # ERROR: Not indented
   ```

3. ❌ **Using = instead of ==:**
   ```python
   if age = 25:  # ERROR: assignment
   if age == 25:  # CORRECT: comparison
   ```

4. ❌ **Off-by-one errors in range:**
   ```python
   for i in range(5):  # 0, 1, 2, 3, 4 (NOT including 5)
   ```

5. ❌ **Infinite while loops:**
   ```python
   while True:  # Make sure to have a break!
       user_input = input("Continue? y/n: ")
       if user_input == "n":
           break
   ```

## Quick Reference

| Concept | Syntax | Example |
|---------|--------|---------|
| If statement | `if condition:` | `if age >= 18:` |
| If-else | `if condition: ... else: ...` | `if score > 50: ... else: ...` |
| If-elif-else | `if ... elif ... else:` | `if score >= 90: ... elif score >= 80: ...` |
| For loop | `for item in sequence:` | `for num in range(10):` |
| While loop | `while condition:` | `while count < 10:` |
| Break | `break` | `if num == 5: break` |
| Continue | `continue` | `if num % 2 == 0: continue` |
| List comp | `[expr for item in seq if cond]` | `[x*2 for x in range(5) if x > 2]` |

## Tips for Success

✅ **Do:** Test your conditions with print statements
✅ **Do:** Use meaningful variable names
✅ **Do:** Break complex logic into smaller pieces
✅ **Do:** Use list comprehensions for readability

❌ **Don't:** Nest loops too deeply (makes code hard to read)
❌ **Don't:** Forget to update loop variables
❌ **Don't:** Mix up loop and condition syntax

## Next Steps

After mastering control flow:
- Move to **03-Data-Structures** for working with complex data
- Learn functions in **04-Functions** to reuse code
- Build projects that combine these concepts

---

Happy coding! 🎉
