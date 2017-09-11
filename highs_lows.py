#! python3
import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'chapter_16_files\death_valley_2014.csv'

with open(filename) as f_obj:
    reader = csv.reader(f_obj)
    header_row = next(reader)
    
    highs, lows, dates = [], [], []
    
    for row in reader:
        try:
            high = int(row[1])
            low = int(row[3])
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
        except ValueError:
            print(current_date, 'missing data')
        else:
            highs.append(high)
            lows.append(low)
            dates.append(current_date)

# Plot data
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha=0.5, label='Daily High Temp')
plt.plot(dates, lows, c='blue', alpha=0.5, label='Daily Low Temp')
plt.ylim(-20, 150)
legend = plt.legend(loc=2)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
# Format plot.
plt.title("Daily high & low temperatures - 2014\nDeath Valley, CA", fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()
