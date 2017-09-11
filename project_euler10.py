from time import clock
from prime_number_searcher import list_prime_factors as lpf

start_time = clock()

size = 2000000

primes = lpf(size)
        
sum_of_primes = 0

for prime in primes:
    sum_of_primes += prime
    
print(sum_of_primes)

end_time = clock()
seconds_elapsed = (end_time - start_time)
print('This routine took ' + str(seconds_elapsed) + ' seconds.')
