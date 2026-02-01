"""
TODO LIST APPLICATION

A command-line task management app.

Features:
- Add tasks
- View all tasks
- Mark tasks as complete
- Delete tasks
- Save tasks to file
- Load tasks from file
"""

import os
import json

class TodoList:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = []
        self.load_tasks()
    
    def load_tasks(self):
        """Load tasks from file"""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as file:
                    self.tasks = json.load(file)
                print(f"Loaded {len(self.tasks)} tasks from file.")
            except:
                self.tasks = []
                print("Error loading tasks. Starting fresh.")
        else:
            self.tasks = []
    
    def save_tasks(self):
        """Save tasks to file"""
        with open(self.filename, 'w') as file:
            json.dump(self.tasks, file, indent=2)
        print("Tasks saved!")
    
    def add_task(self, task):
        """Add a new task"""
        new_task = {
            "id": len(self.tasks) + 1,
            "task": task,
            "completed": False
        }
        self.tasks.append(new_task)
        print(f"✅ Task added: {task}")
        self.save_tasks()
    
    def view_tasks(self):
        """Display all tasks"""
        if not self.tasks:
            print("📝 No tasks! You're all caught up!")
            return
        
        print("\n" + "="*50)
        print("YOUR TASKS")
        print("="*50)
        
        for task in self.tasks:
            status = "✓" if task["completed"] else " "
            print(f"[{status}] ID {task['id']}: {task['task']}")
        
        print("="*50)
    
    def complete_task(self, task_id):
        """Mark task as complete"""
        for task in self.tasks:
            if task["id"] == task_id:
                task["completed"] = True
                print(f"✅ Marked complete: {task['task']}")
                self.save_tasks()
                return
        print("Task not found!")
    
    def delete_task(self, task_id):
        """Delete a task"""
        for i, task in enumerate(self.tasks):
            if task["id"] == task_id:
                deleted = self.tasks.pop(i)
                print(f"🗑️ Deleted: {deleted['task']}")
                self.save_tasks()
                return
        print("Task not found!")
    
    def clear_all(self):
        """Delete all tasks"""
        if self.tasks:
            self.tasks.clear()
            print("🗑️ All tasks deleted!")
            self.save_tasks()

def main():
    """Main application loop"""
    
    todo = TodoList()
    
    print("\n" + "="*50)
    print("WELCOME TO TODO LIST APP")
    print("="*50)
    
    while True:
        print("\nOptions:")
        print("  1. Add task")
        print("  2. View tasks")
        print("  3. Complete task")
        print("  4. Delete task")
        print("  5. Clear all")
        print("  6. Exit")
        
        choice = input("\nEnter choice (1-6): ").strip()
        
        if choice == '1':
            task = input("Enter task: ").strip()
            if task:
                todo.add_task(task)
            else:
                print("Task cannot be empty!")
        
        elif choice == '2':
            todo.view_tasks()
        
        elif choice == '3':
            todo.view_tasks()
            try:
                task_id = int(input("Enter task ID to complete: "))
                todo.complete_task(task_id)
            except ValueError:
                print("Invalid ID!")
        
        elif choice == '4':
            todo.view_tasks()
            try:
                task_id = int(input("Enter task ID to delete: "))
                todo.delete_task(task_id)
            except ValueError:
                print("Invalid ID!")
        
        elif choice == '5':
            confirm = input("Are you sure? (yes/no): ").lower()
            if confirm == 'yes':
                todo.clear_all()
        
        elif choice == '6':
            print("Goodbye! 👋")
            break
        
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
