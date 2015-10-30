#!/usr/bin/env python
"""Tools for the Project Euler problems in Python"""

import math
import time
import sys

class EulerUtils(object):
    @staticmethod
    def is_prime(number):
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

    @staticmethod
    def is_palindrome(value, method = 0):
        if isinstance(value, int) and method == 0:
            return str(value) == str(value)[::-1]

        elif isinstance(value, int) and method == 1::
            import math
            N = int(math.log10(value))+1
            for i in xrange( (N/2) ):
                first = (value % ( 10**(N - i))) / 10**(N-1-i)
                last =  value%(10**(i+1))/(10**i)
                if first != last:
                    break
            return first == last

        elif isinstance(value, str) and method == 0:
            return value == value[::-1]

        elif isinstance(value, str) and method == 1:
            s = str(number)
            N = len(s)
            i = 0
            while s[i] == s[N - i - 1] and i != N/2:
               i += 1
            return i == N/2

if __name__ == '__main__':
    utils = EulerUtils()
    assert utils.is_prime(2) == True
    assert utils.is_prime(10) == False
    print utils.is_palindrome(1234)
    print utils.is_palindrome(12345)
    print utils.is_palindrome(1234321)
    print utils.is_palindrome(1221)

    assert utils.is_palindrome("123") == False
    assert utils.is_palindrome("232") == True
    assert utils.is_palindrome("123456") == False
    assert utils.is_palindrome("623326") == True
