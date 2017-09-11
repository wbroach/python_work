
#~ numbers = [values for values in range(1,11,2)]

#~ with open(filename, 'w') as f_obj:
    #~ json.dump(numbers, f_obj)

import json

filename = 'numbers.json'

with open(filename) as f_obj:
    numbers = json.load(f_obj)
    
print(numbers)
