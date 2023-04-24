#!/usr/bin/python3
"""script to send get request to a url and extract data"""

if __name__ == '__main__':
    import requests
    from sys import argv

    employee_id = argv[1]
    total_todos = 0
    done_todos = 0
    done_todo_titles = []

    result = requests.get('https://jsonplaceholder.typicode\
.com/users/' + employee_id)
    employee_name = result.json().get('name')

    result = requests.get('https://jsonplaceholder.typicode\
.com/users/' + employee_id + '/todos')
    employee_todos = result.json()

    for item in employee_todos:
        total_todos += 1
        if item.get('completed') is True:
            done_todos += 1
            done_todo_titles.append(item.get('title'))

    print('Employee {} is done with tasks({}/{}):'.format(
        employee_name,
        done_todos,
        total_todos
    ))

    for title in done_todo_titles:
        print('\t ' + title)
