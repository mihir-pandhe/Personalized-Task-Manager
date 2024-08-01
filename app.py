tasks = []


def add_task(description):
    tasks.append({"description": description, "completed": False})


def delete_task(index):
    if 0 <= index < len(tasks):
        tasks.pop(index)
        print("Task deleted successfully.")
    else:
        print("Invalid task number.")


def mark_task_completed(index):
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
        print("Task marked as completed.")
    else:
        print("Invalid task number.")


def list_tasks():
    if not tasks:
        print("No tasks available.")
    for index, task in enumerate(tasks):
        status = "Completed" if task["completed"] else "Pending"
        print(f"{index + 1}. {task['description']} - {status}")


def main():
    while True:
        print("\n1. Add Task")
        print("2. Delete Task")
        print("3. Mark Task Completed")
        print("4. List Tasks")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            description = input("Enter task description: ")
            add_task(description)
            print("Task added successfully.")
        elif choice == "2":
            index = int(input("Enter task number to delete: ")) - 1
            delete_task(index)
        elif choice == "3":
            index = int(input("Enter task number to mark as completed: ")) - 1
            mark_task_completed(index)
        elif choice == "4":
            list_tasks()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
