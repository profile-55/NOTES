# -*- coding: utf-8 -*-

import requests


if __name__ == '__main__':

    import json

    task_1 = """
    {
        "task_uuid": "79bdcb3b9f20444f9e7cffcc46eb9455",
        "description": "34125125",
        "params": {
            "param_1": "1",
            "param_2": 1
        }
    }
    """

    task_1 = json.loads(task_1)
    print(task_1)

    task_3 = """
            {
                "task_uuid": "79bdcb3b9f20444f9e7cffcc46eb9449",
                "description": "Test desc_1",
           
                "param_1": "1",
                "param_2": 1
            
            }
        """

    task_2 = """
        {
            "description": "Тестовая задача",
            "params": {
                "param_1": "1",
                "param_2": 1
            }
        }
        """

    res = requests.get('http://127.0.0.1:8000')
    print(res.content)

    res = requests.get('http://127.0.0.1:8000/tasks')
    print('/tasks: ', res.content)

    res = requests.post('http://127.0.0.1:8000/tasks/add', json=task_1)
    print(res.content)

    res = requests.get('http://127.0.0.1:8000/tasks')
    print('/tasks: ', res.content)