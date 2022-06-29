from datetime import datetime

import pandas

data = pandas.read_csv("birthdays.csv")

birthdays = {(row.month, row.day): row for (index, row) in data.iterrows()}

now = datetime.now()
today_month = now.month
today_day = now.day
today_data = data[data['day'] == today_day]
l = today_data[today_data['month'] == today_month]
print((data['day'], data['month']) == (today_day, today_month))