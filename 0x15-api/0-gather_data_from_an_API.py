#!/usr/bin/python3
"""Write a Python script that, using this REST API,
   for a given employee ID, returns information about
   his/her TODO list progress.
"""
import requests
from sys import argv
if __name__ == "__main__":
    url_todos = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'.format(argv[1])).json()
    url_user = requests.get("https://jsonplaceholder.typicode.com/users/{}".format(argv[1])).json()
    url_todos_true = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}&completed=true'.format(argv[1])).json()
    name_user = url_user.get('name')
    number_done = len(url_todos)
    total_number = len(url_todos_true)
    print("Employee {} is done with task({}/{}):"
          .format(name_user, total_number, number_done))
    for task in url_todos_true:
        name_task = task.get('title')
        print("\t{}".format(name_task))
