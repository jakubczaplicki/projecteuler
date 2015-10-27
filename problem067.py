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

    def compute(self):
        data = []
        ins = open( "triangles.txt", "r" )
        for i,line in enumerate(ins):
                data.insert(0, [int(x) for x in line.split()] )
        ins.close()
        for n,d in enumerate(data):
            if n == 0: pass
            else:
                data[n] = [ max(i+data[n-1][nn], i+data[n-1][nn+1]) for nn,i in enumerate(d) ]
        self.result = data[n][0]

if __name__ == '__main__':
    problem = Problem18()
    problem.compute()
    print problem.result
    del problem
