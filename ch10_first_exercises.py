
#~ file_name = 'python_can.txt'

#~ with open(file_name) as file_object:
    #~ lines = file_object.readlines()
    
#~ learning_summary = ''

#~ for line in lines:
    #~ learning_summary += line.strip() + " \n"
    
#~ print(learning_summary)
    
file_name = 'python_can.txt'

with open(file_name) as file_object:
    lines = file_object.readlines()
    
for i in range(len(lines)):
    lines[i] = lines[i].replace('Python', 'C').strip()

for line in lines:
    print(line)
    

