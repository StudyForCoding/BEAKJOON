import sys
input = sys.stdin.readline
from collections import deque

def bfs(root):
    dp = [-1 for _ in range(N+1)] # 부모 노드
    q = deque()
    q.append(root)
    dp[root] = 0
    while q:
        cv = q.popleft()
        for nv in tree[cv]:
            if dp[nv] != -1: continue
            dp[nv] = cv
            q.append(nv)
    return dp
# main
N = int(input())
tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    a,b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a) 
print(*bfs(1)[2:],sep='\n')

