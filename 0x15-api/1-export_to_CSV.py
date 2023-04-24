#!/usr/bin/python3
"""Fetch JSON data from an API and export to CSV file.

Usage: python3 export_to_csv.py <user_id>
"""

import csv
import requests
from sys import argv


def export_to_csv():
    """
    Fetches the todo list data for a given user ID and exports it to a CSV file.
    """

    # Parse user ID from command line argument
    user_id = argv[1]

    # Fetch user data from API
    user_url = "https://jsonplaceholder.typicode.com/users/" + user_id
    user_data = requests.get(user_url).json()

    # Extract username from user data
    username = user_data.get("username")

    # Fetch todo list data for user from API
    todo_url = "{}/todos".format(user_url)
    todo_data = requests.get(todo_url).json()

    # Define output file name
    file_name = "{}.csv".format(user_id)

    # Export todo list data to CSV file
    with open(file_name, 'w') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

        for item in todo_data:
            writer.writerow([
                item.get("userId"),
                username,
                item.get("completed"),
                item.get("title")
            ])


if __name__ == '__main__':
    export_to_csv()
