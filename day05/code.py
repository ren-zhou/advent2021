from collections import defaultdict

with open("example.txt") as f:
    data = f.readlines()

d = defaultdict(lambda: 0)

for line in data:
    pair = list(map(lambda s: s.split(","),line.strip().split(" -> ")))
    if pair[0][0] == pair[1][0]:
        s = sorted([int(pair[0][1]), int(pair[1][1])])
        s[1] +=1
        for i in range(*s):
            d[(int(pair[0][0]),i)] += 1
    elif pair[0][1] == pair[1][1]:
        s = sorted([int(pair[0][0]), int(pair[1][0])])
        s[1] += 1
        for i in range(*s):
            d[(i,int(pair[0][1]))] += 1

print(sum(map(lambda x: x > 1, d.values())))

# =========

from collections import Counter

def special_range(a,b):
    sign = 1 - 2*int(a-b > 0)
    return list(range(a,b+sign,sign))

def expand(line):
    x,y = zip(*map(lambda coord: [int(d) for d in coord.split(",")], line.split(" -> ")))
    srx = special_range(*x)
    sry = special_range(*y)
    print(srx, sry)
    srx *= max(len(srx), len(sry)) if len(srx) < len(sry) else 1
    sry *= max(len(srx), len(sry)) if len(srx) > len(sry) else 1
    return list(zip(srx, sry))

all_coord = sum([expand(l) for l in data],[])
# print((all_coord))
print("*---")
# print(Counter(all_coord).items())
print(sum(map(lambda x: x > 1, Counter(all_coord).values())))

for i in range(10):
    s = ''
    for j in range(10):
        s += str(Counter(all_coord).get((j,i), 0)) + " "
    print(s)