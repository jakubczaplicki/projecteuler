#!/usr/bin/env python
# pylint: disable=invalid-name
"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

import sys

from euler_utils import EulerUtils

class Problem4():
    """
    @class Solution for Problem 4
    @brief
    """
    def __init__(self):
        self.result = None

    def compute(self):
        eutils = EulerUtils
        i = 999
        j = 999
        n = i * j
        max_n = 0
        while j > 100: #str(n) != str(n)[::-1]: #eutils.isPalindrome(n):
            i-=1
            if 100 == i:
                i = 999
                j -= 1
            n = i*j
            if str(n) == str(n)[::-1]:
                if n > max_n:
                    max_n = n
        self.result = max_n

if __name__ == '__main__':
    problem = Problem4()
    problem.compute()
    print problem.result
