#!/usr/bin/env python
# pylint: disable=invalid-name
"""
Each new term in the Fibonacci sequence is generated by adding the previous
two terms. By starting with 1 and 2, the first 10 terms will be:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
By considering the terms in the Fibonacci sequence whose values do not exceed
four million, find the sum of the even-valued terms.
"""
from problembaseclass import ProblemBaseClass

class Problem2(ProblemBaseClass):
    """
    @class Solution for Problem 2
    @brief
    """
    def __init__(self):
        self.result = None

    def f(self, n):
        if (n <= 0) | (1 == n):
            return 1
        else:
            fib = self.f(n-1) + self.f(n-2)
        return fib

    def compute(self):
        _sum = 0
        for n in range(1, 33):
            fib = self.f(n)
            if not fib % 2:
                _sum = _sum + fib
        self.result = _sum #4613732 (OK)

if __name__ == '__main__':
    problem = Problem2()
    problem.compute()
    print problem.result
