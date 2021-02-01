import sys
n, k= map(int, sys.stdin.readline().split())

def power(a, b):
	if b == 0:
		return 1
	if b % 2:
		return (power(a, b//2) ** 2 * a) % P
	else:
		return (power(a, b//2) ** 2) % P

P = 1000000007

f = [1 for _ in range(n + 1)]
for i in range(2, n + 1):
	f[i] = (f[i - 1] * i) % P

A = f[n]
B = (f[n-k]*f[k])%P
print((A % P) * (power(B, P-2) %P) % P)	#페르마의 소정리: N!%P * (K!(N-K)!)^(p-2)%P

