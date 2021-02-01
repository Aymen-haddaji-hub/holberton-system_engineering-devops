#!/usr/bin/python3
"""a Python script that, using this REST API, for a given employee ID,\
returns information about his/her todo list progress."""

import json
import requests
import sys


if __name__ == "__main__":

    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                         .format(sys.argv[1])).json()
    todos = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}"
                         .format(sys.argv[1])).json()

    with open("{}.json".format(sys.argv[1]), "w") as user_id:
            json.dump({sys.argv[1]: [{
                'task': task.get('title'),
                'completed': task.get('completed'),
                'username': users.get('username')
            } for task in todos]}, user_id)
