import sys
N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

def gcd(a, b):
	while b:
		a, b = b, a%b
	return a

for i in range(1, N):
	aaa = gcd(nums[0], nums[i])
	print(nums[0]//aaa, nums[i]//aaa, sep='/')