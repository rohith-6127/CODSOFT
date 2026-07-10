import json
import os
from datetime import datetime

FILE_NAME = "tasks.json"

# ANSI Colors
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
CYAN = "\033[96m"
MAGENTA = "\033[95m"
RESET = "\033[0m"


# ---------------------- FILE FUNCTIONS ----------------------

def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []


def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


tasks = load_tasks()


# ---------------------- DISPLAY ----------------------

def display_tasks():
    if not tasks:
        print(RED + "\nNo tasks available.\n" + RESET)
        return

    print("\n" + "=" * 90)
    print(f"{'ID':<5}{'Task':<30}{'Priority':<12}{'Due Date':<15}{'Status'}")
    print("=" * 90)

    for i, task in enumerate(tasks, start=1):
        status = GREEN + "Completed" + RESET if task["completed"] else YELLOW + "Pending" + RESET

        print(f"{i:<5}{task['title']:<30}{task['priority']:<12}{task['due']:<15}{status}")

    print("=" * 90)


# ---------------------- ADD TASK ----------------------

def add_task():
    title = input("Enter Task : ")

    while True:
        priority = input("Priority (High/Medium/Low): ").capitalize()
        if priority in ["High", "Medium", "Low"]:
            break
        print("Invalid Priority!")

    while True:
        due = input("Due Date (DD-MM-YYYY): ")
        try:
            datetime.strptime(due, "%d-%m-%Y")
            break
        except:
            print("Invalid Date Format!")

    task = {
        "title": title,
        "priority": priority,
        "due": due,
        "completed": False
    }

    tasks.append(task)
    save_tasks(tasks)

    print(GREEN + "\nTask Added Successfully!\n" + RESET)


# ---------------------- UPDATE ----------------------

def update_task():
    display_tasks()

    if not tasks:
        return

    try:
        index = int(input("Enter Task ID to Update: ")) - 1

        if index not in range(len(tasks)):
            print("Invalid ID")
            return

        title = input("New Task Name: ")

        priority = input("Priority (High/Medium/Low): ").capitalize()

        due = input("Due Date (DD-MM-YYYY): ")

        tasks[index]["title"] = title
        tasks[index]["priority"] = priority
        tasks[index]["due"] = due

        save_tasks(tasks)

        print(GREEN + "Task Updated Successfully!" + RESET)

    except:
        print("Invalid Input")


# ---------------------- DELETE ----------------------

def delete_task():
    display_tasks()

    if not tasks:
        return

    try:
        index = int(input("Enter Task ID to Delete: ")) - 1

        if index not in range(len(tasks)):
            print("Invalid ID")
            return

        removed = tasks.pop(index)

        save_tasks(tasks)

        print(RED + f"{removed['title']} Deleted Successfully!" + RESET)

    except:
        print("Invalid Input")


# ---------------------- COMPLETE ----------------------

def mark_completed():
    display_tasks()

    if not tasks:
        return

    try:
        index = int(input("Enter Task ID Completed: ")) - 1

        if index not in range(len(tasks)):
            print("Invalid ID")
            return

        tasks[index]["completed"] = True

        save_tasks(tasks)

        print(GREEN + "Task Marked Completed!" + RESET)

    except:
        print("Invalid Input")


# ---------------------- SEARCH ----------------------

def search_task():
    keyword = input("Enter Keyword: ").lower()

    found = False

    print()

    for i, task in enumerate(tasks, start=1):
        if keyword in task["title"].lower():
            found = True

            status = "Completed" if task["completed"] else "Pending"

            print(f"""
Task ID : {i}
Task    : {task['title']}
Priority: {task['priority']}
Due     : {task['due']}
Status  : {status}
""")

    if not found:
        print(RED + "No Matching Task Found!" + RESET)


# ---------------------- STATISTICS ----------------------

def statistics():

    total = len(tasks)

    completed = len([t for t in tasks if t["completed"]])

    pending = total - completed

    high = len([t for t in tasks if t["priority"] == "High"])

    medium = len([t for t in tasks if t["priority"] == "Medium"])

    low = len([t for t in tasks if t["priority"] == "Low"])

    print("\n========= TASK REPORT =========")
    print("Total Tasks      :", total)
    print("Completed Tasks  :", completed)
    print("Pending Tasks    :", pending)
    print("High Priority    :", high)
    print("Medium Priority  :", medium)
    print("Low Priority     :", low)
    print("===============================\n")


# ---------------------- SORT ----------------------

def sort_tasks():

    order = {
        "High": 1,
        "Medium": 2,
        "Low": 3
    }

    tasks.sort(key=lambda x: order[x["priority"]])

    save_tasks(tasks)

    print(GREEN + "Tasks Sorted by Priority!" + RESET)

    display_tasks()


# ---------------------- CLEAR ----------------------

def clear_completed():
    global tasks

    tasks = [task for task in tasks if not task["completed"]]

    save_tasks(tasks)

    print(GREEN + "Completed Tasks Removed!" + RESET)


# ---------------------- MAIN ----------------------

while True:

    print(CYAN)
    print("=" * 45)
    print("      TO-DO LIST MANAGER")
    print("=" * 45)
    print(RESET)

    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Task Completed")
    print("6. Search Task")
    print("7. Task Statistics")
    print("8. Sort by Priority")
    print("9. Remove Completed Tasks")
    print("10. Exit")

    choice = input("\nEnter Choice: ")

    if choice == "1":
        add_task()

    elif choice == "2":
        display_tasks()

    elif choice == "3":
        update_task()

    elif choice == "4":
        delete_task()

    elif choice == "5":
        mark_completed()

    elif choice == "6":
        search_task()

    elif choice == "7":
        statistics()

    elif choice == "8":
        sort_tasks()

    elif choice == "9":
        clear_completed()

    elif choice == "10":
        save_tasks(tasks)

        print(GREEN + "\nThank You for this Using Advanced To-Do List Manager!" + RESET)

        break

    else:
        print(RED + "Invalid Choice! Try Again." + RESET)
