import pandas as pd

df = pd.read_csv('new_york_city.csv')

while True:

    get_raw = input('Would you like to see 5 lines of raw data?' ).lower()
    if get_raw == "yes":
        print(df.head(5))
    elif get_raw != 'yes':
        break
