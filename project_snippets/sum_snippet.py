import pandas as pd
import numpy as np
import math

df = pd.read_csv('new_york_city.csv')
#print(df['Trip Duration'])
total_trip = df['Trip Duration'].sum()

minutes = int(math.floor(total_trip / 60))
hours = int(math.floor(total_trip / 3600))
days = int(math.floor(total_trip / 86400))
years = int(math.floor(total_trip / 31536000))
days_by_hours = int(math.floor(hours % 24))
print(minutes)
print(hours)
print(days)
print(years)
print(days_by_hours)

def TimeConvert(num):

  # to get the hours, we divide num by 60 and round it down
  # e.g. 61 / 60 = 1 hour
  # e.g. 43 / 60 = 0 hours

    hours = int(math.floor(num / 3600))

  # to get the minutes, now we use the remainder that we discarded above
  # the modulo operation is represented by the % symbol
  # e.g. 61 % 60 = 1 minute
  # e.g. 43 % 60 = 43 minutes
    minutes = num % 60

  # combine the hours and minutes

    return str(hours) + ':' + str(minutes)

print(TimeConvert(total_trip))


#seconds = df['Trip Duration'].sum()

#minutes = seconds % 3600

#hours = seconds // 3600

#days = hours // 24

#print(minutes)
#print(hours)
#print(days)
#print('The total trip duration was {} hours and {} minutes'.format(hours, minutes))
#import datetime
#total_trip_duration = str(datetime.timedelta(seconds=(df['Trip Duration'].sum())))
#df['time'] = pd.to_datetime(df['Trip Duration'], unit='m')
#print(int(total_time_seconds // 60) %60)))
