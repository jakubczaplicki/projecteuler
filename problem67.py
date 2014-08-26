# Project Euler
# problems 18 and 67

def generic():
  data = []
  ins = open( "triangles.txt", "r" )
  for i,line in enumerate(ins):
      data.insert(0, [int(x) for x in line.split()] )
  ins.close()
  for n,d in enumerate(data):
    if n == 0: pass
    else:
      data[n] = [ max(i+data[n-1][nn], i+data[n-1][nn+1]) for nn,i in enumerate(d) ]
  return data[n][0]

def perm(n):
  arr = []
  for s in format(n, '015b'):
    arr.append(int(s))
  #print arr
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

sums = []
n = 2**14
for i in xrange(n):
  sums.append(perm(i))
print "Problem 18:" ,max(sums)
print "Problem 67:", generic()
