import sqlite3
import plotext as plt

def draw_chart():
    conn = sqlite3.connect('data/users.db')
    cursor = conn.cursor()
    cursor.execute('SELECT name FROM users LIMIT 5')
    rows = cursor.fetchall()
    conn.close()

    names = [row[0] for row in rows]
    # Ficticious score
    scores = [85, 42, 90, 55, 73]

    plt.bar(names, scores)
    plt.title("User Activity Dashboard")
    plt.theme('pro')
    plt.show()

if __name__ == '__main__':
    draw_chart()