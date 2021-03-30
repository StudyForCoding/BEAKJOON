import sys
input = sys.stdin.readline

# dfs
dpos = [(0,1),(0,-1),(-1,0),(1,0)]
def dfs(x,y,n):
    MAP[x][y] = n
    for dx,dy in dpos:
        nx,ny = x+dx,y+dy
        if 0<=nx<N and 0<=ny<M and MAP[nx][ny] == 1:
                dfs(nx,ny,n)
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
            # print(*mst,sep='\n')
            return sum(mst) # 연결 성공
    return -1 # 연결 실패
    
# main
N,M = map(int,input().split()) # 세로,가로
MAP = []
nodeNum = 2
for i in range(N): MAP.append(list(map(int,input().split())))
for i in range(N):
    for j in range(M):
        if MAP[i][j] == 1:
            dfs(i,j,nodeNum)
            nodeNum += 1

edges = set([])
# max_cnt = [(N,M),(M,N)] # 좌우방향, 상하방향
for i in range(N): # 좌우방향 탐색
    w = 0
    for j in range(M):
        if w <= 2 and MAP[i][j] > 1: 
            fromN = MAP[i][j]
            w = 1
        if w > 0 and MAP[i][j] == 0: w += 1
        if w > 2 and MAP[i][j] > 1: 
            edges.add((w-1,fromN,MAP[i][j]))
            fromN = MAP[i][j]
            w = 1
for i in range(M): # 상하방향 탐색
    w = 0
    for j in range(N):
        if w <= 2 and MAP[j][i] > 1: 
            fromN = MAP[j][i]
            w = 1
        if w > 0 and MAP[j][i] == 0: w += 1
        if w > 2 and MAP[j][i] > 1: 
            edges.add((w-1,fromN,MAP[j][i]))
            fromN = MAP[j][i]
            w = 1

#print(*MAP,nodeNum,edges,sep='\n')
parent = [-1 for _ in range(nodeNum)]
print(kruskal(nodeNum-2,list(edges)))

 