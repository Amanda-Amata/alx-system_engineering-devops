#!/usr/bin/python3
"""Python script to export data in the JSON format."""

import csv
import json
import requests
import sys


if __name__ == '__main__':
    USER_ID = sys.argv[1]
    url_user = 'https://jsonplaceholder.typicode.com/users/' + USER_ID
    request = requests.get(url_user)
    """defining surname"""
    USERNAME = request.json().get('username')
    """defining tasks in json"""
    url_task = url_user + '/todos'
    request = requests.get(url_task)
    tasks = request.json()

    dict_data = {USER_ID: []}
    for task in tasks:
        TASK_COMPLETED_STATUS = task.get('completed')
        TASK_TITLE = task.get('title')
        dict_data[USER_ID].append({
                                  "task": TASK_TITLE,
                                  "completed": TASK_COMPLETED_STATUS,
                                  "username": USERNAME})
    """print(dict_data)"""
    with open('{}.json'.format(USER_ID), 'w') as f:
        json.dump(dict_data, f)
