import sys
N =int(sys.stdin.readline())
num = []
for _ in range(N):
    x,y = map(int,sys.stdin.readline().split())
    num.append([y,x])

num = sorted(num)

for i in range(N):
    print(num[i][1],num[i][0])    