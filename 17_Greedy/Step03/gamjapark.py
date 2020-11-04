import sys
N = int(sys.stdin.readline())
time = list(map(int, sys.stdin.readline().split()))

time.sort()
answer = 0
for i in range(1,N+1):
	answer += sum(time[:i])
print(answer)