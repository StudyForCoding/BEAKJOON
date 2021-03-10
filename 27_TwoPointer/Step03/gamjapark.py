import sys
N, S = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))

start, end = 0, 0
tmp_sum = 0
result = N + 1
while start <= end:
	if tmp_sum >= S:
		result = min(result, end - start)
		tmp_sum -= a[start]
		start += 1
	elif end == N:
		break
	else:
		tmp_sum += a[end]
		end += 1


if result == N + 1:
	print(0)
else:
	print(result)
