def list_prime_factors(size):
    """ 
    Returns a list of all prime factors > 1 contained in a given range 
    (e.g. enter 10 for all primes under 10).     
    """
    primes = []

    for value in range(2, size):
        is_prime = True
        for x in range(2, (int(value**0.5)+1)):
            if value % x == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(value)
            
    return primes


item = list_prime_factors(50)

print(item)


