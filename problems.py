
import math
import time
import sys

#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.
class problem1():
  #def __init__(self):
  #  print self.result()
  def result(self):
    sum = 0
    for n in range(1,1000):
      if ( (0 == math.fmod(n,3)) or (0 == math.fmod(n,5)) ):
        sum = sum + n
        #print n,m, math.fmod(n,m), sum
    return sum # 233168 (OK)

#Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
#1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
class problem2():
  #def __init__(self):
  #  print self.result()
  def f(self,n):
    if ((n <= 0) | (n==1)):
      return 1
    else:
      fib = (self.f(n-1) + self.f(n-2))
      return fib

  def result(self):
    sum = 0 
    for n in range(1,33):
      fib = self.f(n)
      if not (fib % 2):
        sum = sum + fib
    return sum #4613732 (OK)

#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?
class problem3():
  #def __init__(self):
  #  print self.result()
    
  def fac(self,val,n=2):
    if not (val % n):
      return n
    else:
      #print val, n
      return self.fac(val,n+1)

  def allfac(self,v):
    x=1
    res = []
    while (1):
      v = v/x
      x = self.fac(v,2)
      res.append(x)
      if (v-x == 0):
        return res
    return x # [71, 839, 1471, 6857] (OK)

  def result(self):
    sys.setrecursionlimit(9000)
    x = 1
    #v = 13195
    v=600851475143
    res = []
    while (1):
      v = v/x
      x = self.fac(v,2)
      res.append(x)
      if (v-x == 0):
        return res
    return x # [71, 839, 1471, 6857] (OK)
    #factor 600851475143
    #600851475143: 71 839 1471 6857

#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
#Find the largest palindrome made from the product of two 3-digit numbers.
class problem4():
  def fac(self,val,n=999):
    if n == 2:
      return n
    if not (val % n):
      return n
    else:
      return self.fac(val,n-1)

  def allfac(self,v):
    x=1
    res = []
    while (1):
      v = v/x
      if x==1:
        x = self.fac(v,999)
      else:
        x = self.fac(v,x)
      res.append(x)
      if (v/x == 1):
        return res
    return x
 
  def pal(self,n):
      return n*1000 + ((n/100)%10) + ((n/10)%10)*10 + ((n/1)%10)*100

  def pal2(self):
      i = 999
      j = 999
      max = 0
      while (True):
        n = i * j
        i = i - 1
        if ( ( (n/1)%10 != 0 ) and ( (n/1)%10 == (n/100000)%10 ) and ( (n/10)%10 == (n/10000)%10 ) and ( (n/100)%10 == (n/1000)%10 ) ):
          if (n > max):
            max = n
            maxi = i
            maxj = j
        if (j==100) and (i==100):
            break
        if (i == 100):
          i = 999
          j = j - 1
      print maxi,maxj,max
      #906609
        
  def result(self):
    return self.pal2()

#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
class problem5():
  def result(self):
    notfound=True
    val=0
    while(notfound):
      notfound = False
      val = val + 1
      for n in range(1,20):
        if (val % n):
          notfound = True
    return val
    #232792560

#http://projecteuler.net/problem=6
class problem6():
  def result(self):
    sumA = 0
    sumB = 0
    for n in range(1,101):
      sumA = sumA + n**2
    for n in range(1,101):
      sumB = sumB + n
    sumB = sumB * sumB
    return sumB - sumA
    #25164150

#A permutation is an ordered arrangement of objects. For example, 3124 is one
#possible permutation of the digits 1, 2, 3 and 4. If all of the permutations
#are listed numerically or alphabetically, we call it lexicographic order.
# The lexicographic permutations of 0, 1 and 2 are:
# 012   021   102   120   201   210
#What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
class problem24():
  import math
  arr = [0,0,0]

  def increase(self,n):
    if ((self.arr[n]+1)%3 == 0) and ((n+1) < len(self.arr)):
      self.arr[n] = 0
      self.increase(n+1)
    else:
      self.arr[n] = self.arr[n] + 1
      if (self.arr[n] > max(self.arr)):
        self.arr[n] = 0
      #elif (self.arr[n]) in ( self.arr[:n] + self.arr[(n+1):] ):
      #  self.increase(n)

    out = 0
    for i in xrange(len(self.arr)):
      out = out + self.arr[i] * 10**i
    
  def result(self):
    arrlen = len(self.arr)
    for i in xrange( arrlen ** 3 ): #math.factorial(len(self.arr)) ):
      print self.arr
      self.increase(0)
  ##unfinished


#print problem1().result()
#print problem2().result()
#print problem3().result()
#print problem4().result()
#print problem5().result()
#print problem6().result()
problem24().result()

