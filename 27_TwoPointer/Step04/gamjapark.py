import sys
N = int(sys.stdin.readline())

def prime_list(n):
	arr = [True] * n

	for i in range(2, int(n ** 0.5) + 1):
		if arr[i] == True:
			for j in range(i+i, n, i):
				arr[j] = False

	return [i for i in range(2, n) if arr[i] == True]

a = prime_list(N+1)

start, end = 0, 0
tmp_sum = 0
result = 0
while start <= end:
	if tmp_sum >= N:
		tmp_sum -= a[start]
		start += 1
	elif end == len(a):
		break
	else:
		tmp_sum += a[end]
		end += 1

	if tmp_sum == N:
		result += 1

print(result)
