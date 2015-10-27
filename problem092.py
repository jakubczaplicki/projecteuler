__author__ = 'jc60'
"""
A number chain is created by continuously adding the square of the digits in
a number to form a new number until it has been seen before.

For example,

44 -> 32 -> 13 -> 10 -> 1 -> 1
85 -> 89 -> 145 -> 42 -> 20 -> 4 -> 16 -> 37 -> 58 -> 89

Therefore any chain that arrives at 1 or 89 will become stuck in an endless
loop. What is most amazing is that EVERY starting number will eventually
arrive at 1 or 89.

How many starting numbers below ten million will arrive at 89?
"""

import time

def sum_sq_dig(x):
    y=0
    while (x != 0): y+=(x%10)**2; x=x/10
    return y
n89=0

start_time = time.time()
lookup={}
for x in xrange(1,10000000):
    xt = x
    while ((x != 1) and (x != 89)):
        x = sum_sq_dig(x)
        if x in lookup:
            x=lookup[x]
            break
    lookup[xt]=x
    if x == 89:
        n89+=1
elapsed_time = time.time() - start_time
print n89, elapsed_time
# brute force: 8581146 91.4530000687
# with lookup table: 8581146 31.2089998722
# with lookup table: 8581146 25.5750000477
