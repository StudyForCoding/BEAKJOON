import sys
from heapq import *

N = int(input())
heap = []
for _ in range(N):
    cmd = int(sys.stdin.readline()) # 일반 input() 사용시 시간초과
    if cmd == 0:
        if not heap:  print(0)
        else:  print(heappop(heap)[1])
        continue
    # heapq 모듈은 최소힙이다. 이를 우선순위를 이용하면 최대힙으로 활용할 수 있다. 
    heappush(heap,(-cmd,cmd))