#! python3
import csv
import matplotlib.pyplot as plt
from datetime import datetime
from highs_lows_functions import WeatherData


weather_data_dict = {
                    'Death Valley': 'chapter_16_files\death_valley_2014.csv',  
                    'Sitka': 'chapter_16_files\sitka_weather_2014.csv', 
                    'San Franciso': 'chapter_16_files\san_francisco_2014.csv'
                    }

# Initialize the figure parameters, driver of color change
fig = plt.figure(dpi=128, figsize=(10, 6))
colorlist_high = ['red', 'green', 'orange']
colorlist_low = ['blue', 'yellow', 'white']
color_index = int(0)

for key, value in weather_data_dict.items():
    high = colorlist_high[color_index]
    low = colorlist_low[color_index]
    location = WeatherData(key, value)
    location.store_weather_data()
    # Plot data
    location.plot_weather_data(highcolor=high, lowcolor=low)
    if color_index == (len(colorlist_high)-1):
        color_index = 0
    else:
        color_index += 1

# Format plot.
fig.autofmt_xdate()
plt.ylim(15, 150)
legend = plt.legend(loc=2)
plt.title("Daily high & low temperatures - 2014", fontsize=20)
plt.xlabel('', fontsize=16)
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
#Run plot.
plt.show()
