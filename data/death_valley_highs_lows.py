import csv
from datetime import datetime
import matplotlib.pyplot as plt
filename = 'data/death_valley_2018_simple.csv'
with open(filename, encoding='ISO-8859-1') as f:
    reader = csv.reader(f)
    header_row = next(reader)

# for index, column_header in enumerate(header_row):
#     print(index, column_header)

    # Get dates, and high and low temperatures from this file.
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            high = int(row[4].strip().replace('"', ''))
            low = int(row[5])
        except ValueError:
            # Handle missing or non-numeric temperature values
            print(f"Missing or invalid data for {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

# plot the high temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Formart plot.
title = "Daily high and low temperatures -2018\nDeath Valley, CA"
plt.title(title, fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
