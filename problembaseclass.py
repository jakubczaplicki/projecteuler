#!/usr/bin/env python
"""Base class for the Project Euler problems in Python"""
##@file
#@ingroup 
#
# @brief
# Base class for the Project Euler problems in Python
#
#
# @version $$
# @details
#
# @b Description
# This module implements a base class, that can be used
# for all project eurler solutions.
#
# @b Usage
# Usage:
# Extend this class to implement a test

import math
import time
import sys

class ProblemBaseClass(object):
    """
    @class
    @brief
    """ 
    def __init__(self):
        self.result = None

    def label(self):
        self.label = "No label"


    def setup(self):
        """setup method for all solutions
        Override to:
         - process options, etc.
        """

    def initiate(self, *_args, **_kwargs):
        """initiate method for all solutions
        Override to:
         - load data
         - initiate connections to Spark 
        """

    def compute(self, *_args, **_kwargs):
        """@method compute the solution
        Override to:
         - implement a solution for the given problem.
         
         Must be implemented
        """
        return None

    def teardown(self):
        """@method teardown method for all solutions
        Override to:
         - tidy up
         Must be implemented
        """

    def isPrime(number):
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
    problem = problem1()
    problem.compute()
    print problem.result
