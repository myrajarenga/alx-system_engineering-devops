#!/usr/bin/python3
""" Fetch data from API and converts it into   a dictionary"""
import json
import requests
import sys

if __name__ == "__main__":
    # Check if the user ID is provided as input
    if len(sys.argv) < 2:
        print("Please provide a user ID as input parameter.")
        sys.exit(1)

    # Get the user ID from the input parameter
    user_id = sys.argv[1]

    # URL of the API endpoint for the specified user
    api_url = "https://jsonplaceholder.typicode.com/users/{}/todos"\
    .format(user_id)

    # Get data in JSON format from the API
    todos = requests.get(api_url).json()

    # Initialize an empty list to store the tasks data for the current user
    tasks_list = []

    # Loop through each task item for the current user
    for task in todos:
        # Extract the title and completed status for the task item
        task_title = task.get("title")
        task_completed = task.get("completed")

        # Create a dictionary to store the task item data
        task_dict = {
            "user_id": user_id,
            "task": task_title,
            "completed": task_completed
        }

        # Add the task item data to the tasks list for the current user
        tasks_list.append(task_dict)

    # Write the tasks data for the current user to a JSON file
    output_file = "{}.json".format(user_id)
    with open(output_file, 'w') as f:
        json.dump(tasks_list, f)
