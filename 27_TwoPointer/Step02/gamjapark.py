import sys
n = int(sys.stdin.readline())
f = list(map(int, sys.stdin.readline().split()))

f.sort()

start, end = 0, n - 1
answer = 0

result = sys.maxsize
res_start, res_end = start, end

while start < end:
	tmp = f[start] + f[end]
	if abs(result) > abs(tmp):
		result = tmp
		res_start, res_end = f[start], f[end]
	if tmp > 0:
		end -= 1
	else:
		start += 1

print(res_start, res_end)