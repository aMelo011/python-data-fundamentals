import pandas as pd

def process_data():
    df = pd.read_csv('data/users_export.csv')
    biz_users = df[df['Email'].str.contains('.biz')]
    biz_users.to_csv('data/biz_users.csv', index = False)
    print("Data processed and filtered successfully!")

if __name__ == '__main__':
    process_data()