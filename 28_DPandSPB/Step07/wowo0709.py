from collections import deque

def bfs(a):
    q = deque([[a, '']])
    visited = [0 for _ in range(10000)]
    visited[a] = 1
    while q:
        cn,cmd = q.popleft()
        if cn == b:
            return cmd
        # D
        if not visited[cn * 2 % 10000]:
            visited[cn * 2 % 10000] = 1
            q.append([cn * 2 % 10000, cmd + "D"])
        # S
        if not visited[(cn - 1) % 10000]:
            visited[(cn - 1) % 10000] = 1
            q.append([(cn - 1) % 10000, cmd + "S"])
        # L
        if not visited[cn % 1000 * 10 + cn // 1000]:
            visited[cn % 1000 * 10 + cn // 1000] = 1
            q.append([cn % 1000 * 10 + cn // 1000, cmd + "L"])
        # R
        if not visited[cn % 10 * 1000 + cn // 10]:
            visited[cn % 10 * 1000 + cn // 10] = 1
            q.append([cn % 10 * 1000 + cn // 10, cmd + "R"])

# main
for _ in range(int(input())):
    a,b = map(int, input().split())
    print(bfs(a))
