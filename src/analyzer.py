import pandas as pd

df = pd.read_csv('data/users_export.csv')

#print(df)

#emails = df['Email']
#print(emails)

#df.info()

df['Name'] = df['Name'].str.upper()
#print(df)

#biz_users = df['Email'].str.contains('.biz')
biz_users = df[df['Email'].str.contains('.biz')]
print(biz_users)

biz_users.to_csv('data/biz_users.csv', index = False)
