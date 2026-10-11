
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Literal

app = FastAPI(
    title="Smart Task Management API",
    description="A task management API built with Python and FastAPI",
    version="1.0.0"
)

class TaskCreate(BaseModel):
    title: str = Field(min_length=1, max_length=150)
    description: str = ""
    status: Literal["pending", "in_progress", "completed"] = "pending"
    priority: Literal["low", "medium", "high"] = "medium"

tasks = {}
next_id = 1

@app.get("/")
def home():
    return {"message": "Smart Task Management API is running"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/tasks", status_code=201)
def create_task(task: TaskCreate):
    global next_id
    new_task = {"id": next_id, **task.model_dump()}
    tasks[next_id] = new_task
    next_id += 1
    return new_task

@app.get("/tasks")
def get_tasks(status: str | None = None):
    results = list(tasks.values())
    if status:
        results = [task for task in results if task["status"] == status]
    return results

@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    return tasks[task_id]

@app.put("/tasks/{task_id}")
def update_task(task_id: int, updated: TaskCreate):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    tasks[task_id] = {"id": task_id, **updated.model_dump()}
    return tasks[task_id]

@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    del tasks[task_id]
    return None
