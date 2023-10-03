# Define an empty list to store tasks
tasks = []

# Function to add a task to the list
def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added successfully!")

# Function to view all tasks
def view_tasks():
    if not tasks:
        print("No tasks found.")
    else:
        print("Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

# Function to mark a task as completed
def mark_completed():
    view_tasks()
    try:
        task_index = int(input("Enter the number of the task to mark as completed: ")) - 1
        if 0 <= task_index < len(tasks):
            print(f"Marking '{tasks[task_index]}' as completed.")
            tasks.pop(task_index)
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# Main program loop
while True:
    print("\nMenu:")
    print("1. Add a Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Exit")
    
    choice = input("Enter your choice (1/2/3/4): ")
    
    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        mark_completed()
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please try again.")
