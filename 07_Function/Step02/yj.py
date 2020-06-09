def d(n):
    for i in str(n):
        n+=int(i)
    return n

num=set(range(1,10001))
nselfnum=set()
for j in range(1,10001):
    nselfnum.add(d(j))
selfnum = num - nselfnum

for i in sorted(selfnum):
    print(i)