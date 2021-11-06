# -*- coding: utf-8 -*-

import requests


if __name__ == '__main__':

    import json

    task_1 = """
    {
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


    # Выводим список задач:
    res = requests.get('http://127.0.0.1:8000/tasks')
    print('/tasks: ', res.content)


    # Добавляем новую задачу и возвращаем результат:
    #res = requests.post('http://127.0.0.1:8000/tasks/add', json=task_1)
    #print('/tasks/add: ', res.content)

    #res = requests.get('http://127.0.0.1:8000/tasks')
    #print('/tasks: ', res.content)


    # Изменяем существующую запись и выводим результат:
    task_desc = """
        {
            "task_uuid": "125673ecbfb44be8856341e34af82ea8",
            "description": "new_text_2",
            "params": {
                "param_1": "1",
                "param_2": 1
            }
        }
        """

    task_desc = json.loads(task_desc)

    #res = requests.put('http://127.0.0.1:8000/tasks/1', json=task_desc)
    #print('/tasks/<task_sid> :', res.content)

    res = requests.get('http://127.0.0.1:8000/tasks')
    print('/tasks: ', res.content)