# 07-OOP: Object-Oriented Programming

Master classes, objects, and inheritance.

## Topics Covered

### 1. **Classes & Objects** (`01_classes_objects.py`)
- Defining classes
- Attributes and methods
- Special methods (__init__, __str__)

### 2. **Inheritance** (`02_inheritance.py`)
- Creating subclasses
- Using super()
- Polymorphism

### 3. **Exercises** (`03_exercises.py`)
- Practice problems

---

## Quick Reference

```python
# Class definition
class ClassName:
    def __init__(self, param):
        self.param = param
    
    def method(self):
        return self.param

# Inheritance
class Child(Parent):
    def __init__(self, param1, param2):
        super().__init__(param1)
        self.param2 = param2
```

---

Run: `python 01_classes_objects.py`
