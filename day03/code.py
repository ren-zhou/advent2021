d=open("example.txt").read().split()
f=lambda *a:str(int(2*sum(map(int,a))/len(a)))
g=lambda *a:str(1-int(f(*a)))
n=[int(''.join(r),2) for r in (map(f,*d),map(g,*d))]
print(n[0]*n[1])

s=d
i=0
while s[1:]:
    s=[x for x in s if list(map(f,*s))[i]==x[i]]
    i+=1
print(s)