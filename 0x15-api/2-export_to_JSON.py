#!/usr/bin/python3
"""a Python script that, using this REST API, for a given employee ID,\
returns information about his/her todo list progress."""

import json
import requests
import sys


if __name__ == '__main__':

    completed_tasks = 0
    total_tasks = 0
    title = []
    id = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(sys.argv[1]))
    req = requests.get('https://jsonplaceholder.typicode.com/todos/')
    name = (id.json().get('name'))
    username = (id.json().get("username"))
    r_json = req.json()
    for i in r_json:
        if i.get('userId') == int(sys.argv[1]):
            if i.get('completed') is True:
                title.append(i.get('title'))
                completed_tasks += 1
            total_tasks += 1
    print("Employee {} is done with tasks({}/{}):"
          .format(name, completed_tasks, total_tasks))
    for i in title:
        print("\t {}".format(i))
    req = requests.get(
        'https://jsonplaceholder.typicode.com/users/' +
        (sys.argv[1]) + '/todos')
    new_d = {}
    with open("{}.json".format(sys.argv[1]), "w") as file:
        r_json = req.json()
        d = [{'task': i.get('title'), 'completed': i.get('completed'),
              'username': name}for i in r_json]
        new_d[sys.argv[1]] = d
        json.dump(new_d, file)
