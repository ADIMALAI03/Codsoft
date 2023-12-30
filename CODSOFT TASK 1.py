import json
from datetime import datetime

def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = []
    return tasks

def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)

def display_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return

    print("To-Do List:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task['title']} - {task['date']}")

def add_task(tasks, title):
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    tasks.append({"title": title, "date": date})
    save_tasks(tasks)
    print("Task added successfully!")

def remove_task(tasks, index):
    try:
        removed_task = tasks.pop(index - 1)
        save_tasks(tasks)
        print(f"Task removed successfully: {removed_task['title']}")
    except IndexError:
        print("Invalid task index.")

def main():
    tasks = load_tasks()

    while True:
        print("\n1. Display Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            title = input("Enter the task title: ")
            add_task(tasks, title)
        elif choice == "3":
            display_tasks(tasks)
            index = int(input("Enter the task index to remove: "))
            remove_task(tasks, index)
        elif choice == "4":
            print("Exiting the To-Do List application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
