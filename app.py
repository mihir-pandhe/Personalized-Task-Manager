import pickle

tasks = []


def add_task(description, priority=1):
    tasks.append({"description": description, "completed": False, "priority": priority})


def update_task(index, description=None, priority=None):
    if 0 <= index < len(tasks):
        if description:
            tasks[index]["description"] = description
        if priority is not None:
            tasks[index]["priority"] = priority
        print("Task updated successfully.")
    else:
        print("Invalid task number.")


def save_tasks(filename):
    with open(filename, "wb") as file:
        pickle.dump(tasks, file)
    print("Tasks saved successfully.")


def load_tasks(filename):
    global tasks
    try:
        with open(filename, "rb") as file:
            tasks = pickle.load(file)
        print("Tasks loaded successfully.")
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"Error loading tasks: {e}")


def list_tasks():
    if not tasks:
        print("No tasks available.")
    for index, task in enumerate(tasks):
        status = "Completed" if task["completed"] else "Pending"
        print(
            f"{index + 1}. {task['description']} - Priority: {task['priority']} - {status}"
        )


def main():
    while True:
        print("\n1. Add Task")
        print("2. Update Task")
        print("3. Save Tasks")
        print("4. Load Tasks")
        print("5. List Tasks")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            description = input("Enter task description: ")
            priority = int(input("Enter task priority (1-5): "))
            add_task(description, priority)
            print("Task added successfully.")
        elif choice == "2":
            index = int(input("Enter task number to update: ")) - 1
            description = input(
                "Enter new task description (leave blank to keep current): "
            )
            priority = input("Enter new task priority (leave blank to keep current): ")
            priority = int(priority) if priority else None
            update_task(index, description or None, priority)
        elif choice == "3":
            filename = input("Enter filename to save tasks: ")
            save_tasks(filename)
        elif choice == "4":
            filename = input("Enter filename to load tasks: ")
            load_tasks(filename)
        elif choice == "5":
            list_tasks()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
