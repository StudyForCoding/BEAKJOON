import sys
def isPrime(a):
	if(a < 2):
		return False
	for i in range(2, a):
		if(a % i== 0):
			return False
	return True

N = int(sys.stdin.readline())
if isPrime(N):
	print(N)
else:
	for p in range(2, 10000001):
		if isPrime(N):
			print(N)
			break
		elif N == 1:
			break
		if isPrime(p):
			if N % p == 0:
				while N % p == 0:
					print(p)
					N //= p