import sys
N = int(sys.stdin.readline())
s = []
for i in range(N):
	c = sys.stdin.readline().split()
	if c[0] == 'push':
		s.append(int(c[1]))
	elif c[0] == 'pop':
		if not s:
			print(-1)
		else:
			print(s.pop())
	elif c[0] == 'size':
		print(len(s))
	elif c[0] == 'empty':
		if not s:
			print(1)
		else:
			print(0)
	elif c[0] == 'top':
		if not s:
			print(-1)
		else:
			print(s[-1])