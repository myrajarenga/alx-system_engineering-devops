#!/usr/bin/python3
"""Script to fetch todos of all employees from an\
API and export to JSON format"""
import json
import requests


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users/"
    users = requests.get(url).json()
    todo_dict = {}

    for user in users:
        user_id = str(user.get("id"))
        username = user.get("username")
        todos = requests.get(f"{url}{user_id}/todos").json()
        todo_list = []
        for todo in todos:
            todo_dict_item = {
                "username": username,
                "task": todo.get("title"),
                "completed": todo.get("completed")
            }
            todo_list.append(todo_dict_item)
        todo_dict[user_id] = todo_list

    with open("todo_all_employees.json", "w") as f:
        json.dump(todo_dict, f)
