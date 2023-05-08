# with open("./weather_data.csv", "r") as f:
#     data = [weather for weather in f.readlines()[1:]]

# print(data)

# import csv

# with open("weather_data.csv") as data_file:
#     data = [weather for weather in csv.reader(data_file)]
#     temperatures = [int(tmp[1]) for tmp in data[1:]]

#     print(temperatures)

import pandas as pd
import numpy as np

# data = pd.read_csv('weather_data.csv')

# print(data.loc[data['temp'].idxmax()])

# monday = data[data.day == "Monday"]

# print(monday.condition)
# print(monday.temp * 9/5 + 32)

data = pd.read_csv("squirrel_count.csv")
# print(data["Primary Fur Color"].value_counts())

# df = data["Primary Fur Color"].value_counts().rename_axis(
#     'Fur Color').reset_index(name='counts')
# df.to_csv("squirrel_count.csv")
print(data)
