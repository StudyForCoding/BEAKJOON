import sys
from collections import deque

#list 사용시 시간초과 -> list에서 deque로 변경
N = int(sys.stdin.readline())
s = deque()
size = 0
for i in range(N):
	c = sys.stdin.readline().split()
	if c[0] == 'push':
		s.append(c[1])
		size += 1
	elif c[0] == 'size':
		print(size)
	elif c[0] == 'empty':
		if size == 0:
			print(1)
		else:
			print(0)
	else:
		if size == 0:
			print(-1)
			continue
		if c[0] == 'pop':
			size -= 1
			print(s.popleft())
		elif c[0] == 'front':
			print(s[0])
		elif c[0] == 'back':
			print(s[size-1])