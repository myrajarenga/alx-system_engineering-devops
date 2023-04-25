#!/usr/bin/python3
""" Fetch JSON data from an API and converts it to a dictionary"""

import json
import requests

if __name__ == "__main__":
    # URL of the API endpoint
    api_url = "https://jsonplaceholder.typicode.com/users"

    # List of user IDs to fetch tasks for
    user_ids = ["1", "2", "3"]

    # Loop through each user ID in the list
    for user_id in user_ids:
        # Get the tasks for the current user
        user_tasks_url = f"{api_url}/{user_id}/todos"
        user_tasks = requests.get(user_tasks_url).json()

        # Initialize an empty list to store the tasks for this user
        user_task_list = []

        # Loop through each task for this user
        for task in user_tasks:
            task_title = task.get("title")
            task_completed = task.get("completed")

            # Create a dictionary to represent the task for this user
            task_dict = {
                "user_id": user_id,
                "task": task_title,
                "completed": task_completed
            }

            # Add the task dictionary to the list of tasks for this user
            user_task_list.append(task_dict)

        # Create a dictionary to represent the tasks for this user
        user_dict = {
            user_id: user_task_list
        }

        # Write the user's tasks to a JSON file
        with open(f"{user_id}.json", "w") as f:
            json.dump(user_dict, f)
