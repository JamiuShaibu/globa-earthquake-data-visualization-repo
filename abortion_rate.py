import csv

import matplotlib.pyplot as plt
from datetime import datetime

"""
# Parsing the csv Files Headers.
filename = 'as-dec-19-general-abortion-rate.csv'
print("The csv Files Headers;")
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)

# To Print the Headers and Their Positions(index).
# We need the indexes of the headers for the program
print("\nHEADER AND THEIR POSITIONS(indexes);")
for index, column_header in enumerate(header_row):
    print(index, column_header)
"""

filename = 'as-dec-19-general-abortion-rate.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates, and high and lows temperatures from this file.
    dates, rates = [], []
    for row in reader:
        current_date = datetime.strptime(row[0], '%Y')
        rate = float(row[1])
        dates.append(current_date)
        rates.append(rate)


# Plot the high and low temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, rates, c='red', alpha=0.5)
ax.fill_between(dates, rates, facecolor='blue', alpha=0.1)

# format plot.
ax.set_title("General Abortion Rate, 1980 - 2020", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Rate (%)", fontsize=16)

plt.show()
