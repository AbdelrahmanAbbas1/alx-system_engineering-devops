#!/usr/bin/python3
"""This Script retreives data using REST API"""
import json
import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]
    user_url = f'https://jsonplaceholder.typicode.com/users/{user_id}'
    todo_url = f'https://jsonplaceholder.typicode.com/users/{user_id}/todos'

    users = requests.get(user_url)
    todos = requests.get(todo_url)

    user = users.json()
    todo = todos.json()

    tasks_list = []
    for task in todo:
        tasks_list.append({
            'task': task['title'],
            'completed': task['completed'],
            'username': user['username'],
            })

    with open(f'{user_id}.json', 'w') as json_file:
        json.dump({user_id: tasks_list}, json_file)
