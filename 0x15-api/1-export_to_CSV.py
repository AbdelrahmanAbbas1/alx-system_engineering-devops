#!/usr/bin/python3
"""This script gathers data using REST API"""
import csv
import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(
                employee_id)
    r = requests.get(user_url)
    employee_name = r.json().get('username')
    todo_url = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(
                employee_id)
    r = requests.get(todo_url)
    tasks = r.json()
    with open(f'{employee_id}.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)
        for task in tasks:
            writer.writerow([employee_id,
                             employee_name, task['completed'], task['title']])
