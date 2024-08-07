from fastapi import FastAPI
import uvicorn

app=FastAPI()

@app.get("/")
async def welcome() -> dict:
    return {"message": "Главная страница."}

#Частное всегда должно быть выше!
@app.get("/user/admin")
async def news() -> dict:
    return {"message": f"Внимание! Вы вошли как администратор!"}


@app.get("/user/{user_id}")
async def id_user(user_id: str) -> dict:
    return {"message": f"Внимание! Вы вошли как пользователь - {user_id}." }

#@app.get("/user/{user_name}/{age}")
#async def qnews(user_name: str, age: str) -> dict:
#    return {"message": f"Информация о пользователе: имя - {user_name}, возраст: {age}."}

@app.get("/suser")
async def suser(user_name: str, age: int) -> dict:
    return {"Информация о пользователе. Имя:": user_name, "Возраст:" : age}

#http://127.0.0.1:8000/suser?user_name=Lasygore&age=54


#@app.get("/id")
#async def id_paginator(username: str = 'Igor', age: int = 54) -> dict:
#    return {"User": username, "Age": age}

#@app.get("/user/{first_name}/{last_name}")
#async def news(first_name: str, last_name: str) -> dict:
#    return {"message": f"Hello,{first_name} {last_name}"}

#@app.get("/main")
#async def welcome() -> dict:
#    return {"message": "Main page."}


# Get - адрес в строке ?переменная=значение
# Post - оформить заказ в магазине
# Put - обновить
# Delete - удалить
# Path -
# python -m uvicorn main_1:app -- запуск веб сервиса