from collections import Counter
import pandas as pd
import numpy as np


df = pd.read_csv('new_york_city.csv')
start_station_pd = pd.Series(df['Start Station'])
end_station_pd = pd.Series(df['End Station'])
combined = pd.concat([start_station_pd, end_station_pd ], axis = 1)
print(type(combined))
#counter = Counter(df['Start Station'])
#top_station = counter.most_common(1)
#counter_end = Counter(df['End Station'])
#top_end_station = counter_end.most_common(1)
