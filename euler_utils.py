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
    def is_palindrome(number):
        s = str(number)
        N = len(s)
        i = 0
        while s[i] == s[N - i - 1] and i != N/2:
           i += 1
        return i == N/2

    @staticmethod
    def is_palindrome(string):
        return string == string[::-1]

#class isPalindrome(object):
#    def __init__(self, s):
#        N = len(s)
#        i = 0
#        while s[i] == s[N - i - 1] and i != N/2:
#           i += 1
#        self.result = i == N/2
#    def __str__(self):
#        return str(self.result)




if __name__ == '__main__':
    utils = EulerUtils()
    assert utils.is_prime(2) == True
    assert utils.is_prime(10) == False
    assert utils.is_palindrome("123") == False
    assert utils.is_palindrome("232") == True
    assert utils.is_palindrome("123456") == False
    assert utils.is_palindrome("623326") == True
