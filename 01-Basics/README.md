# 01-Basics: Python Fundamentals

Welcome to the Basics section! This folder covers the foundational concepts you need to understand Python.

## Topics Covered

### 1. **Variables** (`01_variables.py`)
Learn how to create and manage variables in Python.
- Creating variables
- Variable naming conventions
- Dynamic typing
- Best practices

**Key Concepts:**
- Variables store data with meaningful names
- Python is dynamically typed (no need to declare type)
- Use snake_case for variable names

**Run:** `python 01_variables.py`

---

### 2. **Data Types** (`02_data_types.py`)
Understand Python's fundamental data types.
- **int**: Whole numbers (5, -10, 0)
- **float**: Decimal numbers (3.14, -2.5)
- **str**: Text ("Hello", 'World')
- **bool**: True or False
- **None**: Absence of value
- Type conversion

**Key Concepts:**
- Each data type serves a different purpose
- Use `type()` to check a variable's type
- Convert between types using `int()`, `float()`, `str()`

**Run:** `python 02_data_types.py`

---

### 3. **Operators** (`03_operators.py`)
Work with different types of operators.
- **Arithmetic**: +, -, *, /, //, %, **
- **Comparison**: ==, !=, <, >, <=, >=
- **Logical**: and, or, not
- **Assignment**: =, +=, -=, *=, /=
- Operator precedence

**Key Concepts:**
- Arithmetic operators follow mathematical rules
- Comparison operators return True or False
- Logical operators combine boolean values
- Parentheses control order of operations

**Run:** `python 03_operators.py`

---

### 4. **Input/Output** (`04_input_output.py`)
Interact with users through input and output.
- `print()` function for displaying output
- `input()` function for getting user input
- String formatting with f-strings
- Converting input to numbers

**Key Concepts:**
- `print()` displays output to the console
- `input()` always returns a string
- Convert input to numbers using `int()` or `float()`
- F-strings are modern and recommended

**Run:** `python 04_input_output.py`

---

### 5. **String Operations** (`05_string_operations.py`)
Master working with text data.
- Indexing and slicing
- String methods (upper, lower, strip, replace, etc.)
- Searching and replacing
- Splitting and joining
- String concatenation and repetition

**Key Concepts:**
- Strings are sequences of characters
- Use indexing to access individual characters
- Use slicing to get substrings
- Python has many built-in string methods

**Run:** `python 05_string_operations.py`

---

### 6. **Exercises** (`06_exercises.py`)
Practice problems to reinforce your learning.
- Temperature conversion
- Personal information formatting
- Simple calculator
- String manipulation
- Data type conversion
- Logical operations
- Invoice calculation
- String slicing
- Age in different measurements

**Key Concepts:**
- Applying basics to real-world scenarios
- Combining multiple concepts
- Building confidence with practical problems

**Run:** `python 06_exercises.py`

---

## How to Use This Folder

1. **Start with `01_variables.py`** and run it to see examples
2. **Study the comments** to understand each concept
3. **Modify the code** and experiment
4. **Try the exercises** in `06_exercises.py`
5. **Write your own** programs using these concepts

## Sample Output

### Running Variables:
```
Name: Alice
Age: 25
Height: 5.6
Is Student: True

=== Variable Types ===
Type of name: <class 'str'>
Type of age: <class 'int'>
Type of height: <class 'float'>
Type of is_student: <class 'bool'>
```

### Running Operators:
```
=== ARITHMETIC OPERATORS ===
10 + 3 = 13
10 - 3 = 7
10 * 3 = 30
10 / 3 = 3.3333333333333335
10 // 3 = 3
10 % 3 = 1
10 ** 3 = 1000
```

## Common Mistakes to Avoid

1. ❌ **Forgetting quotes for strings:**
   ```python
   name = Alice  # ERROR
   name = "Alice"  # CORRECT
   ```

2. ❌ **Mixing up input conversion:**
   ```python
   age = input("Enter age: ")  # This is a STRING
   age = int(input("Enter age: "))  # This is an INTEGER
   ```

3. ❌ **Using wrong operator:**
   ```python
   if age = 25:  # ERROR (= is assignment)
   if age == 25:  # CORRECT (== is comparison)
   ```

4. ❌ **Forgetting to convert strings to numbers:**
   ```python
   num1 = input("Enter number: ")
   result = num1 + 5  # ERROR: can't add string and int
   ```

## Next Steps

After mastering these basics:
- Move to **02-Control-Flow** to learn conditionals and loops
- Practice writing small programs
- Combine multiple concepts together

## Quick Reference

| Concept | Example |
|---------|---------|
| Variable | `name = "Alice"` |
| Data Type | `age = 25` (int), `price = 19.99` (float) |
| Arithmetic | `10 + 5`, `10 * 2`, `10 / 2` |
| Comparison | `age > 18`, `name == "Alice"` |
| Logical | `age > 18 and has_license` |
| String | `"Hello" + " " + "World"` |
| Input | `name = input("Enter name: ")` |
| Output | `print(f"Hello {name}")` |

## Tips for Success

✅ **Do:** Run every script and see the output
✅ **Do:** Modify examples and experiment
✅ **Do:** Write your own code from scratch
✅ **Do:** Use meaningful variable names

❌ **Don't:** Skip running the code
❌ **Don't:** Copy without understanding
❌ **Don't:** Be afraid to make mistakes
❌ **Don't:** Rush through the material

---

Happy coding! 🐍
