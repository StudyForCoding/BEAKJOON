import sys
from collections import deque

N = int(sys.stdin.readline())
s = deque()
size = 0
for i in range(N):
	c = sys.stdin.readline().split()
	if c[0] == 'push_front':
		s.appendleft(c[1])
		size += 1
	elif c[0] == 'push_back':
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
		if c[0] == 'pop_front':
			size -= 1
			print(s.popleft())
		elif c[0] == 'pop_back':
			size -= 1
			print(s.pop())
		elif c[0] == 'front':
			print(list(s)[0])
		elif c[0] == 'back':
			print(list(s)[size-1])


