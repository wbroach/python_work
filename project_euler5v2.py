from time import clock

start_time = clock()
primes = []
n = 2

while len(primes) < 10001:
    is_prime = True
    for p in primes:
        if n % p == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(n)
    else:
        n += 1

end_time = clock()
print(primes[-1])
seconds_elapsed = (end_time - start_time)

print('This routine took ' + str(seconds_elapsed) + ' seconds.')
