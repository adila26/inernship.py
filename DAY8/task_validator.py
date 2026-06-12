from pydantic import BaseModel, ValidationError, EmailStr
from typing import Optional
import json
import requests
class UserModel(BaseModel):
    name: str
    email: EmailStr
    age: int
class TaskModel(BaseModel):
    title: str
    description: Optional[str] = None
    priority: str
    completed: bool = False
def create_task(data: dict) -> TaskModel:
    return TaskModel(**data)
def tasks_to_json(tasks: list[TaskModel]) -> str:
    return json.dumps(
        [task.model_dump() for task in tasks],
        indent=4
    )
class TodoModel(BaseModel):
    userId: int
    id: int
    title: str
    completed: bool
tasks = []
task_data = {
    "title": "Learn FastAPI",
    "description": "Build APIs with FastAPI",
    "priority": "High"
}
invalid_task = {
    "description": "Missing title",
    "priority": "Low"
}
for data in [task_data, invalid_task]:
    try:
        task = create_task(data)
        tasks.append(task)
        print("Task Created:", task)
    except ValidationError as e:
        print("Validation Error:")
        for error in e.errors():
            print(error["msg"])
print("\nJSON Output:")
print(tasks_to_json(tasks))
try:
    response = requests.get(
        "https://jsonplaceholder.typicode.com/todos/1"
    )
    response.raise_for_status()
    todo = TodoModel(**response.json())
    print("\nAPI Data Parsed Into Pydantic Model:")
    print(todo)
except requests.RequestException as e:
    print("API Request Error:", e)
except ValidationError as e:
    print("Validation Error:")
    for error in e.errors():
        print(error["msg"])