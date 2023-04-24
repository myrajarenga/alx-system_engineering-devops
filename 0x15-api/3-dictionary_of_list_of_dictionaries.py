#!/usr/bin/python3
"""script to fetch todos of all employees from an\
API and export to JSON format.
The script fetches todos of all users from the JSONPlaceholder API and exports
them to a JSON file in the format:

{
    "USER_ID": [
        {
            "username": "USERNAME",
            "task": "TASK_TITLE",
            "completed": TASK_COMPLETED_STATUS
        },
        ...
    ],
    ...
}

The JSON file is saved with the name "todo_all_employees.json".
"""

import json
import requests


if __name__ == "__main__":
    # Base URL for the JSONPlaceholder API
    url = "https://jsonplaceholder.typicode.com/users/"

    # Fetch all users from the API
    users = requests.get(url).json()

    # Dictionary to store todos of all users
    todo_dict = {}

    # Loop through each user and fetch their todos
    for user in users:
        user_id = str(user.get("id"))
        username = user.get("username")
        todos = requests.get(f"{url}{user_id}/todos").json()
        todo_list = []

        # Loop through each todo of the user and store it in a dictionary
        for todo in todos:
            todo_dict_item = {
                "username": username,
                "task": todo.get("title"),
                "completed": todo.get("completed")
            }
            todo_list.append(todo_dict_item)

        # Store the list of todos of the user in the todo_dict
        todo_dict[user_id] = todo_list

    # Write the todo_dict to a JSON file
    with open("todo_all_employees.json", "w") as f:
        json.dump(todo_dict, f)
