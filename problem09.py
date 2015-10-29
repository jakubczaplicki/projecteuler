#!/usr/bin/env python
# pylint: disable=invalid-name
"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

https://projecteuler.net/problem=9
"""
import math

class Problem9():
    """
    @class Solution for Problem 9
    @brief
    """
    def __init__(self):
        self.result = None

    def compute(self):
        a = 0
        b = 1
        c = 2
        #while (a**2 + b**2 != c**2) or (a + b + c != 1000):
        while (2*a*b - 2000 * a - 2000 * b + 1000 **2 != 0):
            a+=1
            if a == 1000:
                a = 0
                b += 1
                #if b == 1000:
                #    b = 0
                #    c += 1
        c = 1000 - a - b
        print a**2 + b**2 - c**2, a+b+c
        self.result = a * b * c

if __name__ == '__main__':
    problem = Problem9()
    problem.compute()
    print problem.result #31875000
