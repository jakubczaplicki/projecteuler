#!/usr/bin/env python
# pylint: disable=invalid-name
"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""
import sys

from problembaseclass import ProblemBaseClass

class Problem3(ProblemBaseClass):
    """
    @class Solution for Problem 3
    @brief
    """
    def __init__(self, v):
        self.result = None
        self.v = v

    def fac(self, val, n=2):
        if not val % n:
            return n
        else:
            return self.fac(val, n+1)

    def allfac(self, v):
        x = 1
        res = []
        while True:
            v = v/x
            x = self.fac(v, 2)
            res.append(x)
            if 0 == v-x:
                return res
        return x

    def rec(self, v):
        sys.setrecursionlimit(9000)
        x = 1
        res = []
        while True:
            v = v/x
            x = self.fac(v, 2)
            res.append(x)
            if 0 == v-x:
                return res
        return x # [71, 839, 1471, 6857] (OK)
        #factor 600851475143
        #600851475143: 71 839 1471 6857

    def compute(self):
        self.result = self.rec(self.v)

if __name__ == '__main__':
    problem = Problem3(13195)
    problem.compute()
    print problem.result
    del problem

    problem = Problem3(600851475143)
    problem.compute()
    print problem.result
    del problem
