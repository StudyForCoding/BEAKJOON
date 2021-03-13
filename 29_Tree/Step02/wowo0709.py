import sys
input = sys.stdin.readline
from collections import deque

def bfs(v):
    dp = [-1 for _ in range(V+1)]
    dp[v] = 0
    q = deque()
    q.append(v)
    while q:
        cv = q.popleft()
        for nc,nv in tree[cv]:
            if dp[nv] == -1: # 아직 들르지 않았다면,
                dp[nv] = dp[cv] + nc
                q.append(nv)
    return dp
# main
V = int(input())
tree = [[] for _ in range(V+1)]
for _ in range(V):
    vs = list(map(int,input().split()))
    cv = vs[0]
    for i in range(1,len(vs),2):
        if vs[i] == -1: break
        tree[cv].append((vs[i+1],vs[i])) # 가중치, 이어진 정점
ds = bfs(1)           # 임의의 정점으로부터의 거리 계산
v = ds.index(max(ds)) # 거리가 최대인 정점을 찾음
print(max(bfs(v)))    # 찾은 정점으로부터의 최대 거리 계산
