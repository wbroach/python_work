from time import clock
start_time = clock()

# a^2 + b^2 = c^2
# a < b < c
# a + b + c = 1000
# Therefore a < 1000 / 3
# Therefore b + c = 2(1000 / 3) 
# c = 1000 - a - b 

a_list = []
b_list = []
limit_of_sum = 1000

for a in range(1, int(limit_of_sum / 3)):
    for b in range(1, limit_of_sum):
        if (a**2 + b**2) == ((1000-a-b)**2):
            a_list.append(a)
            b_list.append(b)

if len(a_list) == 1 and len(b_list) == 1:
    aval = a_list[0]
    bval = b_list[0]
    cval = 1000 - aval - bval

if (aval**2 + bval**2) == cval**2 and (aval + bval + cval) == 1000:
    print(aval, bval, cval)            
    print("The product is " + str(aval*bval*cval) + ".")

end_time = clock()
runtime = end_time - start_time
print('This routine took ' + str(runtime) + ' seconds.')
