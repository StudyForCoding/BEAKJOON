import sys
input = sys.stdin.readline
INF = float('inf')
# 벨만-포드 알고리즘: 다익스트라 알고리즘과 같이 최단경로 알고리즘이지만
# 간선의 가중치가 음수가 될 수 있다는 차이점이 있다.
# 중요한 것은 '음수 사이클'이 생길 경우를 고려해야 한다는 것이다. 
def bellman_ford(startV):
    c,c[startV] = [INF for _ in range(N+1)],0
    # 초점 1. 벨만포드 알고리즘은 힙,큐 등의 자료구조를 쓰지 않는다. 
    # -> 전체 경우 탐색(시간복잡도:O(VE)). 시간이 더 오래걸림.
    # 초점 2. 음수 사이클을 탐지하기 위해 인접 간선을 탐색하고 거리 값을 갱신하는
    # 과정을 'N-1' 회로 제한한다. 그래프에서, 시작 정점에서 특정 정점까지 도달하기 위해
    # 거쳐가는 최대 간선의 수는 'N-1' 개이기 때문이다. 
    for it in range(N):             # 갱신 횟수 제한
        for cv in graph.keys():     # 각 정점에 대하여,
    # 초점 3. 현재 정점으로의 최단거리 값이 아직 한번도 갱신되지 않았다면(최단거리 값이 INF라면)
    # 다른 정점으로 탐색을 진행하지 않는다. 간선의 가중치 값이 음수가 될 수 있기 때문에 
    # 'tmp_c < c[nv]'의 코드로는 잡아낼 수 없다. 
            if c[cv] == INF: continue
            for nc,nv in graph[cv]: # 최단거리 갱신
                tmp_c = c[cv] + nc
                if tmp_c < c[nv]:
                    c[nv] = tmp_c
                    if it >= N-1: return -1 # 최단 거리가 N번 이상 갱신된다면 음수 사이클에 갖힌 것 
    return c


N,M = map(int,input().split())
graph = {i+1:[] for i in range(N)}
for _ in range(M):
    A,B,C = map(int,input().split())
    graph[A].append((C,B)) # 방향 그래프
ans = bellman_ford(1)
if ans == -1: print(-1)
else: 
    for c in ans[2:]: print(c if c < INF else -1)