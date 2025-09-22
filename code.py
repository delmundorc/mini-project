tasks = []

def add_task(task):
    if task.strip() == "":
        print(" Task cannot be empty!")
    else:
        tasks.append(task)
        print(" Task added!")

def show_tasks():
    if not tasks:
        print(" No tasks yet.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
        print()

def remove_task(task_number):
    if 1 <= task_number <= len(tasks):
        removed = tasks.pop(task_number - 1)
        print(f" Removed: {removed}")
    else:
        print("Invalid task number!")

def main():
    while True:
        print("\n--- TO DO LIST ---")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Remove Task")
        print("4. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == "1":
            t = input("Enter task: ")
            add_task(t)
        elif choice == "2":
            show_tasks()
        elif choice == "3":
            try:
                n = int(input("Enter task number to remove: "))
                remove_task(n)
            except ValueError:
                print(" Please enter a valid number!")
        elif choice == "4":
            print(" Exiting To-Do List. Goodbye!")
            break
        else:
            print(" Wrong choice!")

main()
