import numpy as y
n,*g=open("puzzle4_input.txt").read().split("\n\n")
g=y.array([[list(map(int,r.split())) for r in a.split("\n")] for a in g])
def s(a):
    b=a*0
    for i,m in enumerate(n.split(",")):
        b[a==int(m)]=1
        if any(b.all(0)|b.all(1)):return i,int(m)*a[b!=1].sum()
print([a[1] for a in sorted(map(s,g))[::len(g)-1]])