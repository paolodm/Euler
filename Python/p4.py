__author__ = 'Paolo'

import unittest

highest = 0
high_i = 0
high_j = 0

def isPal(number):
    repr = str(number)

    length = len(repr)
    midway = length/2
    firstHalf = repr[:midway]
    secondHalf = repr[length-midway:]

    return firstHalf == secondHalf[::-1]

for i in range(100, 999):
    for j in range(100, 999):
        res = i * j
        if isPal(res) and res > highest:
            highest = res
            high_i = i
            high_j = j

print "The highest is %s with i and j as %s and %s respectively" % (highest, high_i, high_j)

class TestP4(unittest.TestCase):
    def test_isPal(self):
        assert isPal(90709) == True
        assert isPal(9009) == True
        assert isPal(909) == True
        assert isPal(99) == True
        assert isPal(9) == True
        assert isPal(9569) == False
        print isPal(98) == False


"""
    Post-mortem:
    1. substring in python can be achieved with repr[start:finish]
    2. String interpolation is of the form " %s %s ... " % (x, y) -- need ()
    3. unittest is of form: class TestName(unittest.TestCase):
"""