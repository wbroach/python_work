import json
import matplotlib.pyplot as plt

filename = 'chapter_16_files\cpi.json'

with open(filename) as f_obj:
    cpi_dictlist = json.load(f_obj)
    
years = []
cpis = []
    
for dict in cpi_dictlist:
    if dict['Country Name'] == 'Afghanistan':
        year = dict['Year']
        cpi = float(dict["CPI"])
        years.append(year)
        cpis.append(cpi)

cpi_percentages = []
previous_i = 0

for i in cpis:
    try:
        value = (i/previous_i) - 1
    except ZeroDivisionError:
        previous_i = i
    else:
        cpi_percentages.append(value)
        previous_i = i
cpi_percentages.insert(0,0)
        
fig = plt.figure(dpi=128, figsize=(10, 6))
colorlist = ['red', 'green', 'blue', 'orange', 'yellow', 'white']
color_index = int(0)

plt.plot(years, cpi_percentages, c='green', alpha=0.5, label='Afghanistan')

fig.autofmt_xdate()
legend = plt.legend(loc=2)
plt.title("CPI - Afghanistan", fontsize=20)
plt.xlabel('Year', fontsize=16)
plt.ylabel("CPI", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
#Run plot.
plt.show()





