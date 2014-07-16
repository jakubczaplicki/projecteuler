
import math
import sys

sys.setrecursionlimit(200000)

def fac(val,n):
  if not (val % n):
    return fac(val/n, 2)
  else:
    print val, n
    return fac(val,n+1)
  
print fac(600851475143, 2) # MemoryError: stack overflow
