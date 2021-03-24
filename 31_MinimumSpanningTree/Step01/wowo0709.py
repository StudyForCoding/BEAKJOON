import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
# find root node
def find(x):
    if parent[x] < 0:
        return x
    p = find(parent[x])
    parent[x] = p
    return p
# merge two tree
def union(x,y):
    x = find(x)
    y = find(y)

    if x == y: return False

    if parent[x] < parent[y]:
        parent[x] += parent[y]
        parent[y] = x
    else:
        parent[y] += parent[x]
        parent[x] = y
    return True
# find mst (minimum spanning tree)
def kruskal(n,edges):
    mst = []
    # edges.sort()
    for edge in edges:
        x,y = edge
        if union(x,y): 
            mst.append((x,y))
        if len(mst) == n-1: 
            break

    return mst 

# main
for _ in range(int(input())):
    N,M = map(int,input().split()) # node, edge
    parent = [-1 for _ in range(N+1)]
    edges = []
    for _ in range(M):
        a,b = map(int,input().split())
        edges.append((a,b))
    print(len(kruskal(N,edges)))

    
