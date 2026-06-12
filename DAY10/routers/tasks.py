from fastapi import APIRouter, HTTPException
from schemas import TaskCreate, TaskUpdate, TaskResponse
router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)
tasks = {}
next_id = 1
@router.get("/", response_model=list[TaskResponse])
def get_all_tasks():
    return list(tasks.values())
@router.get("/{task_id}", response_model=TaskResponse)
def get_task(task_id: int):
    if task_id not in tasks:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )
    return tasks[task_id]
@router.post("/", response_model=TaskResponse)
def create_task(task: TaskCreate):
    global next_id
    new_task = {
        "id": next_id,
        "title": task.title,
        "description": task.description,
        "completed": False
    }
    tasks[next_id] = new_task
    next_id += 1
    return new_task
@router.put("/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, task: TaskUpdate):
    if task_id not in tasks:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )
    tasks[task_id] = {
        "id": task_id,
        "title": task.title,
        "description": task.description,
        "completed": task.completed
    }
    return tasks[task_id]
@router.delete("/{task_id}")
def delete_task(task_id: int):
    if task_id not in tasks:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )
    del tasks[task_id]
    return {"message": "Task deleted"}
@router.patch("/{task_id}/complete")
def complete_task(task_id: int):
    if task_id not in tasks:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )
    tasks[task_id]["completed"] = True
    return tasks[task_id]