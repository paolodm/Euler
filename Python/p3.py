__author__ = 'Paolo'

remaining = 600851475143
start = 2
high_prime = None
mult = []

while start <= remaining:
    if remaining % start == 0:
        mult.append(start)
        if start % 2 != 0:
            high_prime = start
        remaining = remaining / start
    start += 1

print "The highest prime is %s " % high_prime

print "The multiplers are %s" % mult

"""Post-mortem:
    1. None is null
"""