class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def view_tasks(self):
        for i, task in enumerate(self.tasks, 1):
            print(f"{i}. {task}")

    def delete_task(self, task_number):
        try:
            self.tasks.pop(task_number - 1)
        except IndexError:
            print("Invalid task number.")

def main():
    todo_list = ToDoList()
    while True:
        print("\nTo-Do List")
        print("1. Add task")
        print("2. View tasks")
        print("3. Delete task")
        print("4. Quit")
        user_choice = int(input("Enter your choice: "))
        if user_choice == 1:
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif user_choice == 2:
            todo_list.view_tasks()
        elif user_choice == 3:
            task_number = int(input("Enter the task number: "))
            todo_list.delete_task(task_number)
        elif user_choice == 4:
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()