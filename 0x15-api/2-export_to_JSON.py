#!/usr/bin/python3
import json
import requests
from sys import argv

if __name__ == '__main__':
    todo = \
        requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                     .format(argv[1]))
    users = \
        requests.get('https://jsonplaceholder.typicode.com/users/{}'
                     .format(argv[1]))

    todo = todo.json()
    users = users.json()
    name = users.get('username')
    list_t = []

    for i in todo:
        list_t.append({"task": i.get('title'),
                       "completed": i.get('completed'),
                       "username": name})

    with open('{}.json'.format(argv[1]), 'w') as file:
        file.write(json.dumps({argv[1]: list_t}))
