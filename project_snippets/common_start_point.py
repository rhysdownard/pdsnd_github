import pandas as pd
import numpy as np

df = pd.read_csv('new_york_city.csv')
'''
#print(df['Start Station'])
from collections import Counter
counter = Counter(df['Start Station'])
top_station = counter.most_common(1)
top_station_string = str(top_station)
top_station_split = top_station_string.split(',')
counter_end = Counter(df['End Station'])
top_end_station = counter_end.most_common(1)
#top_station_list = str(top_station.split(','))
print(type(top_station))
print(top_station[0][1])
print(top_station[0][0])
print(str(top_station[0]))
print(top_station_split)
print('The top station is {} with {} visits '.format(top_station[0][0], top_station[0][1] ))
#print('The top station is {} with {} number of visits'.format(top_station[0], top_station[1]))
#pop_start = df['Start Station'].mode()[0]
#print(pop_start)
'''

common_start_station = df['Start Station'].mode()[0]
print(common_start_station)
df["combined"] = df["Start Station"] + " - "+ df["End Station"]
common_combined = df["combined"].mode()[0]

#display most frequent combination of start station and end station trip
#start_station_pd = pd.Series(df['Start Station'])
#end_station_pd = pd.Series(df['End Station'])
#pd.concat([start_station_pd, end_station_pd ], axis = 1).mode()[0]
print('The most frequent occurence of a start and end station group is {}'.format(common_combined))
