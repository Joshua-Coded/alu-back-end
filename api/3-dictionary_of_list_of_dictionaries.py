#!/usr/bin/python3
''' Test request to parse API's
'''


import csv
import json
import requests
import sys

if __name__ == "__main__":
    api_endpoint = "https://jsonplaceholder.typicode.com"

    def get_user_tasks(id):
        '''Return data for the user id passed as an argument
        '''
        user_id = str(id)
        user_data = requests.get(api_endpoint + "/users/" + user_id).json()
        username = user_data.get('username')
        todo_data = \
            requests.get(api_endpoint + "/users/" + user_id + "/todos").\
            json()
        tasks = []
        for task in todo_data:
            tasks.append({'username': username,
                          'task': task['title'],
                          'completed': task['completed']})
        data = {"{}".format(user_id): tasks}
        return data

    all_users = requests.get(api_endpoint + "/users").json()
    all_json = {}
    for user in all_users:
        user_data = get_user_tasks(user.get('id'))
        all_json.update(user_data)
    with open("todo_all_employees.json", 'w') as data_file:
        json.dump(all_json, data_file)
