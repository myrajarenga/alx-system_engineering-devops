#!/usr/bin/python3
""" Fetch JSON data from an API and converts it to a dictionary"""

import json
import requests


if __name__ == "__main__":
    # URL of the API endpoint
    api_url = "https://jsonplaceholder.typicode.com/users/"

    # Get data in JSON format from the API
    users = requests.get(api_url).json()

    # Name of the output file
    output_file = "2.json"

    # Initialize an empty dictionary to store the data
    user_data_dict = {}

    # Loop through each user in the API data
    for user in users:
        # Extract the username and user ID
        username = user.get("username")
        user_id = str(user.get("id"))

        # Get the todos data for the current user
        todos_url = "{}{}/todos".format(api_url, user_id)
        user_todos = requests.get(todos_url).json()

        # Initialize an empty list to store the todos data for the current user
        todos_list = []

        # Loop through each todo item for the current user
        for todo in user_todos:
            # Extract the title and completed status for the todo item
            todo_title = todo.get("title")
            todo_completed = todo.get("completed")

            # Create a dictionary to store the todo item data
            todo_dict = {
                "username": username,
                "task": todo_title,
                "completed": todo_completed
            }

            # Add the todo item data to the todos list for the current user
            todos_list.append(todo_dict)

        # Add the todos data for the current user to the user data dictionary
        user_data_dict[user_id] = todos_list

    # Write the user data dictionary to a JSON file
    with open(output_file, 'w') as f:
        json.dump(user_data_dict, f)
