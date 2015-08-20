#!/usr/bin/env python
# pylint: disable=invalid-name
"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
import sys

from problembaseclass import ProblemBaseClass

class Problem5(ProblemBaseClass):
    """
    @class Solution for Problem 5
    @brief
    """
    def __init__(self, range):
        self.result = None
        self.range = range

    def compute(self):
        notfound=True
        val=0
        while(notfound):
            notfound = False
            val = val + 1
            for n in range(1, self.range):
                if (val % n):
                    notfound = True
        self.result = val

if __name__ == '__main__':
    problem = Problem5(10)
    problem.compute()
    print problem.result
    del problem

    problem = Problem5(20)
    problem.compute()
    print problem.result #232792560
    del problem
