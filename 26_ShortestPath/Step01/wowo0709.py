import sys
input = sys.stdin.readline
from heapq import heappush,heappop
INF = sys.maxsize
## c = cost, v = vertex, c~ = current ~, n~ = new ~
def dijkstra(startV): # 다익스트라 알고리즘!! -> 우선순위 큐 활용(bfs를 일반큐 대신 우선순위큐로 구현)
    heap = []
    heappush(heap,(c[startV],startV)) # 최소힙의 정렬 기준으로 해당 노드까지의 최소 비용 제공
    while heap:
        cc,cv = heappop(heap)     # 현재 비용과 노드 pop
        if c[cv] < cc:  continue  # 현재 노드에서, 기존의 비용보다 현재 비용이 크다면 갱신 안함
        for nc,nv in graph[cv]:           # 현재 노드에 인접한 각 노드에 대해
            tmp_c = cc + nc               # 각 노드에서의 비용을 계산하고,
            if tmp_c < c[nv]:             # 계산한 비용이 기존의 비용보다 작다면,
                c[nv] = tmp_c             # 계산한 비용으로 해당 노드까지의 최소비용을 갱신
                heappush(heap,(tmp_c,nv)) # 힙에 (최소비용,노드) 쌍을 push


V,E = map(int,input().split())
startV = int(input())
graph = {i+1:[] for i in range(V)}
c = [INF for _ in range(V+1)] # 해당 노드까지의 최소 비용(동적 프로그래밍)
c[startV] = 0                 # 시작 노드의 최소 비용은 0
for _ in range(E):
    u,v,w = map(int,input().split())
    graph[u].append((w,v))
dijkstra(startV)
for ans in c[1:]:  print(ans if ans is not INF else 'INF')