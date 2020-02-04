#!/usr/bin/python3
import csv
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
    name = users.get('name')
    count = 0
    done = 0
    list_t = []

    for i in todo:
        if i.get('completed') is True:
            done += 1
            list_t.append(i.get('title'))
        count += 1
    print('Employee {} is done with tasks({}/{}):'.format(name, done, count))
    for title in list_t:
        print("\t {}".format(title))

    with open('{}.csv'.format(argv[1]), 'w') as file:
        o_file = csv.writer(file, quoting=csv.QUOTE_ALL)
        for i in todo:
            o_file.writerow([argv[1], users.get('username'),
                             i.get('completed'), i.get('title')])
