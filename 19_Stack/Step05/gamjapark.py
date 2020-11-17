import sys
N = int(sys.stdin.readline())

num = 1
s = []
result = []
check = True
for i in range(N):
	n = int(sys.stdin.readline())

	while num <= n:
		s.append(num)
		result.append('+')
		num += 1
	
	if s[-1] == n:
		s.pop()
		result.append('-')
	else:
		print('NO')
		check = False
		break
if check:
	for r in result:
		print(r)
