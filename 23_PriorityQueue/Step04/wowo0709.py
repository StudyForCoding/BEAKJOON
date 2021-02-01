'''
1. 중간값을 찾기 위해 최대힙->최소힙으로 두 힙을 연결(한다고 생각)한다.
2. 홀수번째 수이면 최대힙에 추가한다. 짝수번째 수이면 최소힙에 추가한후 최대힙[0]과 최소힙[0]을 비교하여 최대힙[0]이 더 작은수가 되도록 한다.
3. 자연스레 최대힙[0]이 중간값이 된다. 
'''
import sys
from heapq import *

N = int(input())
max_heap,min_heap = [],[]

for _ in range(N):
    num = int(sys.stdin.readline())
    if len(max_heap) == len(min_heap):
        heappush(max_heap,(-num,num))
    else:
        heappush(min_heap,num)
    if min_heap and max_heap[0][1] > min_heap[0]:
        tmp_max = heappop(max_heap)[1]
        tmp_min = heappop(min_heap)
        heappush(max_heap,(-tmp_min,tmp_min))
        heappush(min_heap,tmp_max)

    print(max_heap[0][1])