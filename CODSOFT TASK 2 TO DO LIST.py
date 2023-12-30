import os

def display_menu():
    print("\n===== To-Do List =====")
    print("1. View tasks")
    print("2. Add task")
    print("3. Mark task as done")
    print("4. Remove task")
    print("5. Exit")

def view_tasks():
    with open("tasks.txt", "r") as file:
        tasks = file.readlines()
        if tasks:
            print("\n===== Your Tasks =====")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task.strip()}")
        else:
            print("\nNo tasks yet.")

def add_task():
    task = input("\nEnter the task: ")
    with open("tasks.txt", "a") as file:
        file.write(task + "\n")
    print("Task added successfully!")

def mark_task_as_done():
    view_tasks()
    try:
        task_number = int(input("\nEnter the task number to mark as done: "))
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
        if 1 <= task_number <= len(tasks):
            tasks[task_number - 1] = tasks[task_number - 1].replace('\n', '') + " - Done\n"
            with open("tasks.txt", "w") as file:
                file.writelines(tasks)
            print("Task marked as done!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def remove_task():
    view_tasks()
    try:
        task_number = int(input("\nEnter the task number to remove: "))
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
        if 1 <= task_number <= len(tasks):
            del tasks[task_number - 1]
            with open("tasks.txt", "w") as file:
                file.writelines(tasks)
            print("Task removed successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-5): ")

        if choice == "1":
            view_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            mark_task_as_done()
        elif choice == "4":
            remove_task()
        elif choice == "5":
            print("Exiting the To-Do List application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    if not os.path.exists("tasks.txt"):
        with open("tasks.txt", "w"):
            pass  # Create an empty file if it doesn't exist
    main()
