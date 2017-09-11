factor = 600851475143
multiples = []
prime_factors = []
top_of_range = int(((factor**.5)+1))

for i in range(1, top_of_range):
    if factor % i == 0: 
        multiples.append(i)
        
print(multiples)


#~ for multiple in multiples:
    #~ is_prime = True
    #~ for x in range(2, multiple):
        #~ if multiple % x == 0:
            #~ is_prime = False
            #~ break
    #~ if is_prime:
        #~ prime_factors.append(multiple)
    
#~ print(max(prime_factors))

        
    
