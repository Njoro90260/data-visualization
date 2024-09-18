import csv
import matplotlib.pyplot as plt
filename = 'data/sitka_weather_07-2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get high temparatures from this file.
    highs = []
    for row in reader:
        try:
            high = int(row[5].strip().replace('"', ''))
            highs.append(high)
        except ValueError:
            # Handle missing or non-numeric temperature values
            print(f"Missing or invalid data at row: {row}")

# plot the high temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(highs, c='red')

# Formart plot.
plt.title("Daily high temperature , First week of January 2018", fontsize=24)
plt.xlabel('', fontsize=16)
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
