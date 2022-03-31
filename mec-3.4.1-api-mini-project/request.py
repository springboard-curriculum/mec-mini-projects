import requests
import os
import numpy as np
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('NASDAQ_API_KEY')
DATE_COLUMN = 0
DAY_OPEN_COLUMN = 1
DAY_HIGH_COLUMN = 2
DAY_LOW_COLUMN = 3
DAY_CLOSE_COLUMN = 4
DAY_TRADING_VOLUME = 6

# 1. Collect data from the Franfurt Stock Exchange, for the ticker AFX_X, for the whole year 2017
response = requests.get(
    'https://data.nasdaq.com/api/v3/datasets/FSE/AFX_X/data.json?start_date=2017-01-01&end_date=2017-12-31&api_key={}'.format(
        API_KEY))

# 2. Convert the returned JSON object into a Python dictionary.
data = response.json()
daily_data = data['dataset_data']['data']

print('Data for year 2017 for AFX_X: ', daily_data)


def find_edge(daily_list: list, column: int, func) -> int:
    return func(daily_value[column] for daily_value in daily_list)


# 3. Calculate what the highest and lowest opening prices were for the stock in this period.
print('Highest opening price of the year: ', find_edge(daily_data, DAY_HIGH_COLUMN, max))
print('Lowest opening price of the year:  ', find_edge(daily_data, DAY_LOW_COLUMN, min))


def find_highest_diff(daily_list: list, high: int, low: int):
    return round(max((daily_value[high] - daily_value[low]) for daily_value in daily_list), 2)


# 4. What was the largest change in any one day (based on High and Low price)?
print('Largest change in any one day in 2017: ', find_highest_diff(daily_data, DAY_HIGH_COLUMN, DAY_LOW_COLUMN))


def find_largest_change(daily_list: list, close_column: int):
    i = 1
    largest = 0
    while i < len(daily_list):
        current_diff = abs(daily_list[i - 1][close_column] - daily_list[i][close_column])
        i += 1
        if current_diff > largest:
            largest = current_diff
    return round(largest, 2)


# 5. What was the largest change between any two days (based on Closing Price)
print('The largest change between any two days: ', find_largest_change(daily_data, DAY_CLOSE_COLUMN))


def avg_trading_volume(daily_list: list, trading_vol_column: int):
    trading_volume_list = np.array(daily_list)[:, trading_vol_column]
    return round(trading_volume_list.sum() / (len(daily_list)), 2)


# 6. What was the average daily trading volume during this year?
print('The average daily trading in year 2017: ', avg_trading_volume(daily_data, DAY_TRADING_VOLUME))


def sort_key(daily_value):
    return daily_value[DAY_TRADING_VOLUME]


def median_volume(daily_list):
    sorted_volume_list = sorted(daily_list, key=sort_key, reverse=False)
    list_length = len(daily_list)
    if list_length / 2 == 0:
        return (sorted_volume_list[int(list_length / 2)] + sorted_volume_list[int(list_length / 2 + 1)]) / 2
    else:
        return sorted_volume_list[int((list_length / 2) + 0.5)]


# 7. (Optional) What was the median trading volume during this year.
print('The median trading volume during this year 2017: ', median_volume(daily_data)[6])
