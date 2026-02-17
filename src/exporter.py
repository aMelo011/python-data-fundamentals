import csv
import requests

def fetch_users():
    url = 'https://jsonplaceholder.typicode.com/users'
    response = requests.get(url)
    users = response.json()

    with open('data/users_export.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Email'])
        for user in users:
            writer.writerow([user['name'], user['email']])

    print("Data extracted successfully!")
    
if __name__ == '__main__':
    fetch_users()