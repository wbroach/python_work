import csv

filename = 'chapter_16_files\sitka_weather_2014.csv'

with open(filename) as f_obj:
    r = csv.reader(f_obj)
    header_row = next(r)
    

    
for index, column in enumerate(header_row):
    print(index, column)
