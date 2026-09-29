from datetime import datetime, timedelta

# Import validation functions
from task_manager.validation import validate_task_title, validate_task_description, validate_due_date

# Define tasks list
tasks = []

# Implement add_task function
def add_task(title, description, due_date):
    if validate_task_title(title) and validate_task_description(description) and validate_due_date(due_date):
        tasks.append({"title": title, "description": description, "due_date": due_date, "completed": False})
        print("Task added successfully!")
    
# Implement mark_task_as_complete function
def mark_task_as_complete(index, tasks=tasks):
    if index < 1 or index > len(tasks):
        raise ValueError("Invalid task index.")

    tasks[index - 1]["completed"] = True
    print("Task marked as complete!")
    
# Implement view_pending_tasks function
def view_pending_tasks(tasks=tasks):
    for task in tasks:
        if task["completed"] == False:
            print(task)

# Implement calculate_progress function
def calculate_progress(tasks=tasks):
    completed_tasks = 0
    for task in tasks:
        if task["completed"] == True:
            completed_tasks += 1

    total_tasks = len(tasks)
    if total_tasks == 0:
        return 0

    progress = (completed_tasks / total_tasks) * 100
    return progress