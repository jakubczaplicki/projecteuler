#!/usr/bin/env python
# pylint: disable=invalid-name
"""
In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right,
by only moving to the right and down, is indicated in bold red and is equal to 2427.

131	673	234	103	18
201	96	342	965	150
630	803	746	422	111
537	699	497	121	956
805	732	524	37	331


Find the minimal path sum, in matrix.txt (right click and "Save Link/Target As..."),
a 31K text file containing a 80 by 80 matrix, from the top left to the bottom right by only moving right and down.
"""

class Problem81():
    """
    @class Solution for Problem 81
    @brief
    """
    def __init__(self):
        self.result = None

    def compute(self):
        data = []
        ins = open( "p081_matrix.txt", "r" )
        for i,line in enumerate(ins):
                data.append( [int(x) for x in line.split(',')] )
        ins.close()
        for i,d in enumerate(data):
            for j in xrange(len(d)):
                if i == 0 and j > 0:
                    data[i][j] = data[i][j] +  data[i][j-1]
                elif j == 0 and i > 0:
                    data[i][j] = data[i][j] +  data[i-1][j]
                elif i > 0 and j > 0:
                    data[i][j] = min(data[i][j] +  data[i][j-1], data[i][j] +  data[i-1][j])
        self.result = data[-1][-1]

if __name__ == '__main__':
    problem = Problem81()
    problem.compute()
    print problem.result
