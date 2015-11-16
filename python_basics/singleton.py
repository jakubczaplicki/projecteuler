__author__ = 'jc60'
def f():
  if f.obj is None:
    f.obj = A()
  return f.obj

#f.obj = None
#print f.obj

class A(object):
    def __init__(self, _val):
        self.val = _val

    def foo(self,x):
        print "executing foo(%s,%s)"%(self,x)
        self.val = x
        return self

    @classmethod
    def class_foo(cls,x):
        print "executing class_foo(%s,%s)"%(cls,x)
        return cls(x)

    @staticmethod
    def static_foo(x):
        print "executing static_foo(%s)"%x

a=A(0)
aa = a.foo(111)
print aa.val
print a == aa
b =  a.class_foo(1)
B =  A.class_foo(2)
a.static_foo(1)
A.static_foo('hi')
print b.val
print B.val
print b==B