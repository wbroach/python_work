from time import clock
from primes import PrimeFactors

start_time = clock()

pop = 2000000
ans = PrimeFactors()
ans.size = pop

ans.populate_primes()

print(ans.totals)


end_time = clock()
seconds_elapsed = (end_time - start_time)
print('This routine took ' + str(seconds_elapsed) + ' seconds.')
