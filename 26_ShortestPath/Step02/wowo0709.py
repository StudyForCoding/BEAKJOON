import sys
input = sys.stdin.readline
from heapq import heappush,heappop
INF = float('inf')
# 다익스트라 알고리즘에서는 도착지점에 이를 경우 return하는 방식이 아닌
# 모든 지점에 대한 최단 경로를 구한 뒤 값들을 비교한다. 
def dijkstra(startV):
    c,c[startV] = [INF for _ in range(V+1)],0
    hp = []
    heappush(hp,(c[startV],startV))
    while hp:
        cc,cv = heappop(hp)
        for nc,nv in graph[cv]:
            tmp_c = cc + nc
            if c[nv] <= tmp_c: continue
            c[nv] = tmp_c
            heappush(hp,(c[nv],nv))
    return c

V,E = map(int,input().split())
graph = [set([]) for _ in range(V+1)]
for _ in range(E):
    a,b,c = map(int,input().split())
    graph[a].add((c,b))
    graph[b].add((c,a))
v1,v2 = map(int,input().split())

one_ = dijkstra(1) # 1에서의 최단경로
v1_ = dijkstra(v1) # v1에서의 최단경로
v2_ = dijkstra(v2) # v2에서의 최단경로
# 1->v1->v2->V 와 1->v2->v1->V 를 비교
ans = min(one_[v1]+v1_[v2]+v2_[V],one_[v2]+v2_[v1]+v1_[V])
print(ans if ans < INF else -1)