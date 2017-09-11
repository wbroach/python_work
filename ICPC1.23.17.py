array_list = [value for value in range(1, 101)] #generate array
array_list.append(15) #seed array with duplicates 
array_list.append(19) 
array_list.append(25) 
array_list.append(77) 
array_list.append(88) 

duplicate_list = [] # this array will store the duplicates
        
array_list.sort()

for i in range(1, len(array_list)):
    if array_list[i] == array_list[i-1]:
        duplicate_list.append(array_list[i])
        
print(duplicate_list)



# Brute force
#~ for i in range(len(array_list)):
    #~ for x in array_list[(i+1):]:
        #~ if i == x:
            #~ duplicate_list.append(i)
            
#~ print(duplicate_list)


