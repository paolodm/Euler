__author__ = 'Paolo'

import math

def isDivisible(number, divisor):
    return number % divisor == 0

def isPrime(number, primes):
    square_root = math.sqrt(number)

    possible_primes = [p for p in primes if p <= square_root]

    return any(isDivisible(number, pp) for pp in possible_primes) != True



primes = [2, 3]

i = 4

while len(primes) != 10001:
    if isPrime(i, primes):
        primes.append(i)
    i = i + 1

print primes[-1]


"""
    Notes:
    1. Not very efficient as it took some time.
        The method isPrime can take some time. There are better ways of finding prime numbers.
    2. any list comprehension
    3. -1 index to get the last item of the list
"""