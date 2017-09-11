import pygal, webbrowser
from die import Die

#Create two six-sided dice
die_1 = Die(num_sides=8)
die_2 = Die(num_sides=8)
max_result = die_1.num_sides + die_2.num_sides

#Makes some rolls, store the results in a list. 
rolls = [die_1.roll() + die_2.roll() for value in range(50000)]

#~ for i in range(50000):
    #~ die_rolls = die_1.roll() + die_2.roll()
    #~ rolls.append(die_rolls)
    
frequencies = [rolls.count(value) for value in range(2, max_result+1)]

#~ for value in range(2, max_result+1):
    #~ frequency = rolls.count(value)
    #~ frequencies.append(frequency)
    
# Visualize the results.
hist = pygal.Bar()

hist.title = "Results of rolling D6 & D10 50000 times"
hist.x_labels = [str(value) for value in range(2, max_result+1)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D10', frequencies)
hist.render_to_file('die_visual.svg')
webbrowser.get('windows-default').open('die_visual.svg')
