N = int(input())
nums = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

max_ = -1000000001
min_ = 1000000001

def solution(n, idx, a, s, m, d):
	global max_, min_
	if idx == N:
		max_ = max(max_, n)
		min_ = min(min_, n)
		return
	else:
		if a:
			solution(n + nums[idx], idx + 1, a - 1, s, m, d)
		if s:
			solution(n - nums[idx], idx + 1, a, s- 1, m, d)
		if m:
			solution(n * nums[idx], idx + 1, a, s, m - 1, d)
		if d:
			if n < 0:
				n = -n
				temp = n // nums[idx]
				temp = -temp
				solution(temp, idx + 1, a, s, m, d - 1)
			else:
				solution(n // nums[idx], idx + 1, a, s, m, d - 1)

solution(nums[0], 1, add, sub, mul, div)
print(max_)
print(min_)