


def fibr(n):
    if n<=1:
        return 1
    else:
        return n+fibr(n-1)

def fibi(n):
    i=0
    m=0
    while i < n:
        i += 1
        m += i
    return m

for n in xrange(0,10):
    print n, fibi(n), fibr(n)

mygenerator = (x*x for x in range(3))

for i in mygenerator:
    print i
print "2nd"
for i in mygenerator:
    print i

def createGenerator():
    mylist = range(3)
    for i in mylist:
        yield i*i

mygenerator = createGenerator() # create a generator
print(mygenerator) # mygenerator is an object!
for i in mygenerator:
    print(i)


