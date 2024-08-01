import pickle

tasks = []


def add_task(description, priority=1, category="General"):
    tasks.append(
        {
            "description": description,
            "completed": False,
            "priority": priority,
            "category": category,
        }
    )


def update_task(index, description=None, priority=None, category=None):
    if 0 <= index < len(tasks):
        if description:
            tasks[index]["description"] = description
        if priority is not None:
            tasks[index]["priority"] = priority
        if category:
            tasks[index]["category"] = category
        print("Task updated successfully.")
    else:
        print("Invalid task number.")


def delete_task(index):
    if 0 <= index < len(tasks):
        tasks.pop(index)
        print("Task deleted successfully.")
    else:
        print("Invalid task number.")


def search_tasks(keyword):
    found = False
    for index, task in enumerate(tasks):
        if keyword.lower() in task["description"].lower():
            status = "Completed" if task["completed"] else "Pending"
            print(
                f"{index + 1}. {task['description']} - Priority: {task['priority']} - Category: {task['category']} - {status}"
            )
            found = True
    if not found:
        print("No tasks found.")


def list_tasks(filter_status=None, filter_category=None):
    if not tasks:
        print("No tasks available.")
    for index, task in enumerate(tasks):
        status = "Completed" if task["completed"] else "Pending"
        if filter_status and status != filter_status:
            continue
        if filter_category and task["category"] != filter_category:
            continue
        print(
            f"{index + 1}. {task['description']} - Priority: {task['priority']} - Category: {task['category']} - {status}"
        )


def save_tasks():
    filename = input("Enter filename to save tasks: ")
    try:
        with open(filename, "wb") as file:
            pickle.dump(tasks, file)
        print("Tasks saved successfully.")
    except Exception as e:
        print(f"Error saving tasks: {e}")


def load_tasks():
    filename = input("Enter filename to load tasks: ")
    global tasks
    try:
        with open(filename, "rb") as file:
            tasks = pickle.load(file)
        print("Tasks loaded successfully.")
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"Error loading tasks: {e}")


def main():
    while True:
        print("\n1. Add Task")
        print("2. Update Task")
        print("3. Delete Task")
        print("4. Search Tasks")
        print("5. List Tasks")
        print("6. Save Tasks")
        print("7. Load Tasks")
        print("8. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            description = input("Enter task description: ")
            priority = int(input("Enter task priority (1-5): "))
            category = input("Enter task category (General, Work, Personal): ")
            add_task(description, priority, category)
            print("Task added successfully.")
        elif choice == "2":
            index = int(input("Enter task number to update: ")) - 1
            description = input(
                "Enter new task description (leave blank to keep current): "
            )
            priority = input("Enter new task priority (leave blank to keep current): ")
            category = input("Enter new task category (leave blank to keep current): ")
            priority = int(priority) if priority else None
            update_task(index, description or None, priority, category or None)
        elif choice == "3":
            index = int(input("Enter task number to delete: ")) - 1
            delete_task(index)
        elif choice == "4":
            keyword = input("Enter keyword to search for: ")
            search_tasks(keyword)
        elif choice == "5":
            filter_status = input(
                "Filter by status (Completed/Pending) or leave blank: "
            )
            filter_category = input(
                "Filter by category (General, Work, Personal) or leave blank: "
            )
            list_tasks(
                filter_status if filter_status else None,
                filter_category if filter_category else None,
            )
        elif choice == "6":
            save_tasks()
        elif choice == "7":
            load_tasks()
        elif choice == "8":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
