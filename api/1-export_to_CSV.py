#!/usr/bin/python3
''' Test request to parse API's
'''
import csv
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
        with open("{}.csv".format(user_id), 'w') as csv_file:
            for task in todo_data:
                csv_file.write('"{}","{}","{}","{}"\n'.format(
                    user_id,
                    username,
                    task.get('completed'),
                    task.get('title')
                ))
