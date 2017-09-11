#~ with open('text_files\pi_digits.txt') as file_object:
    #~ contents = file_object.read()
    #~ print(contents)

#~ filename = 'C:\\Users\\Prince of Dubtown\\Documents\\python_work\\text_files\\pi_digits.txt'
#~ with open(filename) as file_object:
    #~ contents = file_object.read()
    #~ print(contents)


#~ file_name = 'text_files\pi_digits.txt'

#~ with open(file_name) as file_object: 
        #~ for line in file_object:
            #~ print(line.rstrip())

#~ file_name = 'text_files\pi_digits.txt'

#~ with open(file_name) as file_object:
    #~ list = file_object.readlines()
    
#~ pi_string = ''

#~ for line in list:
    #~ pi_string += line.strip()
    
#~ print(pi_string)
#~ print(len(pi_string))



file_name = 'text_files\pi_million_digits.txt'

with open(file_name) as file_object: 
    lines = file_object.readlines()

pi_digits = ''

for line in lines:
    pi_digits += line.strip()
    
birthday = input("Enter your birthday, in the form of mmddyy: ")

if birthday in pi_digits:
    print("Your birthday is in the first million digits of Pi!")
else:
    print("Your birthday is not in the first million digits of Pi.")














