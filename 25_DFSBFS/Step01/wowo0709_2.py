'''
연결 리스트로 풀이: 연결 리스트는 각 정점의 간선들이 정렬된 형태가 아니기 때문에 정렬 과정이 필요
'''
import sys
input = sys.stdin.readline

def dfs(v): # 스택
    visit = []
    s = []
    s.append(v)

    while s:
        v = s.pop()
        if v not in visit:
            visit.append(v)
            # 스택은 뒤부터 나가니 역정렬
            s += sorted(list(graph[v]-set(visit)),reverse=True)
                
    return visit

def bfs(v): # 큐
    visit = []
    q = []
    q.append(v)

    while q:
        v = q.pop(0)
        if v not in visit:
            visit.append(v)
            # 큐는 앞부터 나가니 순정렬
            q += sorted(list(graph[v] - set(visit)))

    return visit


N,M,V = map(int,input().split())
graph = [set([]) for _ in range(N+1)] # 연결 리스트 기반 구현
for _ in range(M):
    x,y = map(int,input().split())
    graph[x].add(y)
    graph[y].add(x)

print(*dfs(V))
print(*bfs(V))