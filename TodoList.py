# Initialize an empty to-do list
todo_list = []

# Function to add a task to the to-do list
def add_task():
    task = input("Enter a task: ")
    todo_list.append(task)
    print(f"Task '{task}' has been added to the to-do list.")

# Function to view the to-do list
def view_tasks():
    if not todo_list:
        print("Your to-do list is empty.")
    else:
        print("To-Do List:")
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {task}")

# Function to remove a task from the to-do list
def remove_task():
    view_tasks()
    if not todo_list:
        return
    
    try:
        task_number = int(input("Enter the number of the task you want to remove: "))
        if task_number < 1 or task_number > len(todo_list):
            print("Invalid task number.")
        else:
            removed_task = todo_list.pop(task_number - 1)
            print(f"Task '{removed_task}' has been removed from the to-do list.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")

# Main loop
while True:
    print("\nOptions:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Remove a task")
    print("4. Quit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        remove_task()
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")
