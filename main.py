from os import stat

from fastapi import FastAPI,status,HTTPException
from typing import Optional,List
from database import SessionLocal
import models

#
from pydantic import BaseModel, Field, ValidationError
from uuid import uuid4
from typing_extensions import Annotated

class Param(BaseModel):
    param_1: str
    param_2: int

class Task(BaseModel):
    task_uuid: Annotated[str, Field(default_factory=lambda: uuid4().hex)]
    description: str
    params: Param

    class Config:
        orm_mode=True


app=FastAPI()
db=SessionLocal()

@app.get('/tasks',response_model=List[Task], status_code=200)
def get_tasks():
    tasks=db.query(models.Task).all()

    return tasks

#@app.get('/item/{item_id}',response_model=Item,status_code=status.HTTP_200_OK)
#def get_an_item(item_id:int):
#    item=db.query(models.Item).filter(models.Item.id==item_id).first()
#    return item


@app.post('/tasks/add',response_model=Task, status_code=status.HTTP_201_CREATED)
def create_task(task:Task):
    db_item=db.query(models.Item).filter(models.Item.name==task.task_uuid).first()

    if db_item is not None:
        raise HTTPException(status_code=400, detail="Task already exists")

    new_task = models.Task(
        task_uuid = task.task_uuid,
        description=task.description,
        param_1=task.param_1,
        param_2=task.param_2
    )

    db.add(new_task)
    db.commit()

    return new_task

sid = 'S-1-5-21-500000003-1000000000-1000000003-1001'

@app.put('/tasks/{task_sid}', response_model=Task, status_code=status.HTTP_200_OK)
def update_task(task_sid:int, task:Task):
    task_to_update = db.query(models.Item).filter(models.Item.id==task_sid).first()
    task_to_update.name=task.task_uuid
    task_to_update.price=task.description
    task_to_update.description=task.param_1
    task_to_update.on_offer=task.param_2

    db.commit()

    return task_to_update

@app.delete('/item/{item_id}')
def delete_item(item_id:int):
    item_to_delete=db.query(models.Item).filter(models.Item.id==item_id).first()

    if item_to_delete is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Resource Not Found")
    
    db.delete(item_to_delete)
    db.commit()

    return item_to_delete