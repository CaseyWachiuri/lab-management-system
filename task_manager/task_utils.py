from datetime import datetime

from task_manager.validation import validate_task_title, validate_task_description, validate_due_date

tasks = []

def add_task(title, description, due_date):
    if not validate_task_title(title):
        print("Invalid title!")
        return
    if not validate_task_description(description):
        print("Invalid description!")
        return
    if not validate_due_date(due_date):
        print("Invalid due date!")
        return
    task = {
        "title": title,
        "description": description,
        "due_date": due_date,
        "completed": False
    }
    tasks.append(task)
    print("Task added successfully!")
    
def mark_task_as_complete(index, tasks=tasks):
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
        print("Task marked as complete!")
    else:
        print("Invalid task index!")
    
def view_pending_tasks(tasks=tasks):
    pending = [t for t in tasks if not t["completed"]]
    if not pending:
        print("No pending tasks.")
    else:
        for i, t in enumerate(tasks):
            status = "✓" if t["completed"] else " "
            print(f"[{status}] {i}. {t['title']} - Due: {t['due_date']}")

def calculate_progress(tasks=tasks):
    if not tasks:
        return 0
    completed_count = sum(1 for t in tasks if t["completed"])
    progress = int((completed_count / len(tasks)) * 100)
    return progress
