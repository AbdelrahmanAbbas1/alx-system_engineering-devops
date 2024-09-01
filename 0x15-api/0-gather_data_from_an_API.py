#!/usr/bin/python3
"""This script gathers data using REST API"""
import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(
                employee_id)
    r = requests.get(user_url)
    employee_name = r.json().get('name')
    todo_url = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(
                employee_id)
    r = requests.get(todo_url)
    tasks = r.json()
    total_tasks = len(tasks)
    done_tasks = 0
    tasks_names = []
    for task in tasks:
        if task.get('completed') is True:
            done_tasks += 1
            tasks_names.append(task.get('title'))
    print('Employee {} is done with tasks({}/{})'.format(
          employee_name, done_tasks, total_tasks))
    for task in tasks_names:
        print('\t', task)
