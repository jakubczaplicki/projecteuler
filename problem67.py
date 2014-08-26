
import math

def blad():
    ins = open( "triangles_18.txt", "r" )
    arr = []
    idx = 0
    for line in ins:
        try:
          l = [int(x) for x in line.split()]
          if ( l[idx] < l[idx+1] ):
            idx += 1
        except IndexError:
          pass
        arr.append(l[idx])
    ins.close()
    print arr
    print sum(arr) #6580

    # 3
    # 7 4
    # 2 4 6
    # 8 5 9 3

def all(n):
  arr = []
  for s in format(n, '100b'):
    arr.append(int(s))
  #print arr
  idx = 0
  items = []
  sum = 0
  ins = open( "triangles_18.txt", "r" )
  for i,line in enumerate(ins):
      l = [int(x) for x in line.split()]
      idx += arr[i]
      #print idx
      try:
        sum += l[idx]
      except IndexError:
        print "Out of range: ", idx, "arr:", l
  ins.close()
  return sum
   
sums = []
n = 2**99
for i in xrange(n):
  print i, n
  sums.append(all(i))
print max(sums)