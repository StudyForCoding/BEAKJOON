import sys
N=int(sys.stdin.readline())

d=[0]*101

d[1]=1
d[2]=1
d[3]=1

for _ in range(N):
    num = int(sys.stdin.readline())
    for i in range(4, num + 1):
        d[i] = d[i - 2] + d[i - 3]
    print(d[num])