import sys
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
x = int(sys.stdin.readline())

a.sort()

start, end = 0, n - 1
answer = 0

while start < end:
	tmp = a[start] + a[end]
	if tmp > x:
		end -= 1
	else:
		start += 1
	if tmp == x:
		answer += 1
print(answer)