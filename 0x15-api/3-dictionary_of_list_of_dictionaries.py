#!/usr/bin/python3
import json
import requests

if __name__ == '__main__':
    todo = \
        requests.get('https://jsonplaceholder.typicode.com/todos')
    users = \
        requests.get('https://jsonplaceholder.typicode.com/users/')

    todo = todo.json()
    users = users.json()
    all_employees = {}

    for user in users:
        u_id = user.get('id')
        name = user.get('username')
        list_t = []
        for i in todo:
            if i.get('userId') == u_id:
                list_t.append({
                    "username": name,
                    "task": i.get('title'),
                    "completed": i.get('completed')
                })
        all_employees[str(u_id)] = list_t

    with open('todo_all_employees.json', 'w') as file:
        file.write(json.dumps(all_employees)+'\n')
