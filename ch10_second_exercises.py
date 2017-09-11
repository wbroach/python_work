#~ guest_names = []


#~ while True:
    #~ name = input("Please enter your name (press 'q' at any time to exit): ")
    #~ if name.lower() == 'q':
        #~ break
    #~ print("Hello, " + name + "!")
    #~ guest_names.append(name)
    
#~ with open('guest.txt', 'w') as file_object:
    #~ for line in guest_names:
        #~ file_object.write(line + '\n')
        
programming_reasons = []
file_name = 'why_programming.txt'

while True:
    reasons = input("What do you like about programming? (press 'q' at any time to exit) ")
    if reasons.lower() == 'q':
        break
    programming_reasons.append(reasons)
    
with open(file_name, 'r+') as file_object:
    # This code works
    file_object.seek(0)
    file_object.truncate()
    for line in programming_reasons:
        file_object.write(line + '\n')
# This code only works when you open in read-only    
with open(file_name) as file_object:
    contents = file_object.readlines()
    
for i in contents:
    print(i.strip())
#~ print(contents)
#~ for x in contents:
    #~ print(line + "\n")
    
