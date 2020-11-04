import sys
N =int(sys.stdin.readline())

time = list(map(int, sys.stdin.readline().split()))
time.sort()

num =0
for j in range(N):
    num+=time[j]*(N-j)
print(num)