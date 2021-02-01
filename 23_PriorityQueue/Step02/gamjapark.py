#160ms
import sys
# PriorityQueue보다 빠름
import heapq

N = int(sys.stdin.readline())

A = []
length = 0
for i in range(N):
	c = int(sys.stdin.readline())
	if c == 0:
		if length == 0:
			print(0)
		else:
			length -= 1
			print(heapq.heappop(A))
	else:
		length += 1
		heapq.heappush(A, c)