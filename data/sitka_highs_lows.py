import csv
from datetime import datetime
import matplotlib.pyplot as plt
filename = 'data/sitka_weather_2018_simple.csv'
with open(filename, encoding='ISO-8859-1') as f:
    reader = csv.reader(f)
    header_row = next(reader)

# for index, column_header in enumerate(header_row):
#     print(index, column_header)

    # Get dates, and high and low temperatures from this file.
    dates, rainfall = [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            rcp = float(row[3].strip().replace('"', ''))
            rainfall.append(rcp)
            dates.append(current_date)
        except ValueError:
            # Handle missing or non-numeric temperature values
            print(f"Missing or invalid data at row: {row}")

# plot the Rainfall temperatures.
fig, ax = plt.subplots()
ax.plot(dates, rainfall)

# Formart plot.
plt.title("Daily Rainfall amount -2018", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Rainfall (mm)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
