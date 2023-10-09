tasks = []

class Task:
    def __init__(self, title, completed=False):
        self.title = title
        self.completed = completed

def add_task(title):
    tasks.append(Task(title))

def list_tasks():
    for i, task in enumerate(tasks, start=1):
        status = "[X]" if task.completed else "[ ]"
        print(f"{i}. {status} {task.title}")

def complete_task(task_index):
    tasks[task_index - 1].completed = True

def remove_task(task_index):
    del tasks[task_index - 1]

while True:
    print("\nTo-Do List:")
    list_tasks()
    print("\nMenu:")
    print("1. Add Task")
    print("2. Complete Task")
    print("3. Remove Task")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        title = input("Enter task title: ")
        add_task(title)
    elif choice == "2":
        task_index = int(input("Enter the task number to complete: "))
        complete_task(task_index)
    elif choice == "3":
        task_index = int(input("Enter the task number to remove: "))
        remove_task(task_index)
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please try again.")