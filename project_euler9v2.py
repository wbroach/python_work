from time import clock
start_time = clock()

# a^2 + b^2 = c^2
# a < b < c
# a + b + c = 1000
# Therefore a < 1000 / 3
# Therefore b + c = 2(1000 / 3) 
# c = 1000 - a - b 

def c_finder(sum_of_variables):
    avar = 0
    bvar = 0

    for a in range(1, int(sum_of_variables / 3)):
        for b in range(1, int(sum_of_variables)):
            if (a**2 + b**2) == ((1000-a-b)**2):
                avar = a
                bvar = b
                
    return(avar*bvar*(1000-avar-bvar))

print(c_finder(1000))

end_time = clock()
runtime = end_time - start_time
print('This routine took ' + str(runtime) + ' seconds.')
