mults = []
palins = []

for value in range (100, 1000):
    for i in range (100, 1000):
        prod = value * i 
        mults.append(str(prod))
        
for i in mults:
    if i == i[::-1]:
        palins.append(int(i))
        
print(max(palins, default = 'empty'))

    

