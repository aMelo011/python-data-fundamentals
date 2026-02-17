import csv
import requests

url = 'https://jsonplaceholder.typicode.com/users'
response = requests.get(url)
users = response.json()

with open('data/users_export.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Email'])
    for user in users:
        writer.writerow([user['name'], user['email']])