import json

class Task:
    def __init__(self, title, description, status="Pending"):
        self.title = title
        self.description = description
        self.status = status

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description):
        task = Task(title, description)
        self.tasks.append(task)

    def delete_task(self, title):
        for task in self.tasks:
            if task.title == title:
                self.tasks.remove(task)
                print(f"Task '{title}' deleted successfully.")
                return
        print(f"Task '{title}' not found.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            for idx, task in enumerate(self.tasks, start=1):
                print(f"{idx}. Title: {task.title}, Description: {task.description}, Status: {task.status}")

    def save_tasks(self, filename):
        with open(filename, 'w') as f:
            tasks_data = [vars(task) for task in self.tasks]
            json.dump(tasks_data, f)
        print("Tasks saved successfully.")

    def load_tasks(self, filename):
        try:
            with open(filename, 'r') as f:
                tasks_data = json.load(f)
                self.tasks = [Task(task['title'], task['description'], task['status']) for task in tasks_data]
            print("Tasks loaded successfully.")
        except FileNotFoundError:
            print("File not found.")

def main():
    todo_list = ToDoList()

    while True:
        print("\n===== To-Do List Menu =====")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. View Tasks")
        print("4. Save Tasks")
        print("5. Load Tasks")
        print("6. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            todo_list.add_task(title, description)
        elif choice == '2':
            title = input("Enter title of task to delete: ")
            todo_list.delete_task(title)
        elif choice == '3':
            print("\n===== Tasks =====")
            todo_list.view_tasks()
        elif choice == '4':
            filename = input("Enter filename to save tasks: ")
            todo_list.save_tasks(filename)
        elif choice == '5':
            filename = input("Enter filename to load tasks: ")
            todo_list.load_tasks(filename)
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
