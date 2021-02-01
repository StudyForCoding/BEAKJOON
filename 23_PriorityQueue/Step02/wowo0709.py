import sys
from heapq import *

N = int(input())
heap = []
for _ in range(N):
    cmd = int(sys.stdin.readline())
    if cmd == 0:
        if not heap:  print(0)
        else:  print(heappop(heap))
        continue
    # heapq 모듈은 최소힙이다.
    heappush(heap,cmd)