# -*- coding: utf-8 -*-

import requests


if __name__ == '__main__':

    task_1 = """
        {
            "task_uuid": "79bdcb3b9f20444f9e7cffcc46eb9448",
            "description": "Test desc_1",
            "params": {
            "param_1": "1",
            "param_2": 1
        }
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

    requests.post('http://127.0.0.1:8000/tasks/add', data=task_1)
    #print(res.content)

    res = requests.get('http://127.0.0.1:8000/tasks')
    print('/tasks: ', res.content)