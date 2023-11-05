#!/usr/bin/python3
''' Test request to parse API's
'''
import csv
import json
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        api_endpoint = "https://jsonplaceholder.typicode.com"
        user_id = sys.argv[1]
        user_data = requests.get(api_endpoint + "/users/" + user_id).json()
        username = user_data.get('username')
        todo_data = \
            requests.get(api_endpoint + "/users/" + user_id + "/todos").\
            json()
        with open("{}.json".format(user_id), 'w') as json_file:
            tasks = []
            for task in todo_data:
                tasks.append({'task': task['title'],
                              'completed': task['completed'],
                              'username': username})
            data = {"{}".format(user_id): tasks}
            json.dump(data, json_file)
