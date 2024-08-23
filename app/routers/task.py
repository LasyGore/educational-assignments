from fastapi import APIRouter

router = APIRouter(prefix="/task", tags=["task"])


@router.get("/")
async def all_tasks():
    pass

@router.get("/task_id")
async def task_by_id():
    pass

@router.post ("/create_task")
async def create_task():
    pass

@router.put ("/update_task")
async def update_task():
    pass

@router.put ("/delete_task")
async def delete_task():
    pass