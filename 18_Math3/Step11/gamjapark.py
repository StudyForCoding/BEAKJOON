import sys

def sol(n, x):
	answer = 0
	while n != 0:
		n //= x
		answer += n
	return answer


N, M = map(int, sys.stdin.readline().split())

if M == 0:
	print(0)
    
else:
	print(min(sol(N, 2)-sol(M, 2)-sol(N-M, 2), sol(N, 5)-sol(M, 5)-sol(N-M, 5)))