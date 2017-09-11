mults = []
palins = []
upper = 999 + 1

for value in range(, upper):
    tots = value * (upper-1)
    mults.append(str(tots))
    

for i in mults:
    if i == i[::-1]:
        palins.append(int(i))
        
print(max(palins, default = 'empty'))






#~ digit_1 = 99
#~ mults = []
#~ palins = []

#~ for value in range(1, 1000):
    #~ x = digit_1 * value
    #~ mults.append(x)
    
#~ for i in range (len(mults)):
    #~ mults[i] = str(mults[i])
    










#~ string = '1234'
#~ print(string[::-1])
