# === Part 1 ===

# === dict lambda: 128 char ===
d={}
[(lambda a,b:d.__setitem__(a[0],d.get(a[0],0)+int(b)))(*l.split()) for l in open("data.txt")]
print((d['d']-d['u'])*d['f'])

# === dict func: 118 char ===
d={}
def f(a,b):
 d[a[0]]=d.get(a[0],0)+int(b)
[f(*l.split()) for l in open("data.txt")]
print((d['d']-d['u'])*d['f'])

# === dict for loop: 102 char ===
d={}
for l in open("data.txt"):
 d[l[0]]=d.get(l[0],0)+int(l.split()[1])
print((d['d']-d['u'])*d['f'])

d={k:0 for k in "duf"}
d={'d':0,'u':0,'f':0}
for l in open("data.txt"):
 d[l[0]]+=int(l.split()[1])
print((d['d']-d['u'])*d['f'])

# === imaginary number: 118 char ===
n=sum((lambda a,b:{'d':1,'u':-1,'f':1j}[a[0]]*int(b))(*l.split()) for l in open("data.txt"))
print(int(n.real*n.imag))

# == reduce: 202 char ===
from functools import reduce
(lambda x:print(x[0]*x[1]))(reduce(lambda x,y:(lambda h,d,k,v:[h+(k=='f')*v,d+{'d':1,'u':-1,'f':0}[k]*v])(*x,y[0][0],int(y[1])),[l.split() for l in open("data.txt")],[0]*2))

# === Part 2 ===

# === reduce: 219 char ===
from functools import reduce
(lambda x:print(x[0]*x[1]))(reduce(lambda x,y:(lambda h,d,a,k,v:[h+(k=='f')*v,d+(k=='f')*a*v,a+{'d':1,'u':-1,'f':0}[k]*v])(*x,y[0][0],int(y[1])),[l.split() for l in open("data.txt")],[0]*3))


# === 2-in-1: 244 char ===
from functools import reduce
print([(lambda x,y,_:x*y)(*reduce(lambda x,y:f(*x,lambda i:(y[0]=='fdu'[i])*int(y.split()[1])),open("data.txt"),[0]*3)) for f in [lambda h,d,a,g:[h+g(0),d+g(1)-g(2),a],lambda h,d,a,g:[h+g(0),d+g(0)*a,a+g(1)-g(2)]]])

# === more readable version of above ===
print([
    (lambda x,y,_:x*y)(
        *reduce(
            lambda x,y:f(*x,lambda i:(y[0]=='fdu'[i])*int(y.split()[1])),
            open("data.txt"),
            [0]*3
        )
    ) for f in [
        lambda h,d,a,g:[h+g(0),d+g(1)-g(2),a],
        lambda h,d,a,g:[h+g(0),d+g(0)*a,a+g(1)-g(2)]
    ]
])

# === the real 2-in-1: 188 char ===
from functools import reduce
x,y,z=reduce(lambda x,y:(lambda h,d,a,g:[h+g(0),d+g(0)*a,a+g(1)-g(2)])(*x,lambda i:(y[0]=='fdu'[i])*int(y.split()[1])),open("data.txt"),[0]*3)
print([x*z,x*y])