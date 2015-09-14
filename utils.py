#!/usr/bin/env python
"""Utils class for the Project Euler problems in Python"""
##@file
#@ingroup 
#
# @brief
# Utils class for the Project Euler problems in Python
#
#
# @version $$
# @details
#
# @b Description
# This module implements a utility class.
#
# @b Usage
# Usage:

class Utils(object):
    """
    @class
    @brief
    """ 
    def __init__(self):
        self.result = None

    def isPrime(self, number):
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

        
if __name__ == '__main__':
    utils = Utils()
    assert isinstance(utils, Utils), "%r is not an Utils" % utils
    assert utils.isPrime(2), "Faulty isPrime method"
    assert utils.isPrime(982451653), "Faulty isPrime method"