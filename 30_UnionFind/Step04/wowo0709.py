import sys
input = sys.stdin.readline

def find(x):
    if parent[x] < 0:
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
cycle_flag,ans = False,0
n,m = map(int,input().split())
parent = [-1 for _ in range(n+1)]
for i,_ in enumerate(range(m)):
    x,y = map(int,input().split())
    if not cycle_flag:
        if find(x) == find(y):
            ans = i+1
            cycle_flag = True
        else:
            union(x,y)
print(ans)
