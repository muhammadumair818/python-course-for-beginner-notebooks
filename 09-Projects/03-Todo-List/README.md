# Todo List Application

A command-line task management system with persistent storage.

## Features

- ✅ Add tasks
- 📝 View all tasks
- ✓ Mark tasks as complete
- 🗑️ Delete tasks
- 💾 Save to JSON file
- 📂 Load from file on startup

## How to Run

```bash
python todo.py
```

## Menu Options

1. **Add Task** - Create a new task
2. **View Tasks** - Display all tasks with status
3. **Complete Task** - Mark a task as done
4. **Delete Task** - Remove a task
5. **Clear All** - Delete all tasks
6. **Exit** - Quit the app

## Sample Usage

```
==================================================
WELCOME TO TODO LIST APP
==================================================

Options:
  1. Add task
  2. View tasks
  3. Complete task
  4. Delete task
  5. Clear all
  6. Exit

Enter choice (1-6): 1
Enter task: Buy groceries
✅ Task added: Buy groceries
Tasks saved!

Enter choice (1-6): 2

==================================================
YOUR TASKS
==================================================
[ ] ID 1: Buy groceries
==================================================

Enter choice (1-6): 3
Enter task ID to complete: 1
✅ Marked complete: Buy groceries
```

## Data Storage

Tasks are saved in `tasks.json` in the same directory.

## Learning Concepts

- Class-based design
- File I/O with JSON
- Data persistence
- Menu-driven interface
- List operations

---

Stay organized! 📋
