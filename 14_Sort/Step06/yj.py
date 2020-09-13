import sys
N =int(sys.stdin.readline())
num = []
for _ in range(N):
    num.append(list(map(int,sys.stdin.readline().split())))
num = sorted(num)

for i in range(N):
    print(num[i][0],num[i][1])   