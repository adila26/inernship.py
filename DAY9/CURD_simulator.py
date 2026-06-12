from typing import Dict, List
class TaskNotFoundError(Exception):
    pass
class TaskAlreadyExistsError(Exception):
    pass
class InvalidTaskDataError(Exception):
    pass
tasks: Dict[int, dict] = {}
next_id: int = 1
def get_all_tasks() -> List[dict]:
    return list(tasks.values())
def get_task(task_id: int) -> dict:
    if task_id not in tasks:
        raise TaskNotFoundError("Task not found.")
    return tasks[task_id]
def create_task(data: dict) -> dict:
    global next_id
    if "title" not in data:
        raise InvalidTaskDataError("Title is required.")
    task = {
        "id": next_id,
        "title": data["title"],
        "completed": data.get("completed", False)
    }
    tasks[next_id] = task
    next_id += 1
    return task
def update_task(task_id: int, data: dict) -> dict:
    if task_id not in tasks:
        raise TaskNotFoundError("Task not found.")
    tasks[task_id].update(data)
    return tasks[task_id]
def delete_task(task_id: int) -> bool:
    if task_id not in tasks:
        raise TaskNotFoundError("Task not found.")
    del tasks[task_id]
    return True
while True:
    print("\n=== TASK MANAGER ===")
    print("1. Create Task")
    print("2. View All Tasks")
    print("3. View One Task")
    print("4. Update Task")
    print("5. Delete Task")
    print("6. Exit")
    choice = input("Enter choice: ")
    try:
        if choice == "1":
            title = input("Enter title: ")
            task = create_task({"title": title})
            print("Created:", task)
        elif choice == "2":
            print(get_all_tasks())
        elif choice == "3":
            task_id = int(input("Enter task id: "))
            print(get_task(task_id))
        elif choice == "4":
            task_id = int(input("Enter task id: "))
            title = input("New title: ")
            updated = update_task(task_id, {"title": title})
            print("Updated:", updated)
        elif choice == "5":
            task_id = int(input("Enter task id: "))
            delete_task(task_id)
            print("Task deleted.")
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")
    except (
        TaskNotFoundError,
        TaskAlreadyExistsError,
        InvalidTaskDataError
    ) as e:
        print("Error:", e)
    except ValueError:
        print("Please enter a valid number.")