from fastapi import FastAPI, Path
import uvicorn
from typing import Annotated

app=FastAPI()


@app.get("/user/{userid}")
async def users(userid: int = Path(ge=1, le=100, description="Enter User ID", example='33')) -> dict:
    return {"message": f"Hello,{userid}"}

@app.get("/user/{username}/{age}")
async def news(username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', example="ClausBB")], age: int = Path(ge=18, le=120, description="Enter age", example='24')) -> dict:
    return {"message": f"Hello,{username} {age}"}

@app.get("/")
async def welcome() -> dict:
    return {"message": "Hello World!!!"}