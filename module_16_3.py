from fastapi import FastAPI, Path, HTTPException
import uvicorn
from typing import Annotated

app=FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}


@app.get("/users")
async def get_users() -> dict:
    return users


@app.post("/users/{username}/{age}")
async def create_user(username: Annotated[str, Path(min_length=4, max_length=18, description='Enter username'
        , example="IvanovII")], age: int = Path(ge=18, le=120, description="Enter age", example='24')):
        user_id = str(len(users) + 1)
        users[user_id] = f"Имя: {username}, возраст: {age}"
        return f"User {user_id} is registered"


@app.put("/users/{user_id}/{username}/{age}")
async def update_user(user_id: Annotated[str,Path(min_length=1, max_length=3, description='Enter user_id', example="2")]
    , username: Annotated[str, Path(min_length=4, max_length=18, description='Enter username', example="IvanovII")]
    , age: int = Path(ge=18, le=120, description="Enter age", example='24')):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="Пользователь не найден")

    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"The user {user_id} is updated"


@app.delete("/users/{user_id}")
async def delete_user(user_id: Annotated[str, Path(min_length=1, max_length=3, description='Enter user_id', example="2")]):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="Пользователь не найден")

    del users[user_id]
    return f"The user {user_id} is deleted"

