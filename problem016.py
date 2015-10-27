#!/usr/bin/env python
# pylint: disable=invalid-name
"""
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""

from problembaseclass import ProblemBaseClass

class Problem16(ProblemBaseClass):
    """
    @class Solution for Problem 16
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
    problem = Problem16(2**15)
    problem.compute()
    print problem.result #26
    del problem

    problem = Problem16(2**1000)
    problem.compute()
    print problem.result #1366
    del problem
