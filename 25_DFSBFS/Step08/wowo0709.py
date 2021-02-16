import sys
input = sys.stdin.readline
from collections import deque 

dpos = ['+1','-1','*2']

def bfs(x):
    q = deque()
    q.append(x)
    visited[x] = 1
    while q:
        x = q.popleft()
        if x == K:  return visited[K]
        for dx in dpos:
            nx = eval('x'+dx)
            if 0<=nx<=100000:
                if not visited[nx]:
                    q.append(nx)
                    visited[nx] = visited[x]+1


N,K = map(int,input().split())
visited = [0 for _ in range(100001)]
print(bfs(N)-1)