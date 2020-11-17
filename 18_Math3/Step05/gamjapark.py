import sys

def gcd(a, b):
	while b:
		a, b = b, a%b
	return a

N = int(sys.stdin.readline())
nums = [int(sys.stdin.readline()) for _ in range(N)]
nums.sort()

a = min(nums)

for i in range(N):
	if nums[i] > a:
		nums[i] -= a
nums.remove(a)

temp = nums[0]
for i in range(len(nums)):
	temp = gcd(temp, nums[i])

for i in range(2, temp + 1):
	if temp % i == 0:
		print(i, end=' ')
