#!/usr/bin/python3
"""
getting data using api
"""
import requests
import sys

if __name__ == "__main__":
    employee_Id = int(sys.argv[1])

    todo_url = "https://jsonplaceholder.typicode.com/todos"
    user_data_url = "https://jsonplaceholder.typicode.com/users"

    user_response = requests.get(user_data_url)
    todo_response = requests.get(todo_url)
    # if todo_response.status_code & user_response.status_code == 200:
    todos = todo_response.json()
    users = user_response.json()
    for user in users:
        if user.get("id") == employee_Id:
            employee_name = user.get("name")
    # filter completed tasks
    done = []
    total = 0
    completed = 0
    for todo in todos:
        if todo.get("userId") == employee_Id:
            total += 1
            if todo.get("completed"):
                completed += 1
                done.append(todo.get("title"))
    # Display the progress information
    print(f"Employee {employee_name} is done with tasks({completed}/{total}):")
    for _ in done:
        print(f"\t {_}")
