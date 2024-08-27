from fastapi import FastAPI
from TestPythonProject_66_70_23_08.Zadanie_1.app.routers import task, user

app = FastAPI()

@app.get("/")
async def welcome():
    return {"message": "Welcome to Taskmanager"}

app.include_router(task.router)
app.include_router(user.router)


