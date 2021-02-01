import sys
from heapq import *

N = int(input())
heap = []

for _ in range(N):
    cmd = int(sys.stdin.readline())
    if cmd == 0:
        if not heap:  print(0)
        else:  print(heappop(heap)[1])
        continue
    heappush(heap,(abs(cmd),cmd))