from collections import Counter as c
g=lambda a,b:t(range(a,b+(s:=1-2*int(a-b>0)),s))
w=lambda o,t:max(o,t)if o<t else 1
t=list
def e(l):x,y = zip(*map(lambda c:[int(d) for d in c.split(",")], l.split(" -> ")));m=len(x:=g(*x));n=len(y:=g(*y));x*=w(m,n);y*=w(n,m);r=t(zip(x, y));return r*int(n!=m),r
print([sum(map(lambda x:x>1,c(p).values())) for p in[sum(l,[]) for l in zip(*[e(l)for l in open("data.txt").readlines()])]])

