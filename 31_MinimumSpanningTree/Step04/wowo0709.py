import sys
input = sys.stdin.readline
from math import sqrt
sys.setrecursionlimit(10**9)
# find root node
def find(a):
    if parent[a] < 0:
        return a
    p = find(parent[a])
    parent[a] = p
    return p
# merge two trees
def union(a,b):
    a = find(a)
    b = find(b)

    if a == b: return False

    if parent[a] < parent[b]:
        parent[a] += parent[b]
        parent[b] = a
    else:
        parent[b] + parent[a]
        parent[a] = b
    return True
# find MST
def kruskal(n,edges):
    mst = []
    edges.sort()
    for edge in edges:
        w,a,b = edge
        if union(a,b): 
            mst.append(w)
        if len(mst) == n-1:
            break
    return sum(mst) # return total weight
# calulate distance
def dist(a,b):
    return sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)

# main
N,M = map(int,input().split())
parent = [-1 for _ in range(N+1)]
c,edges = [],[]
for i in range(N):
    c.append(list(map(int,input().split())))
    for j in range(i):
        edges.append([dist(c[j],c[i]),j+1,i+1])
for _ in range(M):
    a,b = map(int,input().split())
    union(a,b)
print("%.2f"%kruskal(N,edges))