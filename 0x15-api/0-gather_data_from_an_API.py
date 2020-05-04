#!/usr/bin/python3
""" Write a Python script that, using
    this REST API, for a given employee
    ID, returns information about his/her
    TODO list progress.
"""
from urllib import urllib
from request import request
from sys import argv

def given_employee(id_employee):
    """ using this REST API, for a given
        employee ID
    """
    dic_json = get("https://jsonplaceholder.typicode.com/users".format(id_employee)).json()
    name_employee = json["name"]
    number_of_done_task = 0
    total_number_of_task = 0
    task=[]
    for arg in get("")

