from fastapi import FastAPI
from starlette.responses import JSONResponse
from app.routers import task, user
import logging
import json
from app.schemas import *

app = FastAPI()

@app.get("/")
async def welcome():
    return {"message": "Welcome to Taskmanager"}


@app.exception_handler(Exception)
async def exception_handler(request, exc):
    logging.error(f"Error occurred: {exc}")
    return JSONResponse(status_code=500, content={"message": "An error occurred."})

app.include_router(task.router)
app.include_router(user.router)


