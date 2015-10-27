#!/usr/bin/env python
# pylint: disable=invalid-name
"""
http://projecteuler.net/problem=6
"""

from problembaseclass import ProblemBaseClass

class Problem6(ProblemBaseClass):
    """
    @class Solution for Problem 6
    @brief
    """
    def __init__(self):
        self.result = None

    def compute(self):
        sumA = 0
        sumB = 0
        for n in range(1,101):
            sumA = sumA + n**2
        for n in range(1,101):
            sumB = sumB + n
        sumB = sumB * sumB
        self.result = sumB - sumA

if __name__ == '__main__':
    problem = Problem6()
    problem.compute()
    print problem.result #25164150
    del problem
