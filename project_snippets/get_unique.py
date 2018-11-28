import pandas as pd
import numpy as np
df = pd.read_csv('new_york_city.csv')

#unique_users = df['User Type'].unique()
users = df['User Type']
subscriber_count = 0
customer_count = 0
unkown_count = 0

for user in users:
    if user == "Subscriber":
        subscriber_count += 1
    elif user == "Customer":
        customer_count += 1
    elif user not in ("Subscriber", "Customer"):
        unkown_count += 1

print(subscriber_count)
print(customer_count)
print(unkown_count)

#subscriber_count = user_types.str.count('Subscriber')
#customer_count = user_types.str.count('Customer')
