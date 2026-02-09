import json
import os

TODO_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(TODO_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def add_task(tasks, description):
    tasks.append({"description": description, "done": False})
    save_tasks(tasks)
    print(f"Added: {description}")

def list_tasks(tasks):
    if not tasks:
        print("No tasks.")
    else:
        for i, task in enumerate(tasks):
            status = "✓" if task["done"] else "✗"
            print(f"{i}. [{status}] {task['description']}")

def delete_task(tasks, index):
    try:
        removed = tasks.pop(index)
        save_tasks(tasks)
        print(f"Deleted: {removed['description']}")
    except IndexError:
        print("Invalid task number.")

def mark_done(tasks, index):
    try:
        tasks[index]["done"] = True
        save_tasks(tasks)
        print(f"Marked as done: {tasks[index]['description']}")
    except IndexError:
        print("Invalid task number.")

def main():
    tasks = load_tasks()
    print("Welcome to CLI Todo App")
    print("Type 'add <task>', 'list', 'delete <index>', 'done <index>', or 'exit'")

    while True:
        command = input("\n> ").strip().split()
        if not command:
            continue

        if command[0] == "add" and len(command) > 1:
            desc = " ".join(command[1:])
            add_task(tasks, desc)
        elif command[0] == "list":
            list_tasks(tasks)
        elif command[0] == "delete" and len(command) > 1:
            try:
                idx = int(command[1])
                delete_task(tasks, idx)
            except ValueError:
                print("Please enter a valid number.")
        elif command[0] == "done" and len(command) > 1:
            try:
                idx = int(command[1])
                mark_done(tasks, idx)
            except ValueError:
                print("Please enter a valid number.")
        elif command[0] == "exit":
            print("Goodbye!")
            break
        else:
            print("Unknown command. Try: add <task>, list, delete <index>, done <index>, exit")

if __name__ == "__main__":
    main()