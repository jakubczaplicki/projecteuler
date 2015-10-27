#!/usr/bin/env python
# pylint: disable=invalid-name
"""
https://projecteuler.net/problem=20
"""
import math

from problembaseclass import ProblemBaseClass

class Problem20(ProblemBaseClass):
    """
    @class Solution for Problem 20
    @brief
    """
    def __init__(self, n):
        self.result = None
        self.n = n

    def compute(self):
        str = "%s" % self.n
        n = 0
        for s in str:
            n = n + int(float(s))
        self.result = n

if __name__ == '__main__':
    problem = Problem20( math.factorial(10) )
    problem.compute()
    print problem.result #27

    problem = Problem20( math.factorial(100) )
    problem.compute()
    print problem.result #648
