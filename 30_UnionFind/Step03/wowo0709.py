import sys
input = sys.stdin.readline

def find(x):
    if not isinstance(parent[x],str) and parent[x] < 0:
        return x
    p = find(parent[x])
    parent[x] = p
    return p

def union(x,y):
    x = find(x)
    y = find(y)

    if x == y: return

    if parent[x] < parent[y]:
        parent[x] += parent[y]
        parent[y] = x
    else:
        parent[y] += parent[x]
        parent[x] = y

# main
for _ in range(int(input())):
    F = int(input())
    parent = {}
    for _ in range(F):
        a,b = input().rstrip().split()
        if a not in parent.keys(): parent[a] = -1
        if b not in parent.keys(): parent[b] = -1
        union(a,b)
        print(-parent[find(a)])

