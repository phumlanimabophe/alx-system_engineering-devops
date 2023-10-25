#!/usr/bin/python3
"""Python script to export data in JSON format."""
import json
import requests
from sys import argv

if __name__ == "__main__":
    # Base URL for the JSONPlaceholder API
    url = "https://jsonplaceholder.typicode.com/"

    # Get user information for the provided user ID
    user = requests.get(url + "users/{}".format(argv[1])).json()
    username = user.get("username")

    # Get TODO list for the user
    todos = requests.get(url + "todos", params={"userId": argv[1]).json()

    # Create and write the JSON file with user's TODO list information
    with open("{}.json".format(argv[1]), "w") as jsonfile:
        json.dump({argv[1]: [{
            "task": to.get("title"),
            "completed": to.get("completed"),
            "username": username
            } for to in todos
            ]}, jsonfile)
