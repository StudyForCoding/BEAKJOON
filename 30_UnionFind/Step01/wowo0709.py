import sys
input = sys.stdin.readline
# 부모 노드 탐색
def find(x):
    if parent[x] < 0: # x가 루트 노드
        return x
    p = find(parent[x])
    parent[x] = p
    return p
# 두 트리를 합침
def union(x,y):
    x = find(x)
    y = find(y)
    # 이미 같은 트리에 속한 노드일 경우
    if x == y: return

    # 두 노드가 속한 트리 중 높이가 낮은 트리를 높은 트리에 합침
    # 루트 노드의 parent[x], parent[y] 값은 음수이므로 값이 작은 경우가 더 높이가 큰 노드이다. 
    if parent[x] < parent[y]:
        parent[x] += parent[y]
        parent[y] = x
    else:
        parent[y] += parent[x]
        parent[x] = y

# main
n,m = map(int,input().split())
parent = [-1 for _ in range(n+1)]
for _ in range(m):
    op,a,b = map(int,input().split())
    if op == 0: union(a,b)
    if op == 1: 
        # 함수 호출 횟수 줄이기
        root_a = find(a)
        root_b = find(b)
        if a == root_b or b == root_a or root_a == root_b:
            print("YES")
        else:
            print("NO")

