import sys
N = int(sys.stdin.readline())

def fact(n):
	if n <= 1:
		return 1
	else:
		return n * fact(n-1)

ttt = str(fact(N))
answer = 0
for i in ttt[::-1]:
	if i == '0':
		answer += 1
	else:
		print(answer)
		break
