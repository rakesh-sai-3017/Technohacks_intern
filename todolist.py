class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        print(f"Task '{task}' added.")

    def update_task(self, index, new_task):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["task"] = new_task
            print(f"Task {index + 1} updated to '{new_task}'.")
        else:
            print("Invalid task index.")

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            removed_task = self.tasks.pop(index)
            print(f"Task '{removed_task['task']}' deleted.")
        else:
            print("Invalid task index.")

    def mark_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["completed"] = True
            print(f"Task {index + 1} marked as completed.")
        else:
            print("Invalid task index.")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            for idx, task in enumerate(self.tasks, 1):
                status = "Done" if task["completed"] else "Not Done"
                print(f"{idx}. {task['task']} - {status}")


def main():
    todo = ToDoList()
    
    while True:
        print("\nToDo List Menu:")
        print("1. Add Task")
        print("2. Update Task")
        print("3. Delete Task")
        print("4. Mark Task as Completed")
        print("5. List Tasks")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            task = input("Enter task: ")
            todo.add_task(task)

        elif choice == '2':
            index = int(input("Enter task number to update: ")) - 1
            new_task = input("Enter new task description: ")
            todo.update_task(index, new_task)

        elif choice == '3':
            index = int(input("Enter task number to delete: ")) - 1
            todo.delete_task(index)

        elif choice == '4':
            index = int(input("Enter task number to mark as completed: ")) - 1
            todo.mark_completed(index)

        elif choice == '5':
            todo.list_tasks()

        elif choice == '6':
            print("Exiting ToDo List. Goodbye!")
            break

        else:
            print("Invalid choice. Please select from 1 to 6.")

if __name__ == "__main__":
    main()
