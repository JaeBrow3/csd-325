# This program reads temperature data from a CSV file and allows the user to view either high or low temperatures for a specific year.
# The user must choose whether to view high or low temperatures or exit the program.

import csv
from datetime import datetime

from matplotlib import pyplot as plt

filename = 'sitka_weather_2018_simple.csv'
dates, highs, lows = [], [], []
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates, highs, and lows from this file
    for row in reader:
        try:
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            high = int(row[5])
            low = int(row[6])
        except ValueError:
            # Skip rows with missing or bad data
            continue
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

# Main loop for user prompts
while True:
    choice = input("Type 'highs' to see high temperatures, 'lows' to see low temperatures, or 'exit' to exit: ").strip().lower()

    if choice == 'exit':
        print("Exiting the program. Good day!")
        break
    elif choice == 'highs':
        fig, ax = plt.subplots()
        ax.plot(dates, highs, c='red')
        ax.set_title("Daily High Temperatures - 2018", fontsize=24)
        ax.set_ylabel("Temperature (F)", fontsize=16)
    elif choice == 'lows':
        fig, ax = plt.subplots()
        ax.plot(dates, lows, c='blue')
        ax.set_title("Daily Low Temperatures - 2018", fontsize=24)
        ax.set_ylabel("Temperature (F)", fontsize=16)
    else:
        print("Invalid input. Please choose 'highs', 'lows', or 'exit'.")
        continue

    ax.set_xlabel('', fontsize=16)
    fig.autofmt_xdate()
    ax.tick_params(axis='both', which='major', labelsize=16)
    plt.show()
