import csv
import matplotlib.pyplot as plt
from datetime import datetime

def store_weather_data(filname):
    """ Pull data from CSV file and store it in relevant attributes."""
    highs, lows, dates = [], [], []
    
    with open(filename) as f_obj:
        reader = csv.reader(f_obj)
        self.header_row = next(reader)
        
        for row in reader:
            try:
                high = int(row[1])
                low = int(row[3])
                current_date = datetime.strptime(row[0], "%Y-%m-%d")
            except ValueError:
                print(current_date, 'missing data')
            else:
                self.highs.append(high)
                self.lows.append(low)
                self.dates.append(current_date)

def plot_weather_data(self):
    """ Plots the weather data using matplotlib's pyplot."""
    plt.plot(self.dates, self.highs, c='red', alpha=0.5, 
        label='Daily High Temp: ' + self.location)
    plt.plot(self.dates, self.lows, c='blue', alpha=0.5, 
        label='Daily Low Temp: ' + self.location)
    plt.fill_between(self.dates, self.highs, self.lows, facecolor='blue', 
        alpha=0.1)
