#import psutil
#import os

#p = psutil.Process(os.getpid())
#pinfo = p.as_dict()

#print pinfo['memory_percent']
#print pinfo['memory_info'].rss, pinfo['memory_info'].vms

for i in range(250, 270 ):
  for j in range(250, 270):
    if i==j:
      print i,j,i is j 
      
for i in range(-10, 0 ):
  for j in range(-10, 0):
    if i==j:
      print i,j,i is j 
