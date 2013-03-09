__author__ = 'Paolo'

import math

def factorization(number):
    remaining = number
    factors = []
    start = 2
    while start <= remaining:
        while remaining % start == 0:
            factors.append(start)
            remaining = remaining / start
        start += 1
    return factors

answer = 1
numbers = range(2,21)  # 2 to 20
factorized = []

for i in numbers:
    factorized.append(factorization(i))

for i in numbers:
    highest_cnt_i = 0
    for item in factorized:
        cnt_i = item.count(i)
        if cnt_i > highest_cnt_i:
            highest_cnt_i = cnt_i

    answer *= math.pow(i, highest_cnt_i)

print answer

"""
    Post-mortem
    1. math.pow(x, y)
    2. range is included-non included
"""

