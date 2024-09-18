import csv

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
print(highs)

