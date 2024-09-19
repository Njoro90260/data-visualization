import csv
from datetime import datetime
import matplotlib.pyplot as plt
filename = 'data/sitka_weather_07-2018_simple.csv'
with open(filename, encoding='ISO-8859-1') as f:
    reader = csv.reader(f)
    header_row = next(reader)

# for index, column_header in enumerate(header_row):
#     print(index, column_header)

    # Get industry and values from this file.
    dates, highs = [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            high = int(row[5].strip().replace('"', ''))
            dates.append(current_date)
            highs.append(high)
        except ValueError:
            # Handle missing or non-numeric temperature values
            print(f"Missing or invalid data at row: {row}")

# plot the high temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red')
ax.plot(highs, c='red')

# Formart plot.
plt.title("Daily temperatures of January 2018", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
