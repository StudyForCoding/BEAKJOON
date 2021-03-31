import sys
input = sys.stdin.readline
'''
*** 풀이 과정 ***
1. MAP을 입력받고 dfs로 각 섬을 라벨링(노드 번호는 2부터)
2. 상하/좌우 방향 탐색으로 섬을 연결할 수 있는 간선 추가
3. mst를 만드는 크루스칼 알고리즘으로 각 섬을 연결 
-> 하나의 라인에서 두 개 이상의 간선이 추가되는 경우 고려!!!
'''
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
            return sum(mst) # 연결 성공
    return -1 # 연결 실패
    
# main
# 과정 1
N,M = map(int,input().split()) # 세로,가로
MAP = []
nodeNum = 2
for i in range(N): MAP.append(list(map(int,input().split())))
for i in range(N):
    for j in range(M):
        if MAP[i][j] == 1:
            dfs(i,j,nodeNum)
            nodeNum += 1
# 과정 2
edges = set([])
max_cnt = [(N,M,'left-right'),(M,N,'up-down')] # 좌우방향, 상하방향
for cnt1,cnt2,cmd in max_cnt:
    for i in range(cnt1):
        w = 0
        for j in range(cnt2):
            if cmd == 'left-right': cur1,cur2 = i,j
            else: cur1,cur2 = j,i
            if w <= 2 and MAP[cur1][cur2] > 1:         # 시작점
                fromN = MAP[cur1][cur2]
                w = 1
            if w > 0 and MAP[cur1][cur2] == 0: w += 1  # 중간점
            if w > 2 and MAP[cur1][cur2] > 1:
                edges.add((w-1,fromN,MAP[cur1][cur2])) # 끝점(은 또다른 시작점)
                fromN = MAP[cur1][cur2]
                w = 1
# 과정 3
parent = [-1 for _ in range(nodeNum)]
print(kruskal(nodeNum-2,list(edges)))