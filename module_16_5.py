from fastapi import FastAPI, status, Body, HTTPException, Request, Form
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

users_db = []
messages_db = []

class UserModel(BaseModel):
    id: int = None
    username: str
    age: int = None


@app.get("/")
def display_users(request: Request):
    return templates.TemplateResponse("users.html", {"request": request, "users": users_db})


@app.get("/users/{user_id}")
def display_user(request: Request, user_id: int):
    try:
        selected_user = [user for user in users_db if user.id == user_id][0]
        return templates.TemplateResponse("users.html", {"request": request, "user": selected_user})
    except IndexError:
        raise HTTPException(status_code=404, detail="User not found")


@app.post("/create_user")
def create_user(request: Request, username: str = Form(...), age: int = Form(...)):
    new_user_id = len(users_db) + 1
    new_user = UserModel(id=new_user_id, username=username, age=age)
    users_db.append(new_user)
    return templates.TemplateResponse("users.html", {"request": request, "users": users_db})

#все что ниже - не изменялось поскольку в ДЗ не вошло.
@app.put("message/{message_id}")
def update_message(message_id: int, message: str = Body()) -> str:
    try:
        edit_message = messages_db[message_id]
        edit_message.text = message
        return f"Message updated!"
    except IndexError:
        raise HTTPException(status_code=404, detail="Message not found")


@app.delete("/message/{message_id}")
def delete_message(message_id: int) -> str:
    try:
        messages_db.pop(message_id)
        return f"Message ID={message_id} deleted!"
    except IndexError:
        raise HTTPException(status_code=404, detail="Message not found")


@app.delete("/")
def kill_message_all() -> str:
    messages_db.clear()
    return "All messages deleted!"