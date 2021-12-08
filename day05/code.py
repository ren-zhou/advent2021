from collections import Counter as c
q=list
g=lambda a,b:q(range(a,b+(s:=1-2*(a-b>0)),s))
w=lambda o,t:t<=o or t
def e(l):x,y=zip(*map(lambda c:q(map(int,c.split(","))),l.split(" -> ")));m=len(x:=g(*x));n=len(y:=g(*y));x*=w(m,n);y*=w(n,m);r=q(zip(x,y));return(n!=m)*r,r
print([sum([1<c(p)[k]for k in c(p)])for p in[sum(l,[])for l in zip(*[e(l)for l in open("example.txt").readlines()])]])

from collections import Counter as t
d=[sorted([list(map(int,p.split(",")))for p in l.split(" -> ")])for l in open("example.txt")]
print(d)
n=t()
s=lambda x:print(list(x)) or print("---")or n.update(x)or sum(1<n[k]for k in n)
print([s((p[0]+i*k,p[1]+j*k)for i,j in[[0,1],[1,0]]for p,q in d if p[i]==q[i]for k in range(q[j]-p[j]+1)),s((p[0]+k,p[1]+i*k)for i in[1,-1]for p,q in d if p[0]<q[0]and i*p[1]<i*q[1]for k in range(q[0]-p[0]+1))])