tasks = []

def add_task(description):
    tasks.append({"description": description, "completed": False})

def list_tasks():
    if not tasks:
        print("No tasks available.")
    for index, task in enumerate(tasks):
        status = "Completed" if task["completed"] else "Pending"
        print(f"{index + 1}. {task['description']} - {status}")

def main():
    while True:
        print("\n1. Add Task")
        print("2. List Tasks")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            description = input("Enter task description: ")
            add_task(description)
            print("Task added successfully.")
        elif choice == '2':
            list_tasks()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
