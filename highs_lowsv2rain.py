#! python3
import matplotlib.pyplot as plt
from highs_lows_functions_rain import WeatherData


weather_data_dict = {
                    'Death Valley': 'chapter_16_files\death_valley_2014.csv',  
                    'Sitka': 'chapter_16_files\sitka_weather_2014.csv', 
                    'San Franciso': 'chapter_16_files\san_francisco_2014.csv'
                    }

# Initialize the figure parameters, driver of color change
fig = plt.figure(dpi=128, figsize=(10, 6))
colorlist = ['red', 'green', 'blue', 'orange', 'yellow', 'white']
color_index = int(0)

for key, value in weather_data_dict.items():
    linecolor = colorlist[color_index]
    location = WeatherData(key, value)
    location.store_weather_data()
    # Plot data
    location.plot_rain_data(color=linecolor)
    if color_index == (len(colorlist)-1):
        color_index = 0
    else:
        color_index += 1

# Format plot.
fig.autofmt_xdate()
#~ plt.ylim(15, 150)
legend = plt.legend(loc=2)
plt.title("Daily Rainfall - 2014", fontsize=20)
plt.xlabel('', fontsize=16)
plt.ylabel("Precipitation (Inches)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
#Run plot.
plt.show()
