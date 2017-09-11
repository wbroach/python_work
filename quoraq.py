list_1 = ['Mary', 'Jane', 'Alice']
list_2 = [value for value in range (3,6)]
my_dict = dict(zip(list_1, list_2))

for k, v in my_dict.items():
    print(str(k) + ":\t" + str(v))


#~ if len(list_1) == len(list_2):
    #~ for i in range(0, len(list_1)):
        #~ my_dict[list_1[i]] = list_2[i]
        

    
