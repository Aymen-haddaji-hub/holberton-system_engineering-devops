#!/usr/bin/python3
"""a Python script that, using this REST API, for a given employee ID,\
returns information about his/her todo list progress."""

import csv
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

    with open("{}.csv".format(sys.argv[1]), "w") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in req.json():
            writer.writerow([sys.argv[1], username,
                            task.get("completed"), task.get("title")])
