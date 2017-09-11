import csv
import matplotlib.pyplot as plt
from datetime import datetime

class WeatherData():
    """ 
    A class that attempts to model a set of weather data for a given time
    period and location.
    """
    def __init__(self, location, filename):
        self.location = location
        self.filename = filename
        self.highs = []
        self.lows = []
        self.dates = []
        self.header_row = ''
        
    def store_weather_data(self):
        """ Pull data from CSV file and store it in relevant attributes."""
        with open(self.filename) as f_obj:
            reader = csv.reader(f_obj)
            self.header_row = next(reader)
            for row in reader:
                try:
                    current_date = datetime.strptime(row[0], "%Y-%m-%d")
                    high = int(row[1])
                    low = int(row[3])
                except ValueError:
                    print(current_date, 'missing data')
                else:
                    self.highs.append(high)
                    self.lows.append(low)
                    self.dates.append(current_date)
    
    def plot_weather_data(self, highcolor='red', lowcolor='blue'):
        """ Plots the weather data using matplotlib's pyplot."""
        plt.plot(self.dates, self.highs, c=highcolor, alpha=0.5, 
            label='Daily High Temp: ' + self.location)
        plt.plot(self.dates, self.lows, c=lowcolor, alpha=0.5, 
            label='Daily Low Temp: ' + self.location)
        plt.fill_between(self.dates, self.highs, self.lows, facecolor='blue', 
            alpha=0.1)
