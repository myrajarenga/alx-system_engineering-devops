#!/usr/bin/env python3
"""
This script retrieves a user's to-do list from the\
 JSONPlaceholder API and writes it to a CSV file.

Usage: python3 todo_to_csv.py [user_id]
"""
import csv
import requests


def export_csv():
    """
    Export todo list data for all users to a CSV file.
    """
    users = requests.get("https://jsonplaceholder.typicode.com/users").json()
    todos = requests.get("https://jsonplaceholder.typicode.com/todos").json()

    with open("todo_all_employees.csv", "w") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

        for user in users:
            userId = user.get("id")
            userName = user.get("username")

            for todo in todos:
                if userId == todo.get("userId"):
                    writer.writerow([
                        userId,
                        userName,
                        todo.get("completed"),
                        todo.get("title")
                    ])
