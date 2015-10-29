#!/usr/bin/env python
"""Tools for the Project Euler problems in Python"""

import math
import time
import sys

class Utils(object):
    def isPrime(self, number):
        """Returns True is number is prime, False otherwise"""
        # This algorithm checks if the given number can be divided by integers of the form 6k +/- 1
        # see: http://en.wikipedia.org/wiki/Primality_test#Naive_methods
        if number <= 3:
            return number > 1
        if number % 2 == 0 or number % 3 == 0:
            return False
        for i in range(5, int(number ** 0.5) + 1, 6):
            if number % i == 0 or number % (i + 2) == 0:
                return False
        return True

if __name__ == '__main__':
    utils = Utils()
    assert utils.isPrime(2) == True
    assert utils.isPrime(10) == False
