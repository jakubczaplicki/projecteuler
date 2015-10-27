#!/usr/bin/env python
# pylint: disable=invalid-name
"""
https://projecteuler.net/problem=18
"""

from problembaseclass import ProblemBaseClass

class Problem18(ProblemBaseClass):
    """
    @class Solution for Problem 18
    @brief
    """
    def __init__(self):
        self.result = None

    def perm(self, n):
        arr = []
        for s in format(n, '015b'):
            arr.append(int(s))
        idx = 0
        items = []
        sum = 0
        ins = open( "triangles_18.txt", "r" )
        for i,line in enumerate(ins):
            l = [int(x) for x in line.split()]
            idx += arr[i]
            try:
                sum += l[idx]
            except IndexError:
                print "Out of range: ", idx, "arr:", l
        ins.close()
        return sum

    def compute(self):
        sums = []
        n = 2**14
        for i in xrange(n):
            sums.append( self.perm(i) )
        self.result = max(sums)

if __name__ == '__main__':
    problem = Problem18()
    problem.compute()
    print problem.result
