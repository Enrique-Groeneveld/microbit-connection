import json
import os

def add_task():
    task_name = input("Enter the task name: ")
    task_time = ""
    while len(task_time) != 5 or task_time[2] != ":":
        task_time = input("Enter the time it needs to be completed 'hh:mm' format: ")

    if os.path.exists("tasks.json"):
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
    else:
        tasks = {}

    tasks[task_time] = task_name

    with open("tasks.json", "w") as file:
        json.dump(tasks, file)
    print("Task added successfully.")

def list_tasks():
    if os.path.exists("tasks.json"):
        with open("tasks.json", "r") as file:
            print("\nTasks:")
            tasks = json.load(file)
            for time, task in tasks.items():
                print(f"Task: {task}, Time: {time}")
            print("\n")
    else:
        print("No tasks found.")

def main():
    while True:
        print("1. Add a task")
        print("2. List tasks")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()