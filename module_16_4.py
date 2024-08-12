from fastapi import FastAPI, Path, Body, HTTPException
from pydantic import BaseModel
import uvicorn
from typing import List

app=FastAPI()


class User(BaseModel):
    id: int
    username: str
    age: int

users = []


@app.get("/users", response_model=List[User])
async def get_users() -> List[User]:
    return users


@app.post("/user/{username}/{age}", response_model=User)
async def create_user(username: str, age: int):
    user_id = 1 if not users else max(user.id for user in users) + 1
    user = User(id=user_id, username=username, age=age)
    users.append(user)
    return user


@app.put("/user/{user_id}/{username}/{age}", response_model=User)
async def update_user(user_id: int, username: str, age: int):
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return user
    raise HTTPException(status_code=404, detail="User was not found")


@app.delete("/user/{user_id}", response_model=User)
async def delete_user(user_id: int):
    for user in users:
        if user.id == user_id:
            users.remove(user)
            return user
    raise HTTPException(status_code=404, detail="User was not found")