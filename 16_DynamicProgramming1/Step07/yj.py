import sys
N=int(sys.stdin.readline())
num=[0]*301
for i in range(1,N+1):
    num[i]=int(sys.stdin.readline())
d=[0]*301
d[1]=num[1]
d[2]=num[1]+num[2]
d[3]=max(num[1]+num[3],num[2]+num[3])

for i in range(4, N + 1):
    d[i] = max(d[i-3]+num[i-1]+num[i],d[i-2]+num[i])
print(d[N])