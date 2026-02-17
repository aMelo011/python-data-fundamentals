import sqlite3
import csv

def save_to_db():
    conn = sqlite3.connect('data/users.db')
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        email TEXT NOT NULL)''')

    with open('data/users_export.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            cursor.execute('INSERT INTO users (name, email) VALUES (?, ?)', 
                        (row[0], row[1]))

    conn.commit()
    conn.close()
    print("Data loaded to database successfully!")

if __name__ == '__main__':
    save_to_db()