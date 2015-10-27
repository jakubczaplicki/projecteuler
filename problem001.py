#!/usr/bin/env python
"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we
get 3, 5, 6 and 9. The sum of these multiples is 23. Find the sum of all the
multiples of 3 or 5 below 1000.
"""

import math

from problembaseclass import ProblemBaseClass

class Problem1(ProblemBaseClass):
    """
    @class Solution for Problem 1
    @brief
    """
    def __init__(self):
        self.result = None

    def compute(self):
        _sum = 0
        for n in range(1, 1000):
            if (0 == math.fmod(n, 3)) or (0 == math.fmod(n, 5)):
                _sum = _sum + n
        self.result = _sum
        return sum # 233168 (OK)

if __name__ == '__main__':
    problem = Problem1()
    problem.compute()
    print problem.result
