# -*- coding: utf-8 -*-

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

def parse_json(input_json):
    try:
        task = Task.parse_raw(input_json)
    except ValidationError as e:
        print(e.json())
    else:
        return task

if __name__ == '__main__':

    input_json = """
    {
        "task_uuid": "79bdcb3b9f20444f9e7cffcc46eb9448",
        "description": "Тестовая задача",
        "params": {
            "param_1": "1",
            "param_2": 1
        }
    }
    """

    task = parse_json(input_json)
    print(task)

    uuid4 = uuid4()
    print(uuid4)

