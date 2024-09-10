from fastapi import APIRouter, Depends, status, HTTPException
# Сессия БД
from sqlalchemy.orm import Session
# Функция подключения к БД
from app.backend.db_depends import get_db
# Аннотации, Модели БД и Pydantic.
from typing import Annotated
from app.models import User
from app.models import Task
from app.schemas import *
# Функции работы с записями.
from sqlalchemy import insert, select, update, delete
# Функция создания slug-строки
from slugify import slugify

router = APIRouter(prefix="/task", tags=["task"])


@router.get("/")
async def all_tasks(db: Annotated[Session, Depends(get_db)]):
    tasks = db.execute(select(Task)).scalars().all()
    return tasks


@router.get("/{task_id}")
async def task_by_id(task_id: int, db: Annotated[Session, Depends(get_db)]):
    task = db.execute(select(Task).where(Task.id == task_id)).scalar_one_or_none()
    if task is None:
        raise HTTPException(status_code=404, detail="User was not found")
    return task


@router.post("/create")
async def create_task(user_id: int, task: CreateTask, db: Annotated[Session, Depends(get_db)]):
    user = db.execute(select(User).where(User.id == user_id)).scalar_one_or_none()
    if user is None:
        raise HTTPException(status_code=404, detail="Пользователь не найден")

    new_task = Task(**task.dict(), user_id=user_id)
    db.execute(insert(Task).values(new_task))
    db.commit()

    return {'status_code': status.HTTP_201_CREATED, 'transaction': 'Успешно'}


@router.put("/update/{task_id}")
async def update_task(task_id: int, task: UpdateTask, db: Annotated[Session, Depends(get_db)]):
    existing_task = db.execute(select(Task).where(Task.id == task_id)).scalar_one_or_none()
    if existing_task is None:
        raise HTTPException(status_code=404, detail="Задача не найдена")

    for key, value in task.dict(exclude_unset=True).items():
        setattr(existing_task, key, value)

    db.commit()
    return {'status_code': status.HTTP_200_OK, 'transaction': 'Обновление задачи успешно!'}


@router.delete("/delete/{task_id}")
async def delete_task(task_id: int, db: Annotated[Session, Depends(get_db)]):
    task = db.execute(select(Task).where(Task.id == task_id)).scalar_one_or_none()
    if task is None:
        raise HTTPException(status_code=404, detail="Задача не найдена")

    db.execute(delete(Task).where(Task.id == task_id))
    db.commit()
    return {'status_code': status.HTTP_200_OK, 'transaction': 'Задача успешно удалена!'}



#@router.get("/")
#async def all_tasks():
#    pass

#@router.get("/task_id")
#async def task_by_id():
#    pass

#@router.post ("/create_task")
#async def create_task():
#    pass

#@router.put ("/update_task")
#async def update_task():
#    pass

#@router.put ("/delete_task")
#async def delete_task():
#    pass