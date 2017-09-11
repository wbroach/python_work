factor = int(600851475143)
multiples_lower = []
multiples_higher = []
prime_factors = []
top_of_range = int(((factor**.5)+1))

for i in range(1, top_of_range):
    if factor % i == 0: 
        multiples_lower.append(i)
        
for multiple in multiples_lower:
    oth_factor = factor / multiple
    multiples_higher.append(oth_factor)

all_multiples = multiples_lower + multiples_higher

for multiple in all_multiples:
    is_prime = True
    for x in range(2, int(multiple)):
        if multiple % x == 0:
            is_prime = False
            break
    if is_prime:
        prime_factors.append(multiple)
    
print(max(prime_factors))

        
    
