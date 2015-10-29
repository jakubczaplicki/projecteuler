#!/usr/bin/env python
# pylint: disable=invalid-name
"""
In England the currency is made up of pound, and pence,
and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, 1 (100p) and 2 (200p).

How many different ways can 2 pounds be made using any numbers of coins ?
https://projecteuler.net/problem=31
"""
import math

# Ultra slow unoptimised solution
class Problem31():
    """
    @class Solution for Problem 31
    @brief
    """
    def __init__(self):
        self.result = None
        self.A = [ 1, 2, 5, 10, 20, 50, 100, 200 ]
        self.B = [ 200, 100, 40, 20, 10, 4, 2, 1 ]
        self.C = [ 0 ] * len(self.A)

    def compute(self):
        A=self.A
        B=self.B
        N=len(self.A)
        C = [ 0 ] * N

        def increase(C, i):
            if C[i] == B[i]*A[i]:
                C[i]=0
                return increase(C, i+1)
            else:
                C[i] += A[i]
                #if sum( map(lambda x,y:x*y, A, C) ) == 200:
                if sum( C ) == 200:
                    return 1
                else:
                    return 0
        count = 0
        while C != [ 0, 0, 0, 0, 0, 0, 0, 200 ]:
            if increase(C, 0):
                count += 1
                print count, C

        self.result = count

if __name__ == '__main__':
    problem = Problem31()
    problem.compute()
    print problem.result #73682
