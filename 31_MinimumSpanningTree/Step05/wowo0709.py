import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
# find root node
def find(a):
    if parent[a] < 0:
        return a
    parent[a] = find(parent[a])
    return parent[a]
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

# main
# 문제의 조건을 활용하여 각 좌표 별로 N-1개의 간선만을 추가하는 것이 핵심!
N = int(input())
parent = [-1 for _ in range(N+1)]
cs,edges = [],[]
for i in range(1,N+1): # 좌표 입력
    x,y,z = map(int,input().split())
    cs.append([x,y,z,i]) # x,y,z,node
for i in range(3): # 각 좌표에 대하여 정렬
    cs.sort(key=lambda c:c[i])
    for j in range(N-1): # 정렬된 노드 사이의 거리를 차례로 간선에 추가
        edges.append([abs(cs[j][i]-cs[j+1][i]),cs[j][3],cs[j+1][3]])

edges.sort()
print(kruskal(N,edges))


