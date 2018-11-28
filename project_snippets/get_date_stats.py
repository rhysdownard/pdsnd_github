import pandas as pd
import numpy as np
import datetime as dt

df = pd.read_csv('new_york_city.csv')

common_hour = df['Start Time'].dt.hour.mode()[0]
print(common_hour)

#df["Time Hour"]= df['Start Time'].str.split(' ', n = 1, expand = True)[1]
#split_time = df["Time Hour"].str.split(':', n = 1, expand = True)[0]
#common_hour = split_time.mode()
#time_index = pd.Series.dt.time(time_day)
#hour = time_day.str.split(':')
#df['datetime'].dt.time
#DatetimeIndex
#df[['h','m','s']] = time_day.astype(str).str.split(':', expand=True).astype(int)
#hour = df[['h','m','s']][0]
#print(type(split_time))
#print(split_time.shape)
#print(type(df[['h','m','s']]))
#split_time = time_day.str.split(':').mode()[0]
#first_hour = split_time
#df["Date"]= time_day[0]
#time = time_day[1]
#df["Hour of day"] = time_day[1]
#day_split = df["Hour of day"].str.split(':')[0]
#print(split_time)
#print(type(time_day))
#sorted_hour = df["Hour of day"].sort_values(ascending=True)
#common_start = df["Hour of day"].iloc()[0]
#print('The most common start hour is: {}'.format(common_start))
#print(sorted_hour)
#print(type(df["Hour of day"]))
