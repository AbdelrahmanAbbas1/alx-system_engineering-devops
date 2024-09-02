#!/usr/bin/python3
"""This Script retreives data using REST API"""
import json
import requests


if __name__ == "__main__":
    user_url = f'https://jsonplaceholder.typicode.com/users'
    todo_url = f'https://jsonplaceholder.typicode.com/todos'

    response_users = requests.get(user_url)
    response_todos = requests.get(todo_url)

    users = response_users.json()
    todos = response_todos.json()

    users_dict = {}
    tasks_list = []
    for user in users:
        for task in todos:
            if user['id'] == task['userId']:
                tasks_list.append({
                    'username': user['username'],
                    'task': task['title'],
                    'completed': task['completed']
                    })
        users_dict[user['id']] = tasks_list
        tasks_list = []

    with open(f'todo_all_employees.json', 'w') as json_file:
        json.dump(users_dict, json_file)
