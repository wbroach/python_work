from time import clock
start_time = clock()

class PrimeFactors():
    """ A class that models a list of prime numbers"""
    
    def __init__(self):
        """ 
        Initialize list of all prime factors > 1 contained in a given range 
        (e.g. enter 10 for all primes under 10).     
        """
        self.primes = []
        self.size = 0
        self.totals = 0
    
    def populate_primes(self):
        """Populates the list of primes."""
        for value in range(2, self.size):
            is_prime = True
            for x in range(2, (int(value**0.5)+1)):
                if value % x == 0:
                    is_prime = False
                    break
            if is_prime:
                self.primes.append(value)
                self.totals += value

pop = 2000000
ans = PrimeFactors()
ans.size = pop

ans.populate_primes()

print(ans.totals)


end_time = clock()
seconds_elapsed = (end_time - start_time)
print('This routine took ' + str(seconds_elapsed) + ' seconds.') 
