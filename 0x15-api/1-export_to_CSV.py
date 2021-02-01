#!/usr/bin/python3
""" a Python script that, using this REST API, for a given employee ID,
 returns information about his/her TODO list progress.
"""

import csv
import requests
from sys import argv


if __name__ == '__main__':

    filename = argv[1] + ".csv"
    id = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1]))
    req = requests.get('https://jsonplaceholder.typicode.com/todos/')
    name = (id.json().get('name'))
    with open(filename, "w") as f:
        r_json = req.json()
        for i in r_json:
            if i.get('userId') == int(argv[1]):
                w = csv.writer(f, quoting=csv.QUOTE_ALL)
                w.writerow([i.get('userId'), name,
                           i.get('completed'), i.get('title')])
