# -*- coding: utf-8 -*-

from os import stat

import models

from fastapi import FastAPI, status, HTTPException
from database import SessionLocal
from typing import List, Optional

# Код из validator.py
from pydantic import BaseModel, Field, ValidationError
from uuid import uuid4
from typing_extensions import Annotated


class Param(BaseModel):
    # param_1 (sid), param_2 (version)
    param_1: str
    param_2: int

    # class Config:
    #    orm_mode = True


# TODO: Подумать про orm_mode
class Task(BaseModel):
    task_uuid: Annotated[str, Field(default_factory=lambda: uuid4().hex)]
    description: str
    params: Param

    class Config:
        orm_mode = True


app = FastAPI()
db = SessionLocal()


@app.get('/', status_code=status.HTTP_200_OK)
def foo():
    return 'Hello from FastAPI!'


@app.get('/tasks', response_model=List[Task], status_code=status.HTTP_200_OK)
def get_tasks():

    all_tasks = db.query(models.Task).all()
    print('get_tasks: ', all_tasks)

    res = []
    for curr_task in all_tasks:
        elem = {
            "task_uuid": curr_task.task_uuid,
            "description": curr_task.description,
            "params": {
                "param_1": curr_task.param_1,
                "param_2": curr_task.param_2
            }
        }
        res.append(elem)

    return res


@app.post('/tasks/add', response_model=Task, status_code=status.HTTP_201_CREATED)
def create_task(task: Task):

    db_task = db.query(models.Task).filter(models.Task.task_uuid == task.task_uuid).first()

    if db_task is not None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Задача уже была добавлена ранее!")

    new_task = models.Task(
        task_uuid=task.task_uuid,
        description=task.description,
        param_1=task.params.param_1,
        param_2=task.params.param_2
    )

    db.add(new_task)
    db.commit()

    return task


# sid = 'S-1-5-21-500000003-1000000000-1000000003-1001'
#@app.put('/tasks/{task_sid}', response_model=Task, status_code=status.HTTP_200_OK)
#def update_task(task_sid: int, task):


@app.put('/tasks/{task_sid}', status_code=status.HTTP_204_NO_CONTENT)
def update_task(task_sid:str, task:Task):
    print('TASK_SID: ', task_sid)

    # Проверка на повторение uuid:
    db_task = db.query(models.Task).filter(models.Task.task_uuid == task.task_uuid).first()

    if db_task is not None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="В запросе повторяется uuid!")

    task_to_update = db.query(models.Task).filter(models.Task.param_1 == task_sid).order_by(models.Task.param_2.desc()).first()
    task_to_update.task_uuid = task.task_uuid
    task_to_update.description = task.description
    task_to_update.param_1 = task.params.param_1
    task_to_update.param_2 = task.params.param_2

    db.commit()
    #print(task)
    #res = ''

    #return res
