#276ms
import sys
import heapq

N = int(sys.stdin.readline())

left_len = right_len = 0

maxHeap, minHeap = [], []

for i in range(N):
	n = int(sys.stdin.readline())
	if left_len == right_len:
		heapq.heappush(maxHeap, -n)
		left_len += 1
	else:
		right_len += 1
		heapq.heappush(minHeap, n)
	if minHeap and ((-maxHeap[0]) > minHeap[0]):
		left_max = heapq.heappop(maxHeap)
		right_min = heapq.heappop(minHeap)
		heapq.heappush(minHeap, -left_max)
		heapq.heappush(maxHeap, -right_min)

	print(-maxHeap[0])