# Get assumptions for finding duplicates - know greatest N? YES!


string = 'Reverse this string.'

reversed_string = []
rev_string_message = ''

list = string.split()
    
for i in list:
    rev = i[::-1]
    reversed_string.append(rev)
    
for x in reversed_string:
    rev_string_message += x + ' '
    
print(rev_string_message)


#~ bool_flag = [False for value in range(3)]

#~ print(bool_flag)
