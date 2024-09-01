#!/usr/bin/python3
"""This script gathers data using REST API"""
import requests
import sys


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/users/2'
    r = requests.get(url)
    r.json()
