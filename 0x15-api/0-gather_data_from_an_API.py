#!/usr/bin/python3
"""Write a Python script that, using this REST API,
   for a given employee ID, returns information about
   his/her TODO list progress.
"""
import requests
from sys import argv
if __name__ == "__main__":
    todos = 'https://jsonplaceholder.typicode.com/todos?userId={}'
    url_todos = requests.get(todos.format(argv[1])).json()
    user = 'https://jsonplaceholder.typicode.com/users/{}'
    url_user = requests.get(user.format(argv[1])).json()
    lt = 'https://jsonplaceholder.typicode.com/todos?userId={}&completed=true'
    true = requests.get(lt.format(argv[1])).json()
    name_user = url_user.get('name')
    number_done = len(url_todos)
    total_number = len(true)
    print("Employee {} is done with task({}/{}):"
          .format(name_user, total_number, number_done))
    for task in true:
        name_task = task.get('title')
        print("\t{}".format(name_task))
