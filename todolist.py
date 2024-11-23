import os

def display_menu():
    """Display the menu options."""
    print("\nTo-Do List Menu:")
    print("1. View tasks")
    print("2. Add a task")
    print("3. Update a task")
    print("4. Delete a task")
    print("5. Save tasks to file")
    print("6. Load tasks from file")
    print("7. Exit")

def view_tasks(tasks):
    """Display all tasks."""
    if not tasks:
        print("Your to-do list is empty.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def add_task(tasks):
    """Add a new task."""
    task = input("Enter a new task: ").strip()
    if task:
        tasks.append(task)
        print(f"Task '{task}' added.")
    else:
        print("Task cannot be empty.")

def update_task(tasks):
    """Update an existing task."""
    view_tasks(tasks)
    try:
        index = int(input("Enter the task number to update: ")) - 1
        if 0 <= index < len(tasks):
            new_task = input("Enter the updated task: ").strip()
            if new_task:
                print(f"Task '{tasks[index]}' updated to '{new_task}'.")
                tasks[index] = new_task
            else:
                print("Task cannot be empty.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def delete_task(tasks):
    """Delete a task."""
    view_tasks(tasks)
    try:
        index = int(input("Enter the task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            print(f"Task '{tasks[index]}' deleted.")
            tasks.pop(index)
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def save_tasks(tasks, filename="tasks.txt"):
    """Save tasks to a file."""
    with open(filename, "w") as file:
        for task in tasks:
            file.write(task + "\n")
    print(f"Tasks saved to {filename}.")

def load_tasks(filename="tasks.txt"):
    """Load tasks from a file."""
    if os.path.exists(filename):
        with open(filename, "r") as file:
            tasks = [line.strip() for line in file.readlines()]
        print(f"Tasks loaded from {filename}.")
    else:
        print(f"No file found at {filename}. Starting with an empty list.")
        tasks = []
    return tasks

def main():
    tasks = []
    print("Welcome to the To-Do List Manager!")
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-7): ").strip()
        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            update_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            save_tasks(tasks)
        elif choice == '6':
            tasks = load_tasks()
        elif choice == '7':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
