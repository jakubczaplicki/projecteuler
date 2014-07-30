
input = [1, 5, 2,  
         2, 4, 7,
         3, 6, 9]
         
size = 3

input = [0, 2, 1, 3,
         2, 1, 0, 4,
         3, 3, 3, 3,
         5, 5, 2, 1]
size = 4


input = [1, 0, 2, 5, 8,
         2, 3, 4, 7, 9,
         3, 5, 7, 8, 9,
         1, 2, 5, 4, 2,
         3, 3, 5, 2, 1]
size = 5

output = [0] * len(input)

def getNeighbours(i):
  if i == 0: # top left corner
    return [ 1, size]
  elif i == (size-1): # top right corner
    return [ i-1, i+size]
  elif i == (len(input)-size): # bottom left corner
    return [ i-size, i+1]
  elif i == (len(input)-1): # bottom right corner
    return [ i-size, i-1]
  elif i%(size) == 0: # left edge
    return [ i-size, i+1, i+size]
  elif i <= size: # top edge
    return [ i-1, i+size, i+1]
  elif i >= (len(input)-size): #bottom edge
    return [ i-1, i-size, i+1]
  elif (i+1)%(size) == 0: # right edge
    return [ i-size, i-1, i+size]
  else: # inside
    return [ i-1, i-size, i+1, i+size]

def getMin(i):
  min = float("inf")
  idx = -1
  for n in getNeighbours(i):
    if input[n] < min:
        min = input[n]
        idx = n
  return idx

import operator

basins = {}
n = 0
x = {}
for i in input:
  x[n] = i
  n = n + 1
sorted_input = sorted(x.iteritems(), key=operator.itemgetter(1))
for i,v in sorted_input:
  sink = True
  for n in getNeighbours(i):
    if (input[n] < input[i]):
      sink = False
      break
  if sink:
    #print "Sink at idx:", i
    if (output[i] == 0):
      output[i] = max(output) + 1
  else:
    if (output[getMin(i)] == 0):
      output[getMin(i)] = max(output) + 1
    output[i] = output[getMin(i)]

# count basins
for o in output:
  o = chr(64+o)
  if o in basins:
    basins[o] = basins[o] + 1
  else:
    basins[o] = 1

# print output
str = ''
i = 0
print "Basins: %d" % max(output), basins
for o in output:
    i = i + 1
    str = str + chr(64+o)
    if i%size == 0:
      str = str + "\n"
print str
