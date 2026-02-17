import sqlite3
import csv

conn = sqlite3.connect('data/users.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL)''')

#with open('data/users_export.csv', 'r') as file:
#    reader = csv.reader(file)
#    next(reader)
#    for row in reader:
#        cursor.execute('INSERT INTO users (name, email) VALUES (?, ?)', 
#                       (row[0], row[1]))

conn.commit()

cursor.execute('''SELECT * FROM users
                  WHERE email LIKE '%.biz' ''')
rows = cursor.fetchall()
for row in rows:
    print(row)

conn.close()