d={}
[(lambda a,b:d.__setitem__(a[0],d.get(a[0],0)+int(b)))(*l.split()) for l in open("data.txt")]
print((d['d']-d['u'])*d['f'])

n=sum((lambda a,b:{'d':1,'u':-1,'f':1j}[a[0]]*int(b))(*l.split()) for l in open("data.txt"))
print(int(n.real*n.imag))

hor, dep, aim = 0, 0, 0
for line in open("data.txt"):
    key, val = line.split()
    key, val = key[0], int(val)
    hor += (key == 'f') * val
    dep += {'d':1, 'u':-1, 'f':aim, 'a':0}[key] * val
    aim += (key == 'a') * val
print(hor * dep)

from functools import reduce
(lambda x:print(x[0]*x[1]))(reduce(lambda x,y:(lambda h,d,k,v:[h+(k=='f')*v,d+{'d':1,'u':-1,'f':0}[k]*v])(*x,y[0][0],int(y[1])),[l.split() for l in open("data.txt")],[0]*2))

(lambda x:print(x[0]*x[1]))(reduce(lambda x,y:(lambda h,d,a,k,v:[h+(k=='f')*v,d+(k=='f')*a*v,a+{'d':1,'u':-1,'f':0}[k]*v])(*x,y[0][0],int(y[1])),[l.split() for l in open("data.txt")],[0]*3))